![image](https://github.com/user-attachments/assets/8d6c1b5f-46ee-4bfe-8b4b-532579a0de28)
# Super Store
- Welcome to the Super Store Project! This is a Django-based web application for managing customers and orders. The project is designed for simple understanding and extension, with an emphasis on creating RESTFUL APIs, Implementation of data structures, Implementation authentication and authorization via OpenID Connect, writing automated tests at all levels (unit, integration, and acceptance), and integrating CI/CD.
## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Sections](#sections)
- [Screenshots](#screenshots)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview
- A simple Django project that inputs/uploads customers and orders using REST API. Requires users to login or signup using their Google accounts (with the help of Openid Connect). Africastalking sms gateway is implemented to add sms functionality.
## Features

- User authentication with OpenID Connect
- Customer management
- Order processing and management
- Responsive design
- Admin panel for managing users, products, and orders

## Technologies Used

- Django
- Djngorestframework
- MySQL
- mozilla-django-oidc
- HTML, CSS, JavaScript
- Bootstrap
- FontAwesome
- Africastalking
- coverage
- Docker
## Getting Started

### Prerequisites

- Python 3.x
- Django 4.x
- MySQL
- djangorestframework
- mozilla-django-oidc
- python-dotenv
- mysqlclient
- africastalking
- coverage

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/super_store.git```
2. Install Dependencies
``` pip install -r requirements.txt ```
3. Run the Project
```python manage.py migrate```
```python manage.py runserver```
## Sections
- **Login Page** - user to log in using their google account
  ![image](https://github.com/user-attachments/assets/ffa2d78f-fb69-40f7-9299-643e7f026757)
- **Register Page** - New users can register manualy or using their google accounts
  ![image](https://github.com/user-attachments/assets/e7fc319c-ad56-47b4-93cf-9885705460ac)
- **Home Page**:  Introduction to the project and links to various sections.
  ![image](https://github.com/user-attachments/assets/8d6c1b5f-46ee-4bfe-8b4b-532579a0de28)
- **customers page**: You can add and view customers here
  ![image](https://github.com/user-attachments/assets/97a470ee-f3ea-4547-a237-9f9b688797d3)
- **Orders Page**: You can add and View Orders here
  ![image](https://github.com/user-attachments/assets/d0c05579-a9fa-4494-9107-dac9d161f1da)
## API Endpoints
- GET [api/order](http://127.0.0.1:8000/order/) - List all orders
- POST [api/order](http://127.0.0.1:8000/order/)- Create a new orders
- GET [api/customer](http://127.0.0.1:8000/customer/) - List all customers
- POST [api/customer](http://127.0.0.1:8000/customer/)- Create a new customers
## Contributing
Contributions are welcome! Please open an issue or submit a pull request with any improvements or new features. Here are the Steps
  1. Fork the repository
  2. Create a new branch (git checkout -b feature-name)
  3. Make your changes
  4. Commit your changes (git commit -m 'Add new feature')
  5. Push to the branch (git push origin feature-name)
  6. Open a pull request
## License
This project is licensed under the MIT License.
## Contact
If you have any questions, feel free to reach out:
  - Name: Sarah Mwangi
  - Email: mwangisarah113@gmail.com
  - GitHub: Mwangisara

