I have used Antigravity to generate the code for this project.

prompts i used :



Build a complete Student Recruitment Dashboard web app using Python Django (local environment only, no deployment). Use SQLite as the database. Generate clean, beginner-friendly, production-structured code with proper file separation.
Project Requirements:

Create a Django project named:
recruit_dashboard

Create an app named:
students


Core Features:

Model: Student:

Create a Student model with these fields:

name (CharField)
email (EmailField)
course_interest (CharField)
status (choices: New, Contacted, Enrolled, Rejected)



Pages / Views Needed:

1. Add Student Page
Create a form page where users can add new students.
Fields:

Name
Email
Course Interest
Status


Use Django Forms or ModelForms.

2. Student List Dashboard
Create a page that displays all students in a table.

Columns:

Name
Email
Course Interest
Status


Include:

Search by student name
Filter by course_interest
Clean UI using Bootstrap



Project Structure Required:

Generate all required files:

models.py
views.py
forms.py
urls.py (app + project)


Templates:

base.html
student_form.html
student_list.html





Functional Requirements
Also provide:
Admin Setup
Register Student model in admin.py
Commands to Run
Include terminal commands:
django-admin startproject recruit_dashboard .
python manage.py startapp students
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


Extra Requirements:

Use Bootstrap CDN
Use class-based or function-based views (best choice)
Keep code simple and readable
Ensure search/filter works properly
Ready to run locally without errors


Output Format:

Give full code file by file with clear headings like:

students/models.py
students/views.py
students/forms.py
students/urls.py
templates/base.html
templates/student_form.html
templates/student_list.html

Also explain where each file should be placed.




manual changes:
no more manual changes needed, the code is perfect because of the prompts i used and with the help of antigravity.

challenges:

No big challenges, the antigravity given error while prompting the code.i have retried for 5 times and got the perfect code.