# FreelaWay - Django Project

## Simple system to manage jobs. You can register jobs, someone can apply to do the job. Once it is done, the freelancer can upload pics of the job that can be approved or not

### You can:

###### - Signup as contractor or freelancer

###### - Signin

###### - Get a new password by mail if it is forgotten

###### - Upload images

###### - List jobs is status open

###### - See details of each job

###### - Apply to a oppened job

###### - Filter the jobs listing by price, date, category

###### - Update profile and register email to be used if you forget password

###### - As a freelancer you can list the jobs alread applied, post image about status of the job

###### - Using the admin platform, the contractor can change the job status to finish it

---

To run the project you need to have [Python](https://www.python.org/downloads/).

Create a directory to the project and inside of it run this in cmd to create a virtual environment:
`python -m venv venv`

Now you need to activate the virtual environment. If you are under Linux or Mac run in cmd:
`source /venv/bin/activate`

If you are under windows run this in cmd:
`/venv/bin/activate.bat`

Once it is done, run in cmd:
`pip install -r requirements.txt`

In the root directory you have `.env copy`. Rename it to `.env` and put a key in the SECRET_KEY field.

Inside the settings.py file in the freelaway project directory, you have this field:

```
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

For the test purpose, about the email fields, you can put any data because in the `EMAIL_BACKEND` variable we are using: `django.core.mail.backends.console.EmailBackend`
To send the email for real this must be changed to: `django.core.mail.backends.smtp.EmailBackend`

To run the project:
`python manage.py runserver`

To create a super user:
`python manage.py createsuperuser`

To enter the admininstration of the app, in the browser enter:
`http://127.0.0.1/admin/`

Enter the user you created in the step before.

In the cmd run this command to create the tables in database:
`python manage.py migrate`

---

![pic1](./templates/static/jobs/img/pic1.png)
![pic2](./templates/static/jobs/img/pic2.png)
![pic3](./templates/static/jobs/img/pic3.png)
![pic4](./templates/static/jobs/img/pic4.png)
![pic5](./templates/static/jobs/img/pic5.png)
![pic6](./templates/static/jobs/img/pic6.png)

Tiago Mendes
tetigo@gmail.com
