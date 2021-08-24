
Steps to run
=============
install python3 

```
git clone git@github.com:vardhanshah138/stackoverflowclone.git

pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

cd userapp
python manage.py makemigrations 
python manage.py migrate 
python manage.py runserver

```
