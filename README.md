# Little Lemon Restaurant

Final capstone project for Meta Back-end developer professional certification program on Cousera. This project is a restaurant management system that allows the user to create a menu, add items to the menu, create a booking, and assign a table to the booking.

Course link: [Meta Back-end Developer Professional Certificate ](https://www.coursera.org/professional-certificates/meta-back-end-developer)

## Tech Stack
* Django
* Django REST Framework
* Pipenv
* Docker
* MySQL
* Djoser

##  Installation

1. Clone the repository ```git clone https://github.com/serodas/LittleLemon.git```

2. Create a virtual environment ```pipenv shell```

3. Install the requirements ```pipenv install```

4. Run the migrations ```python manage.py migrate```

5. Run the server ```python manage.py runserver```

6. Run the tests ```python manage.py test```

7. Create a superuser `python manage.py createsuperuser`

#  API paths to test the application

* http://127.0.0.1:8000/restaurant/menu/

* http://127.0.0.1:8000/restaurant/menu/items/

* http://127.0.0.1:8000/restaurant/menu/items/{int:pk}

* http://127.0.0.1:8000/restaurant/booking/

* http://127.0.0.1:8000/restaurant/booking/tables/
