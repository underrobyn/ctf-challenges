# ctf-challenges

## Web Challenges

### Web-DataDown

PHP application that uses a SQLite database for its backend, but it has three key vulnerabilities.

1. Application error handling is not disabled, allowing users to find out extra information about the system
2. The database is easily accessible via a HTTP GET request
3. Passwords are not hashed in the database

In this challenge, the flag is loaded in from /flag.txt in the root of the file system, this is then set as the admin user
password


### Web-Swagger

FastAPI Python application which has automatically generated API endpoints.

The application will 

**Vulnerability**: Accidentally exposes endpoint: /api/admin/reset which has no authentication to reset the admin password.

