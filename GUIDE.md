# **This is the guide of how I create my project**

## **Step One: Define the project**

This project exist to try to improve the way in that students in EL Salvador are tested in public School.

**Description:** 
  
    A web-based platform for conducting secure online tests with anti-cheating mechanisms.

**Features:**
  
    -User authentication (Students & Teachers)
    -Test & Question Management
    -Timed Tests with Auto-Submission
    -Anti-cheating mechanisms (tab switching detection, copy-paste blocking)
    -Test Results & Analytics

**Tech Stack:**

    -Backend: Django, PostgreSQL
    -Frontend: HTML/CSS/JavaScript
    -Deployment: AWS
    -Setup Instructions (Installation, Running Locally)

## **Step Two: Set up the project**

**Create my directory, the README.md with all the information about the project**

In this step I have create files such as: FEATURES.md in which i broke down as detailed as possible all the functionality
in my project, DATABASE.md with the structure that will be used when creating the Databases.

**Connect the local directory with a GITHUB repository**

1. create a repository in my personal GITHUB
2. Install git locally: 
    git --version  
    git config --global user.name "Your Name"
    git config --global user.email "your-email@example.com"
    cd your-project-folder
    git init
    git remote add origin https://github.com/"your github username"/"Repository name"
    git remote -v
    git add .
    git commit -m "Initial commit: write your commit"
    git branch -M main  # Renames default branch to "main"
    git push -u origin main

3. Set Up a virtual enviroment:

    pip install virtualenv
    virtualenv env
    source env/Scripts/activate

4. Intall Django
    pip install Django

5. Start my Django Project
    django-admin startproject secure_online_testing

    "Create my Django app"
    cd secure_online_testing
    python manage.py startapp exams


    "Open secure_online_testing/settings.py"
    Add "'exams'," to the installed apps

    Run migrations:
    python manage.py migrate

6. Run the server
    python manage.py runserver

7. Create a model in exams and admin interface.


