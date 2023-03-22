import random
import string
import subprocess


first_names = [
    "Michael", "Christopher", "Jessica", "Matthew", "Ashley", "Jennifer", "Joshua", "Amanda", "Daniel", "David",
    "James", "Robert", "John", "Joseph", "Andrew", "Ryan", "Brandon", "Jason", "Justin", "Sarah", "William", "Jonathan",
    "Stephanie", "Brian", "Nicole", "Nicholas", "Anthony", "Heather", "Eric", "Elizabeth", "Adam", "Megan", "Melissa",
    "Kevin", "Steven", "Thomas", "Timothy", "Christina", "Kyle", "Rachel", "Laura", "Lauren", "Amber", "Brittany",
    "Danielle", "Richard", "Kimberly", "Jeffrey", "Amy"
]
last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Thomas", "Taylor", "Martin",
    "Lee", "Thompson", "White", "Clark", "Lewis", "Robinson", "Walker", "Young", "Hill", "Adams", "Baker", "Acres"
]


def random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def create_user(username, password, first_name, last_name):
    cmd = f'sudo samba-tool user create {username} {password} --given-name="{first_name}" --surname="{last_name}"'
    subprocess.run(cmd, shell=True, check=True, text=True)

    cmd = f'sudo samba-tool user setexpiry --noexpiry {username}'
    subprocess.run(cmd, shell=True, check=True, text=True)


def set_flag(username, secret):
    cmd = f'sudo ldbmodify -H /usr/local/samba/private/sam.ldb -a -b "CN={username},CN=Users,DC=localhost,DC=localdomain" --set=flag={secret}'
    subprocess.run(cmd, shell=True, check=True, text=True)


def generate_users(num_users):
    users_list = []
    for _ in range(num_users):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        username = f"{first_name.lower()}.{last_name.lower()}"
        password = random_string(14)
        create_user(username, password, first_name, last_name)

        users_list.append(username)

    flag_user = random.choice(users_list)
    set_flag(flag_user, 'flag{well_done}')


if __name__ == "__main__":
    num_users = 25
    generate_users(num_users)
