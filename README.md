# api-menu-section
This Menu Section REST API was built using the Django Framework due to its simplicity and rapid development capabilities.

Requirements:  
This is a Django app built on `Django 2.2` with `Python 3.6.2`.   

Installation Instructions:  
Run the following commands to get started running this app locally: 
```
$ git clone https://github.com/feliciatrinh/api-menu-section.git  
$ cd api-menu-section  
$ python -m venv venv # use python3 if you have multiple versions of python
$ source venv/bin/activate  
$ pip install -r requirements.txt  
```
```
$ cd menuapi
$ python manage.py migrate  
$ python manage.py runserver
```

Testing the REST Menu API:  
Use any browser or curl to test the API using the URL `http://127.0.0.1:8000/api/menu/`.   

Operations `GET`, `POST`, `PUT`, `DELETE` are supported as follows:   
`GET`:     
```
curl http://127.0.0.1:8000/api/menu/
{"sections":[{"id":1,"name":"Specials of the Day"},{"id":2,"name":"Lunch Specials"},{"id":3,"name":"Dinner Specials"},{"id":4,"name":"Desserts"}]}﻿   
curl http://127.0.0.1:8000/api/menu/3   
{"section":{"id":3,"name":"Dinner Specials"}}  
```
`POST`:  
```
curl -X POST -H "Content-Type: application/json" -d '{"section":{"id":5,"name":"Easter Day Specials"}}' http://localhost:8000/api/menu/
{"success":"Menu section 'Easter Day Specials' created successfully."}
```

To access admin:  
Visit `http://127.0.0.1:8000/admin/` and enter the following:  
Username: `admin`  
Password: `Intern!1`  
