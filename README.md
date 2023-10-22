# Cretae Document in multiple Language
## This is small Django application to save multiple languages as jsonfield in one field of models.   
---
## How to run.   
1. Clone this repo. and Go to this repo in terminal.   
2. In terminal type the following commands to install python supported packages.  
`pip install -r requirements.txt`
3. you can run app by typin following command.
` python manage.py runserver 8000`
4. Following api will show you the title of article in different 3 languages (English, French, and Spanish).   
  `http://127.0.0.1:8000/articles/`   
  `http://127.0.0.1:8000/articles/french/`   
  `http://127.0.0.1:8000/articles/spanish/`   
5. You can enetr new article in admin side   
  `http://127.0.0.1:8000/articles/admin`
  > username: admin password: admin123
6. you can add article or change article. runtime you can update languages and get new language control in add/edit form for that new language.   
7. This would be helpful to store this in single json field instead many field but when too many model fields are then it have large field to add up.   
8. you also test it with following commands.   
`python manage.py test`
