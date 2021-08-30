# Himaliyan_Bliss


## Team members
- [Kushal Shah](https://github.com/Kushal-Ajay-Shah)
- [Anupam Laddha](https://github.com/Anupamladdha)

## Table of Contents

* [About the Project](#about-the-project)
  * [Description](#description)
  * [Presentation](#presentation)
  * [Visuals](#visuals)
  * [Tech Stack](#tech-stack)
* [Getting Started](#getting-started)
  * [Installation](#installation)




## About The Project

### Description

  - Himalayan Bliss has been in existence since 1960 and operating as a resort since 1981, Himalayan Bliss is spread across the lush green land of the mountain side of Uttarakhand, with elite facilities.
  - We have used django for the backend along with sqlite as the database.
  - We have used HTML, CSS, JAVASCRIPT, BOOTSTRAP for our frontend web pages.
  - We are using django-allauth in order to authenticate users.We have also used razorpayAPI In order to enable payments. We make a post request to api from client side.

<img src="https://github.com/Anupamladdha/Himaliyan_Bliss/blob/main/Screenshots/flowchart.png" height = 450/> 
      
### Presentation 
[Project Overview](https://docs.google.com/presentation/d/1yiEVSrla-NAencIITmwhMaNbVrFSWHUFhGFRk4L4Joc/edit#slide=id.p2)

### Visuals
<img src="https://github.com/Anupamladdha/Himaliyan_Bliss/blob/main/Screenshots/homepage.png" height = 450/> 
<img src="https://github.com/Anupamladdha/Himaliyan_Bliss/blob/main/Screenshots/room_booking.png" height = 450/> 
<img src="https://github.com/Anupamladdha/Himaliyan_Bliss/blob/main/Screenshots/rooms.png" height = 450/> 
<img src="https://github.com/Anupamladdha/Himaliyan_Bliss/blob/main/Screenshots/payment.png" height = 450/> 


### Tech Stack : 
#### Server Side : 
   - Django
   - SQLite
   - Razorpay
   
#### Client Side : 
 - HTML, CSS, JS
 - Bootstrap


    
## Getting Started
    
### Installation
* Clone the repo
```bash
git clone https://github.com/Anupamladdha/Himaliyan_Bliss
```
* Create a virtual environment and install all dependencies from the requirements.txt file
```bash
$ virtualenve your_env
$ source your_env/bin/activate
$ pip install -r requirements.txt
```
* To start server
```bash
$ python manage.py createsuperuser
$ python manage.py makemigrations
$ python manage.py mirgate
$ python manage.py runserver
```


