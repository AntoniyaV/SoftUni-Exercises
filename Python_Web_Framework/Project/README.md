# Cooking Recipes Django web application
The current project represents a Python web application implemented using the Django Framework. It was created as part of the final exam for the SoftUni course "Python Web Framework".
This application is a simple website for sharing cooking recipes. Its functionalities include user and profile creation, profile update as well as sharing, viewing, editing and deleting recipies.

In the project you can find one main package containing three Django applications: accounts, common and recipes. Additionally there are also directories for the HTML templates, static files, media files, uploaded by the user, as well as a tests directory.

### Accounts app
This app contains the following files:

models.py - contains the extended User model as well as the User Profile model linked to it.

forms.py - contains the model forms for the User and User Profile models. It also contains a Sign up form.

manager.py - contains a manager that helps to create and save the extended User.

signals.py - contains signals so that the Profile model will be automatically created and updated when the User instance, to which it is linked, is created and updated.

admins.py - contains the User model admin registration so that it can be available through the Django admin site.

views.py - contains the controllers for the Sign up, Sign in and Sign out functionalities as well as for the Profile details and edit options.

urls.py - contains the paths related to the views.

### Common app
This app contains the following files:

views.py - contains the views for the landing page, a "login required" warning page and pages for the different categories of recipes.

urls.py - contains the paths for the above mentioned views.

### Recipes app
This app contains the following files:

models.py - contains the Recipe model.

validators.py - contains a validator for the "recipe_type" field of the Recipe model.

admin.py - contains the Recipe model admin registration so that recipes can be viewed, added, edited and deleted through the Django admin site.

views.py - contains controllers for the create, edit, delete and details functionalities of the Recipe model.

urls.py - contains the paths for the views.

### Templates folder
Contains the HTML files returned by all the apps views.

### Static folder
Contains two subdirectories - css and images, containg respectively css styles file and default images for the profile and main recipes categories.

### Media folder
Contains all images uploaded by the users in two folders - profiles and recipes.

### Tests folder
Contains a subdirectory for each of the apps which includes tests for the forms, models and views of the app.

### Additional files in the main Django app directory
setting.py - the three apps are added in the INSTALLED_APPS; the database is set to work with PostgreSQL; media and static roots are set; AUTH_USER_MODEL is set to the extended User model.

urls.py - contains the main paths: to the admin and each of the apps.
