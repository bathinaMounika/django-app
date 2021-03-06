# Web Application To Conduct Online Tests [![Generic badge](https://img.shields.io/badge/build-passing-<COLOR>.svg)](https://shields.io/)
 

<p align="center">
<img src="https://raw.githubusercontent.com/bathinaMounika/django-app/master/media/pk.jpg">
</p>

## Requirement
<ul>
    <li>
        python 3.7.1
    </li>
</ul>

### Setup
<ul>
<li>Clone the repo</li>
</ul>

```
git clone https://github.com/bathinaMounika/django-app.git
```
<ul>
<li>Create Virtual Environment</li>
</ul>

```
python -m virtualenv DJANGO
```
```
DJANGO/Scripts/activate.bat    
```
<ul>
<li>install django</li>
</ul>

```
pip install Django
```

```
WARNING: pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
Collecting Django
WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/django/
WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/django/
WARNING: Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/django/
WARNING: Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/django/
WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/django/
```

```
Could not fetch URL https://pypi.org/simple/django/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/django/ (Caused by SSLError("Can't connect to HTTPS URL because the SSL module is not available.")) - skipping
ERROR: Could not find a version that satisfies the requirement django (from versions: none)
ERROR: No matching distribution found for django
WARNING: pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pip/ (Caused by SSLError("Can't connect to HTTPS URL because the SSL module is not available.")) - skipping
```


<h3 align="center">OR</h3>

* Open Anaconda Prompt

* install required packages

```
pip install -r requirements.txt
```

## Run

```
python manage.py createsuperuser

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
``` 

## Type the following in the browser
  http://127.0.0.1:8000/

## Access admin page with

 http://127.0.0.1:8000/admin

## Contributors

- [Bathina Mounika](https://github.com/bathinaMounika)
- Perisetla Pavan Kalyan
- Aishwarya V S




