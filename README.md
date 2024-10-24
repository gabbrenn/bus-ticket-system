# Online Bus Ticket System

Welcome to the Online Bus Ticket System! This project is a web application built using Django, designed to simplify the process of booking bus tickets online. It features multiple user roles, including Master Admin, Bus Operators, Drivers, and Clients, allowing for comprehensive management of bus routes, schedules, and ticket sales.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [User Roles](#user-roles)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Authentication**: Secure sign-up and login for different user roles.
- **Bus Management**: Add, edit, or remove buses and bus operators.
- **Route Management**: Create and manage routes with schedules.
- **Ticket Booking**: Clients can search for available buses and book tickets online.
- **Admin Dashboard**: Master Admin can oversee all operations, manage users, and generate reports.

## Technologies Used

- **Django**: A high-level Python web framework for building web applications.
- **PostgreSQL**: The database management system used for storing data.
- **HTML/CSS**: For structuring and styling the web application.
- **JavaScript**: For dynamic content and interactivity.
- **Git/GitHub**: For version control and collaboration.

## Installation

To get started with the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/gabbrenn/bus-ticket-system.git
   cd bus-ticket-system

2. **Create a virtual environment**:
   ```bash
   python -m venv myenv

3. **Activate the virtual environment**:
   On Windows:
     ```bash
     myenv\Scripts\activate
   On macOS/Linux:
      ```bash
     source myenv/bin/activate

4. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt

5. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

6. **Start the development server**:
   ```bash
   python manage.py runserver


Now you can access the application at http://127.0.0.1:8000/.

## Usage
Once the application is running, you can register as a user and log in. Depending on your role, you will have access to different functionalities:

- **Master Admin**: Manage users, buses, routes, and view reports.
- **Bus Operators**: Manage your buses and view bookings.
- **Drivers**: View your assigned routes and schedules.
- **Clients**: Search and book tickets for available routes.

## User Roles
- **Master Admin**: Full access to all features, user management, and reporting.
- **Bus Operator**: Manage their own buses and view ticket sales.
- **Driver**: Access to schedules and routes they are assigned to.
- **Client**: Ability to search for buses and purchase tickets.

## Contributing
Contributions are welcome! If you would like to contribute to this project, please follow these steps:

- Fork the repository.
- Create a new branch:
  ```bash
  git checkout -b feature/YourFeature
- Make your changes and commit them:
  ```bash
  git commit -m "Add some feature"
- Push to the branch:
  ```bash
  git push origin feature/YourFeature
Open a pull request.
