# DRF_test1
## Running Django app in a container. PostgreSQL is not containerized. 
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
## Restore the database from dump
```
sudo -u postgres psql
createdb drf_test1
psql drf_test1 < drf_test1.dump
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
## Get all manufacturers
```
http://127.0.0.1:8000/api/manufacturers/
```
![2023-03-14 06-49-47 Ubuntu Dev SSD  Работает  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/55321531/224888809-3c6261d0-2381-4e26-8944-f70cba4d94ac.png)
## Get a manufacturer
```
http://127.0.0.1:8000/api/manufacturers/24/
```
![2023-03-14 06-50-03 Ubuntu Dev SSD  Работает  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/55321531/224888699-f8b2862c-0b54-4a2b-aff7-d37d41d58325.png)
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
## Export cars
```
http://127.0.0.1:8000/api/cars/export/?format=xlsx
```
![2023-03-14 06-43-18 Ubuntu Dev SSD  Работает  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/55321531/224887846-4be8402e-765e-4e34-9ad7-bf8b41174384.png)
```
http://127.0.0.1:8000/api/cars/export/?format=csv
```
![2023-03-14 06-45-08 Ubuntu Dev SSD  Работает  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/55321531/224888002-e4253e60-0f05-44c3-8ca7-c9e7594f1ed9.png)
![2023-03-14 06-47-19 Ubuntu Dev SSD  Работает  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/55321531/224888304-de133221-12f6-4505-8cfd-aa8881b2ada1.png)
## Get all comments
```
http://127.0.0.1:8000/api/comments/
```
![2023-03-14 06-51-52 Ubuntu Dev SSD  Работает  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/55321531/224888935-918876cf-f831-4fd8-8ce4-f9e3acc9f672.png)





