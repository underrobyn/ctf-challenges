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

add_flag_ldif = """
dn: CN={{USER_CN}},CN=Users,DC=directory,DC=clam-corp
changetype: modify
add: flagVariable
flagVariable: "flag{well_done}"
"""


def random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits + '!£&') for _ in range(length))


def create_user(username, password, first_name, last_name):
    print(f'Creating user: {first_name} {last_name}, {username}, with password: {password}')
    cmd = f'sudo samba-tool user create {username} "{password}" --given-name="{first_name}" --surname="{last_name}"'
    subprocess.run(cmd, shell=True, check=True, text=True)

    cmd = f'sudo samba-tool user setexpiry --noexpiry {username}'
    subprocess.run(cmd, shell=True, check=True, text=True)


def set_flag(username):
    with open('/tmp/add_flag.ldif', 'w') as f:
        f.write(add_flag_ldif.replace('{{USER_CN}}', username))

    cmd = f'sudo ldbmodify -H /var/lib/samba/private/sam.ldb /tmp/add_flag.ldif --option="dsdb:schema update allowed"=true'
    subprocess.run(cmd, shell=True, check=True, text=True)


def add_user_to_group(username):
    cmd = f'sudo samba-tool group addmembers "Flag Readers" {username}'
    subprocess.run(cmd, shell=True, check=True, text=True)



def generate_users(num_users):
    users_list = []
    for _ in range(num_users):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        username = f"{first_name.lower()}.{last_name.lower()}"
        password = random_string(32)
        try:
            create_user(username, password, first_name, last_name)
        except Exception:
            continue

        users_list.append([f'{first_name} {last_name}', username])

    flag_user = random.choice(users_list)
    set_flag(flag_user[0])
    add_user_to_group(flag_user[1])


if __name__ == "__main__":
    num_users = 40
    generate_users(num_users)
