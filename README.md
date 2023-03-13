# DRF_test1
## Running Django app in a container. PostgreSQL not containerized. 
![2023-03-13_17-09-53](https://user-images.githubusercontent.com/55321531/224729146-3f62bd9a-a2d4-499b-9061-c7909dc0a520.png)
## Credentials
```
# PostgreSQL:
database: drf_test1
login: pgadmin
pass: pgadmin_elros

# Django superuser:
login: admin
pass: admin

# Django user:
login: auth_user1
pass: auth_user1pass
token: 862dd9639ae2f456c3e9e9193be74e787d5b2a53
```
## HTTPie
```
sudo apt-get install httpie
```
# Examples
## Get all countries:
```
http GET http://localhost:8000/api/countries/ Authorization:"Token 862dd9639ae2f456c3e9e9193be74e787d5b2a53"
```
![2023-03-13_17-45-23](https://user-images.githubusercontent.com/55321531/224735177-2715b4b2-e608-4d65-a172-a192748867ec.png)
## Get a country:
```
http GET http://localhost:8000/api/countries/4/ Authorization:"Token 862dd9639ae2f456c3e9e9193be74e787d5b2a53"
```
![2023-03-13_17-46-37](https://user-images.githubusercontent.com/55321531/224735615-086cf60a-8ac3-4f53-be5d-c18e171f2aa6.png)
## Get all cars:
```
http GET http://localhost:8000/api/cars/ Authorization:"Token 862dd9639ae2f456c3e9e9193be74e787d5b2a53"
```
![2023-03-13_17-22-56](https://user-images.githubusercontent.com/55321531/224730872-08c178ab-85f3-4159-a397-b0f90362d364.png)
## Get a car
```
http GET http://localhost:8000/api/cars/2/ Authorization:"Token 862dd9639ae2f456c3e9e9193be74e787d5b2a53"
```
![image](https://user-images.githubusercontent.com/55321531/224733503-a4c6acaf-38ea-4467-90f0-130bdb87c186.png)


