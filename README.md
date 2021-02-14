# About 
<br/>
This is a python/Django project demonstrating Role based Access Control using an example of a car hiring company. It includes CRUD functionalities and REST APIs.<br/>  
### Instrallation & setup
cd requirements  
run: pip3 install -r requirements.txt  
<br/>
run: python3 manage.py makemigrations  
run: python3 manage.py migrate  

#### create superuser  
run: python3 manage.py createsuperuser<br />

run: python3 manage.py runserver <br />

<br>
login to the admin panel 'http://127.0.0.1:8000/admin' and create 2 user groups.<br />
1. customer<br />
2. admin<br />

Then logout;


open http://127.0.0.1:8000/ on your browser
for demo purposes: customer should 1st create an account.

# How the app works
For the purpose of demontrating all functionalities of RBAC, a customer must register an account then login to view available cars.<br/>
On registration he/she is asigned the role of a customer.<br/>
To demontrate admin's functionalities, the superuser can create a admin user or can assign the role of admin to an existing user. The login at http://127.0.0.1:8000/ <br/>

### Postman collection collection is available at the root folder as carpass.postman_collection.json  

## For APIs visit http://127.0.0.1:8000/swagger/



### NB: Developed using python 3 and django 3.1 <br /> 
