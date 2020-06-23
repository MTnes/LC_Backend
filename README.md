# LC App Backend
We are using django REST framework for backend api. <br />

---
Use a virtual envionment for installing this, 
i.e `venv` or `pipenv`.
### Install Dependencies
For debian based distro, *in virtual evironment* terminal type
```shell
pip install -r requirements.txt
```
### To run the project on local machine
Inside project directory type
```shell
python manage.py makemigrations
python manage.py migrate

# To run with development settings
python manage.py runserver
```
