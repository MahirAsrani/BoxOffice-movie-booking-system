# BoxOffice (Django Movie ticket booking system)

The main objective of the Project on BoxOffice Online Movie Ticket Booking System is to manage the details of
Movie, Tickets, Booking, Show Timing, Customer. It manages all the information about Movie, Audi,
Customer, Movie. The project is totally built at administrative end and thus only the administrator is
guaranteed the access. The purpose of the project is to build an application program to reduce the manual
work for managing the Movie, Tickets, Audi, Booking. It tracks all the details about the Booking, Show
Timing, Customer.

## Screenshots 
![alt text](https://user-images.githubusercontent.com/23280462/78024964-dbd92e00-7376-11ea-9dea-fe8c6ccee058.jpg)
![alt text](https://user-images.githubusercontent.com/23280462/78024974-de3b8800-7376-11ea-9231-ed3ff707eb68.png)
![alt text](https://user-images.githubusercontent.com/23280462/78024970-dd0a5b00-7376-11ea-9f7b-29735c7a0e91.png)



## Live Demo
[https://boxofficeonline.herokuapp.com](https://boxofficeonline.herokuapp.com/)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

* MySQL for database
* Python 3

### Installing
A step by step series of examples that tell you how to get a development env running

    - install requirements.txt
    - create .env file and enter all details
    SECRET_KEY = 
    DB_NAME = 
    DB_USER = 
    DB_PASSWORD = 
    DB_HOST = 
    DB_PORT =

### Launch
    python manage.py createsuperuser
    python manage.py migrate
    python manage.py runserver
       

## Built With

* [Bootstrap](https://getbootstrap.com/) - UI Components
* [Django](https://www.djangoproject.com/) - Python web framework
* [MySQL]() - Used for Database

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

