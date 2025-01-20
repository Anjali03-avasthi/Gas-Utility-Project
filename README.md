# Gas Utility Service Request Application

This is a Django-based web application designed to facilitate the management of gas utility service requests. Users can register, log in, submit service requests, and track their progress.

---

## Features

1. **User Authentication:**
   - User registration with fields for name, phone, email, password, and confirm password.
   - Login and logout functionality.

2. **Service Requests:**
   - Submit new service requests.
   - Track the status of submitted requests.

3. **Database Integration:**
   - PostgreSQL database for storing user information and service requests.

4. **Responsive UI:**
   - Built using Bootstrap for a responsive and attractive design.

5. **Security:**
   - Passwords are securely hashed using Django's authentication system.
   - `.env` file used for storing sensitive credentials like database password.

---

## Prerequisites

Ensure you have the following installed:

1. **Python** (>= 3.8)
2. **PostgreSQL** (Latest version)
3. **Git**
4. **django**
---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/gas-utility.git
cd gas-utility
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Database

1. Create a PostgreSQL database.
2. Create a `.env` file in the root directory with the following content:

   ```plaintext
   DATABASE_NAME=your_database_name
   DATABASE_USER=your_database_user
   DATABASE_PASSWORD=your_database_password
   DATABASE_HOST=localhost
   DATABASE_PORT=5432
   ```

3. Update `settings.py` to load credentials from `.env` (already configured).

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000`.

---

## Usage Instructions

1. **Register a New User:**
   - Visit `/register/` to create an account.
2. **Log In:**
   - Navigate to `/login/` and enter your credentials.
3. **Submit Requests:**
   - After logging in, go to `/submit_request/` to submit a new service request.
4. **Track Requests:**
   - View all your service requests and their status at `/track_requests/`.
5. **Log Out:**
   - Click on the "Logout" link in the navbar.

---




## Troubleshooting

1. **Error: NoReverseMatch**
   - Ensure all URLs in `urls.py` have valid names and are used correctly in templates.
2. **Error: Database Connection**
   - Verify credentials in `.env` and ensure the database server is running.
3. **Static Files Not Loading**
   - Run `python manage.py collectstatic` in production.

For further assistance, open an issue on the GitHub repository.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

For any inquiries, please contact:

- **Name:**  Anjali Avasthi
- **Email:** anajaliavasthi@gmail.com

