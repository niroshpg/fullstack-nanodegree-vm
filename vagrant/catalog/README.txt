#Catalogue

Project Overview
This is an application that provides a list of items within a
variety of categories as well as provide a user registration and
authentication system. Registered users will have the ability to post, edit
and delete their own items.

Why This Project?
Modern web applications perform a variety of functions and provide amazing
features and utilities to their users; but deep down,
it’s really all just creating, reading, updating and deleting data.
This project combines the knowledge of building dynamic
websites with persistent data storage to create a web application
that provides a compelling service to the users.

This project demonstrates how to develop a RESTful web application using the
Python framework Flask along with implementing third-party OAuth authentication.
and then show how to properly use the various HTTP methods available and how
these methods relate to CRUD (create, read, update and delete) operations.


To run this final project

1. git clone https://github.com/niroshpg/fullstack-nanodegree-vm.git

2 cd fullstack-nanodegree-vm\vagrant\

3. Setup VM by ( This will install Vortual Box VM):
   vagrant up

4. Connect to VM with:
    vagrant ssh

5. OAuth setup
Go to the Google Developers Console and register the project
Once you have your credentials, put the IDs and secrets inside client_secrets.json

You will now be able to log in to the app.

6. Within the VM SSH shell, navigate to catalog app:
 cd /vagrant/catalog

7. run db_set_schema.py to create the database schema

8. run db_insert_values.py to populate the database

9. run main.py and navigate to localhost:5000 in your browser

10 When done VM can be shutdown by:
  vagrant halt
