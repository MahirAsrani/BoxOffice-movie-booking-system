# BoxOffice (Django Movie ticket booking system)

The main objective of the Project on BoxOffice Online Movie Ticket Booking System is to manage the details of
Movie, Tickets, Booking, Show Timing, Customer. It manages all the information about Movie, Audi,
Customer, Movie. The project is totally built at administrative end and thus only the administrator is
guaranteed the access. The purpose of the project is to build an application program to reduce the manual
work for managing the Movie, Tickets, Audi, Booking. It tracks all the details about the Booking, Show
Timing, Customer.

## Screenshots 

## Live Demo
[https://boxofficeonline.herokuapp.com](https://boxofficeonline.herokuapp.com/)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

MySQL for database
Python 3

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

* [Bootstrap](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Python](https://maven.apache.org/) - Dependency Management
* [MySQL](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

