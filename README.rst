MultiDb
=======

Requirements:
--------------

* Databases: PostgreSQL DB and My SQL DB.
* Django 1.10 with Python.
* Multi setting for local and production environments.
* Proper Readme file with setup instruction.


Description:
--------------
* Project has 2 roles Admin and User
* PostgreSQL has 2 database: database1, database2
* My SQL has 3 database: database3, database4, database5

You need to create a django application where admin cab add users and assign multiple database (database1, database2, database3, database4, database5 ) to a user and when user is created, he should get Email for login and password(or any other way to handle this flow).
When user performs login, he can see the database list, which admin assigned to him.

Then user can create Product by selecting database from the List. Product should be save under selected database.
There should be one page where user can see all product list with database name.

Admin has one page, where he can see all user's and their product details.
(CRUD operation should follow by default.)


Basic Commands
--------------

Install requirments::

    $ pip install -r requirments/local.txt
    
Migrate commands::

    $ python manage.py migrate users
    $ python manage.py migrate products --database=database1
    $ python manage.py migrate products --database=database2
    $ python manage.py migrate products --database=database3
    $ python manage.py migrate products --database=database4
    $ python manage.py migrate products --database=database5


Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser
    
* To create a **database entries**, just go to::

    http://localhost:8000/admin

  Sign In as superuser, go to Databases table and add all 5 databases name entry their i.e (database1, database2, ...)

* To create a **normal user account**, just go to:

  Sign In as superuser, go to Users table, click add user button, Admin can assign databases to user on UserCreation form.


Application Flow
^^^^^^^^^^^^^^^^^^^^^

* To create a **product entries**, just visit::
    
    http://localhost:8000/
    
  Sign In as normal user, User will be redirected to products page, where user can perform CURD on product. 
  On product creation he can select database assigned to him.

