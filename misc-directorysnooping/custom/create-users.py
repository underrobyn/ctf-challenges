import random
import string
import subprocess


first_names = [
    "Michael", "Christopher", "Jessica", "Matthew", "Ashley", "Jennifer", "Joshua", "Amanda", "Daniel", "David",
    "James", "Robert", "John", "Joseph", "Andrew", "Ryan", "Brandon", "Jason", "Justin", "Sarah", "William", "Jonathan",
    "Stephanie", "Brian", "Nicole", "Nicholas", "Anthony", "Heather", "Eric", "Elizabeth", "Adam", "Megan", "Melissa",
    "Kevin", "Steven", "Thomas", "Timothy", "Christina", "Kyle", "Rachel", "Laura", "Lauren", "Amber", "Brittany",
    "Danielle", "Richard", "Kimberly", "Jeffrey", "Amy", "Patrick"
]
last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Thomas", "Taylor", "Martin", "Bateman",
    "Lee", "Thompson", "White", "Clark", "Lewis", "Robinson", "Walker", "Young", "Hill", "Adams", "Baker", "Acres"
]

groups_list = ["LocalAdmins", "ProxyUsers", "VPNUsers", "BackupAdmins", "BlogUsers", "LinuxTeam", "DevOpsTeam",
               "SecurityTeam", "NetworkTeam", "WebTeam", "LMSTeam"]

add_flag_ldif = """
dn: CN={{USER_CN}},CN=Users,DC=internal,DC=clam-corp,DC=com
changetype: modify
add: flagVariable
flagVariable: "flag{well_done}"
"""

add_groups_ldif = """
dn: CN=LocalAdmins,OU=Groups,DC=internal,DC=clam-corp,DC=com
changetype: modify
add: member
member: CN={{USER_CN}},CN=Users,DC=internal,DC=clam-corp,DC=com
"""


def random_string(length: int) -> str:
    return ''.join(random.choice(string.ascii_letters + string.digits + '!£&') for _ in range(length))


def create_user(username: str, password: str, first_name: str, last_name: str) -> None:
    print(f'Creating user: {first_name} {last_name}, {username}, with password: {password}')
    cmd = f'sudo samba-tool user create {username} "{password}" --given-name="{first_name}" --surname="{last_name}"'
    subprocess.run(cmd, shell=True, check=True, text=True)

    cmd = f'sudo samba-tool user setexpiry --noexpiry {username}'
    subprocess.run(cmd, shell=True, check=True, text=True)


def set_flag(username: str) -> None:
    with open('/tmp/add_flag.ldif', 'w') as f:
        f.write(add_flag_ldif.replace('{{USER_CN}}', username))

    cmd = f'sudo ldbmodify -H /var/lib/samba/private/sam.ldb /tmp/add_flag.ldif --option="dsdb:schema update allowed"=true'
    subprocess.run(cmd, shell=True, check=True, text=True)


def add_user_to_group(username: str, group_name: str) -> None:
    cmd = f'sudo samba-tool group addmembers "{group_name}" {username}'
    subprocess.run(cmd, shell=True, check=True, text=True)


def add_user_groups(username: str) -> None:
    add_user_to_group(username, "StandardSoftwareDeployment")

    group_add_int = random.randint(1, len(groups_list))
    groups_to_add = random.sample(groups_list, group_add_int)
    for group in groups_to_add:
        add_user_to_group(username, group)


def do_create_user() -> list[str, str, str]:
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    rand_user_number = random.randint(100000,999999)
    username = f"{first_name.lower()}.{last_name.lower()}{rand_user_number}"
    password = random_string(32)
    create_user(username, password, first_name, last_name)
    return [f'{first_name} {last_name}', username]


def generate_users(num_users: int) -> None:
    users_list = []
    for _ in range(num_users):
        users_list.append(do_create_user())

    flag_user = random.choice(users_list)
    set_flag(flag_user[0])
    add_user_to_group(flag_user[1], "FlagReaders")
    add_user_groups(flag_user[1])

    # Create user that player will login to
    create_user('rctftechnical', 'RCTF_T3chN1c4l_Us3r!', 'RCTF', 'Technical')

    # Create user from another misc-jeffrey for consistency’s sake
    create_user('jeffrey.jones', 'flag{j3ff_c4nt_k33p_4_s3cr3t}', 'Jeffrey', 'Jones')


if __name__ == "__main__":
    num_users = 100
    generate_users(num_users)
