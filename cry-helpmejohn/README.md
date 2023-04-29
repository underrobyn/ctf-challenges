# Cry-HelpMeJohn!

You found an old Clam-Corp database for some ancient user management system.

The admin credentials are: `admin:97bf34d31a8710e6b1649fd33357f783`

The flag is in the format: `flag{result of the hash}`


Hint 1: Luckily, people weren't too security conscious back then, so the password only has lower case letters and numbers in it.

Hint 2: You can use JohnTheRipper or HashCat to help you here

Hint 3: Dictionary attacks won't help you too much...



How to solve:

echo "admin:97bf34d31a8710e6b1649fd33357f783" >> ~/password.md5
./john --format=Raw-MD5 --incremental ~/password.md5

Time taken: 2 mins 18 secs on my desktop
