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
  - The website has the functionality of Room booking on specific dates according to availability.
  - User can also print their bookings. Different pages relating to location, tourist spots in Nainital, Booked rooms list page, Gallery page, Contact us page and Event booking page are also added.
  - Django-allauth is used in order to authenticate users. RazorpayAPI in test mode is used in order to enable payments. A post request is made to api from client side.

<img src="https://github.com/Anupamladdha/Himaliyan_Bliss/blob/main/Screenshots/flowchart.png" height = 450/> 
      
### Presentation 
[Project Overview](https://docs.google.com/presentation/d/1yiEVSrla-NAencIITmwhMaNbVrFSWHUFhGFRk4L4Joc/edit#slide=id.p2)

### Visuals
<img src="https://github.com/Anupamladdha/Himaliyan_Bliss/blob/main/Screenshots/homepage.png" height = 450/> 
<img src="https://github.com/Anupamladdha/Himaliyan_Bliss/blob/main/Screenshots/room_booking.png" height = 450/> 
<img src="https://github.com/Anupamladdha/Himaliyan_Bliss/blob/main/Screenshots/rooms.png" height = 450/> 
<img src="https://github.com/Anupamladdha/Himaliyan_Bliss/blob/main/Screenshots/payment.png" height = 450/> 


### Tech Stack
* Server Side : 
   - Django
   - SQLite
   - Razorpay
   
* Client Side : 
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


