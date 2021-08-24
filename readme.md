
Steps to run
=============
install python3 

```
git clone git@github.com:vardhanshah138/stackoverflowclone.git

cd stackoverflowclone/
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt


python manage.py createsuperuser (for creating username and password)
python manage.py makemigrations 
python manage.py migrate 
python manage.py runserver

