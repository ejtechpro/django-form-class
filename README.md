Django Form Class
In Django, a form class is a Python class used to define the structure and behavior of an HTML form. It is a fundamental part of Django's form handling system, providing a convenient way to create, validate, and process HTML forms. A Django form class is typically a subclass of django.forms.Form. This class defines the fields, widgets, and validation rules for the form. Each form field corresponds to an HTML form input element, and Django takes care of rendering the form in HTML and processing the submitted data.

THE FORM DATA IS STORED/INSERTED INTO postgres db: I used psycopg2 for connection.

Note: Form Class is different from ModelForm so database oparations are performed differently.
