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
