# User Admin CRUD Project

## Overview

Welcome to the User Admin CRUD project! This project focuses on creating a user sign-up and login system using Django and MySQL database. It also includes an admin login page and separate home pages for both admin and regular users. The project allows the admin to perform CRUD (Create, Read, Update, Delete) operations on user data. The frontend design is implemented using Bootstrap for responsiveness.

## Project Structure

The project repository contains the following files and directories:

1. **my_app**: Contains the Django app, including views, models, and templates for user authentication and CRUD operations.

2. **my_project**: The main Django project directory.

3. **templates**: Contains HTML templates used by the Django app for rendering pages.

4. **README.md**: Project documentation file (You are currently reading this).

5. **db.sqlite3**: SQLite database file (can be changed to MySQL as mentioned).

6. **manage.py**: Django management script.

## Installation

To run the User Admin CRUD project on your local machine, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/your-username/user-admin-crud.git
cd user-admin-crud
```

2. Create and set up the MySQL database:

   - Configure your MySQL database settings in the Django project's `settings.py` file.

   - Run the migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Run the Django development server:

```bash
python manage.py runserver
```

4. Access the project in your web browser at `http://localhost:8000`.

## Features

- User Sign-up and Login: Users can sign up and log in to the application.

- Admin Login: Admins have a separate login page to access the admin dashboard.

- Admin Dashboard: The admin dashboard allows the admin to perform CRUD operations on user data.

- Responsiveness: Bootstrap is used for responsive and mobile-friendly design.

## Usage

1. Navigate to `http://localhost:8000` in your web browser.

2. Sign up with a new user account or log in with existing credentials.

3. Admins can log in using the admin login page to access the admin dashboard.

4. On the admin dashboard, admins can manage user data (add, update, delete, search).

## Contributing

Contributions to this project are welcome! Whether you want to add new features, improve the existing code, or fix bugs, feel free to open issues or submit pull requests. Let's collaborate to make this project even better.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Conclusion

Start managing user data efficiently with the User Admin CRUD project. Implement user sign-up, login, and admin dashboard functionality using Django and MySQL. Enhance your skills in web development and user authentication. Happy coding!

**Project Author: Muhammed Thahseer CK**  
**Self-taught Data Scientist**
