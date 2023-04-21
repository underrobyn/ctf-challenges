import copy
import os
import random
import string
import subprocess
from time import sleep


first_names = [
    "Michael", "Christopher", "Jessica", "Matthew", "Ashley", "Jennifer", "Joshua", "Amanda", "Daniel", "David",
    "James", "Robert", "John", "Joseph", "Andrew", "Ryan", "Brandon", "Jason", "Justin", "Sarah", "William", "Jonathan",
    "Stephanie", "Brian", "Nicole", "Nicholas", "Anthony", "Heather", "Eric", "Elizabeth", "Adam", "Megan", "Melissa",
    "Kevin", "Steven", "Thomas", "Timothy", "Christina", "Kyle", "Rachel", "Laura", "Lauren", "Amber", "Brittany",
    "Danielle", "Richard", "Kimberly", "Amy", "Patrick", "Austin", "Finn", "Gerald", "Alexander"
]
last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Thomas", "Taylor", "Martin", "Bateman",
    "Lee", "Thompson", "White", "Clark", "Lewis", "Robinson", "Walker", "Young", "Hill", "Adams", "Baker", "Acres",
    "Tian", "Hogan", "Edwards", "Langley", "Stoll", "Ford", "Finnegan", "Gray", "Oatrun", "Hart", "Ashford", "Singh"
]

groups_list = ["LocalAdmins", "ProxyUsers", "VPNUsers", "BackupAdmins", "BlogUsers", "LinuxTeam", "DevOpsTeam",
               "SecurityTeam", "NetworkTeam", "WebTeam", "LMSTeam", "DeveloperSoftwareDeployment"]

server_names = ['ITSRV', 'VPNSRV', 'PROXYSRV', 'FILESRV', 'BACKUPSRV', 'DEV', 'WEB', 'LINUXSRV', 'MSDBSRV', 'LMSINTERNAL',
                'SECURITYSRV', 'EMAILSRV', 'FIREWALL', 'FORENSICSRV', 'DEVSIT', 'DEVUAT', 'DEVPROD', 'CICD', 'CLOUD']

add_groups_ldif = """
dn: CN={{GROUP_CN}},OU=Groups,DC=internal,DC=clam-corp,DC=com
changetype: modify
add: member
member: CN={{USER_CN}},CN=Users,DC=internal,DC=clam-corp,DC=com
"""


def random_string(length: int) -> str:
    return ''.join(random.choice(string.ascii_letters + string.digits + '!£&') for _ in range(length))


def create_user(username: str, password: str, first_name: str, last_name: str, retries: int = 0) -> None:
    print(f'Creating user: {first_name} {last_name}, {username}, with password: {password}')

    if retries > 3:
        return

    try:
        cmd = f'sudo samba-tool user create {username} "{password}" --given-name="{first_name}" --surname="{last_name}"'
        subprocess.run(cmd, shell=True, check=True, text=True)
        cmd = f'sudo samba-tool user setexpiry --noexpiry {username}'
        subprocess.run(cmd, shell=True, check=True, text=True)
    except Exception as err:
        print(f'USER CREATION FAILED, RETRYING: {retries}, {err}')
        sleep(1)
        retries = retries + 1
        return create_user(username, password, first_name, last_name, retries)


def create_computer(netbios: str, desc: str, admin: str, retries: int) -> None:
    print(f'Creating computer: {netbios}')

    if retries > 3:
        return

    u = f'CN={admin},CN=Users,DC=internal,DC=clam-corp,DC=com'

    try:
        cmd = f'sudo samba-tool computer create {netbios} --description="{desc}" -U "{u}" --password="Pa55w0rd"'
        subprocess.run(cmd, shell=True, check=True, text=True)
    except Exception as err:
        print(f'computer CREATION FAILED, RETRYING: {retries}, {err}')
        sleep(1)
        retries = retries + 1
        return create_computer(netbios, desc, admin, retries)


def add_user_to_group(username: str, group_name: str) -> bool:
    file_name = f'/tmp/adduser--{group_name.lower()}--{random.randint(10000,99999)}.ldif'
    print(f'adding {username} to {group_name}, ldif: {file_name}')

    with open(file_name, 'w+', encoding='utf-8') as fp:
        ldif_cont = copy.copy(add_groups_ldif)
        ldif_cont = ldif_cont.replace('{{GROUP_CN}}', group_name)
        ldif_cont = ldif_cont.replace('{{USER_CN}}', username)
        fp.write(ldif_cont)

    cmd = f'sudo ldbmodify -H /var/lib/samba/private/sam.ldb {file_name} --option="dsdb:schema update allowed"=true'
    try:
        subprocess.run(cmd, shell=True, check=True, text=True)
    except subprocess.CalledProcessError as err:
        return False

    try:
        os.unlink(file_name)
    except Exception as err:
        return True

    return True


def add_user_to_flag_group(username: str) -> None:
    add_user_to_group(username, 'FlagReaders')



def add_user_groups(username: str) -> None:
    last_result = add_user_to_group(username, "StandardSoftwareDeployment")

    group_add_int = random.randint(1, len(groups_list))
    groups_to_add = random.sample(groups_list, group_add_int)
    for group in groups_to_add:
        try:
            last_result = add_user_to_group(username, group)
        except Exception as err:
            print(err)
            break

        if not last_result:
            return


def do_create_user() -> list[str, str]:
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    rand_user_number = random.randint(100000, 999999)
    username = f"{first_name.lower()}.{last_name.lower()}{rand_user_number}"
    password = random_string(32)

    create_user(username, password, first_name, last_name)
    add_user_groups(f'{first_name} {last_name}')

    return [f'{first_name} {last_name}', username]


def generate_users(num_users: int) -> None:
    # Create user that player will login to
    create_user('rctftechnical', 'RCTF_T3chN1c4l_Us3r!', 'RCTF', 'Technical')

    # Create user from another misc-jeffrey for consistency’s sake
    create_user('jeffrey.jones', 'flag{j3ff_c4nt_k33p_4_s3cr3t}', 'Jeffrey', 'Jones')

    users_list = []
    for _ in range(num_users):
        users_list.append(do_create_user())

    flag_user = random.choice(users_list)
    add_user_to_flag_group(flag_user[1])
    add_user_groups(flag_user[1])

    for server in server_names:
        for i in range(0, random.randint(1,9)):
            create_computer(f'{server}0{i}', f'Computer for team {server}', random.choice(users_list), 0)

    create_computer('EMAILSRV00', 'flag{d1r3ct0ry_5n00p1ng_c4n_b3_fru1tfu1}', flag_user, 0)


if __name__ == "__main__":
    num_users = 50
    generate_users(num_users)
