# ctf-challenges

## Shell Challenges

### Rem-DockerEsc

Docker priv-esc

### Rem-FilePerm

File permission

## Web Challenges

### Web-DataDown

PHP application that uses a SQLite database for its backend, but it has three key vulnerabilities.

1. Application error handling is not disabled, allowing users to find out extra information about the system
2. The database is easily accessible via a HTTP GET request
3. Passwords are not hashed in the database

In this challenge, the flag is loaded in from /flag.txt in the root of the file system. This is read out to the user when
they login to the admin account.
The admin account password is randomised on the container creation.
Upon user account creation, the DatabaseManager class leaks the location of the SQLite3 database file, which is web accessible.
The user is able to download users.db, viewing the admin account password.


### Web-JasonsToken

Jason is learning about JWTs, but he forgot to set a key! So the data can be modified by a client...


### Web-Swagger

FastAPI Python application which has automatically generated API endpoints.

The application will 

**Vulnerability**: Accidentally exposes endpoint: /api/admin/reset which has no authentication to reset the admin password.

