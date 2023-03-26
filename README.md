# Django Blogs REST API

This is a Django app that allows users to create and manage blog posts. Users can create, view and update the blog posts.

Usage:

Clone the repository: git clone https://github.com/faisal7008/Blogs_RESTAPI.git
Change into the project directory: cd Blogs_RESTAPI
Create a virtual environment: python3 -m venv venv
Activate the virtual environment: source venv/bin/activate (for Linux or Mac) or venv\Scripts\activate (for Windows)
Install the dependencies: pip install -r requirements.txt
Run the migrations: python manage.py migrate
To run the app, use the following command: python manage.py runserver
This will start the development server, and you can access the app in your browser at http://127.0.0.1:8000 or http://localhost:8000/

API Endpoints

To view all the blogs posted: /blogs/all
To create a new blog: /blogs/create
To update an existing blog: /blogs/create/<:id>

Created by Faisal Hussain. It is based on the Django web framework and Django REST framework.
