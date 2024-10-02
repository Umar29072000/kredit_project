# Credit Project

This project is a web application built with Django to calculate and manage credit. The application allows users to input credit data and receive immediate calculations.

## Features

- **Credit Calculation:** Calculates monthly payments based on loan amount, interest rate, and term.
- **SQLite Database:** Stores loan data for future reference or analysis.
- **Credit Application Form:** Uses a form to receive user input with proper validation.

## Installation

Make sure you have Python and pip installed on your system. To set up this project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <REPOSITORY_URL>
   ```

2. **Navigate to the project directory:**
   ```bash
   cd kredit_project-main
   ```

3. **Create a virtual environment:**
   ```bash
   python -m venv env
   ```

4. **Activate the virtual environment:**
   ```bash
   env\Scripts\activate
   ```

5. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Migrate the database:**
   ```bash
   python manage.py migrate
   ```

7. **Run the server:**
   ```bash
   python manage.py runserver
   ```
