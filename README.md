##Installation:
This project was developed under python 3.4. To install all dependencies use the following:
```
pip -r pubmed_central_request/requirements.txt
```

####Database Setup For Postgres:
From a Postgres console the following will create the user and database to be used by the application.
```
CREATE ROLE pubmed_central_request PASSWORD 'Change This’;
ALTER ROLE pubmed_request LOGIN;
CREATE DATABASE pubmed_central_request;
GRANT ALL PRIVILEGES ON DATABASE pubmed_central_request TO pubmed_central_request;
```

Copy example_local.py to local.py pubmed_central_request/pubmed_central_request/settings/ and update with the user, password, and database set with the above commands. Production settings currently read from environment variables for the database user name and password.

####Sqlite:
example_local.py has alternative settings to use sqlite instead of postgres alongside the postgres boilerplate settings. Migrations have only been tested on Postgres

####Initialize Database
The following command will perform the inital setup of the database, creating the tables to be used:
```
python manage.py syncdb
```
The Django admin portion of the site is currently not in use, so creating a super user when prompted from the above command is not necessary.

##Running the Site:
The development server can be run from pubmed_central_request with the following command:
```
python manage.py runserver
```

The default view is the formview to create an article request against PubMed Central. The field presented takes the integer portion of the ID to perform a lookup on it. Once an ID is submitted a detail view with the articles information is displayed. If this is the desired article it can be marked as "accepted". The code to email the author is currently commented out. It reads Mandrill username and passwords from environment variables and sends a preformatted message to the author of listed in pubmed as handling correspondence.
