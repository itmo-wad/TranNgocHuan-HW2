# Authentication Feature Implementation for Web Application

This project implements an authentication feature for a web application, storing user data in a database MongoDB.

## Features

### Basic Authentication

- **Listen on localhost:5000:** The application listens on `localhost:5000`(or the address shown in terminal).
- **Authentication Form:** An authentication form is rendered at `http://localhost:5000/`.
  ![Alt text](static/images/authentication_form.jpg)

- **Redirection:** Upon successful authentication, the user is redirected to profile page at `http://localhost:5000/profile`.
  ![Alt text](static/images/profile_page.jpg)

- **Data Storage:** Usernames and passwords are stored in MongoDB.
  ![Alt text](static/images/Database.jpg)

### Advanced Features (Optional)

- **User Registration:** Users can create new accounts. Profile data is specific to each account.
  ![Alt text](static/images/Register.jpg)

- **Form Registration:** User enters information to register
  ![Alt text](static/images/Registration.jpg)

Profile will be shown with data respected to each account:
![Alt text](static/images/profile_page_2.jpg)

- **Password hashing**: Passwords will be hashed before being saved to the database.
  ![Alt text](static/images/Hash_password.jpg)

- **Logout**: When logging out, the page will be redirected to the login confirmation page.
  ![Alt text](static/images/Function_logout.jpg)

## Technologies Used

- Python (Programming Language)
- Flask (Web Framework)
- MongoDB(Database)
- bcrypt (Password Hashing)
- HTML, CSS, JavaScript (Frontend)

## How to Run

1.  **Clone the Repository:**

    ```bash
    git clone [repository URL]
    ```

2.  **Navigate to the Project Directory:**

    ```bash
    cd [project directory name]
    ```

3.  **Install Dependencies:**

    ```bash
    pip install Flask pymongo bcrypt
    ```

4.  **Database Setup:**
    **MongoDB:** Ensure MongoDB is running and configure the connection URI in Python code.

5.  **Run the Application:**
    ```bash
    py app.py
    ```
6.  **Access the application:**
    Open your web browser and navigate to http://localhost:5000 (or the address shown in terminal).
