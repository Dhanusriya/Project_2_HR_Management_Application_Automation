# HR Management Application Automation Testing

## Project Overview

This project automates the testing of the OrangeHRM application using Selenium WebDriver, Python, and Pytest following the Page Object Model (POM) design pattern.

The objective of this project is to validate the core functionalities of the HR Management System by executing automated test cases for login, user management, leave management, claim management, and employee information modules.

---

## Tech Stack

* Python 3.14
* Selenium WebDriver
* Pytest
* Pytest HTML Reports
* WebDriver Manager
* OpenPyXL
* Chrome Browser
* Page Object Model (POM)

---

## Framework Design

The project follows the Page Object Model (POM) framework design to improve code reusability, maintainability, and readability.

### Features Implemented

* Page Object Model Design Pattern
* Explicit Waits
* Logging
* HTML Reports
* Screenshot Support
* Data-Driven Testing Support
* Exception Handling
* Reusable Utility Methods

---

## Project Structure

Project_2_HR_Management_Application

├── pages/

│   ├── login_page.py

│   ├── dashboard_page.py

│   ├── admin_page.py

│   ├── myinfo_page.py

│   ├── leave_page.py

│   └── claim_page.py

│

├── tests/

│   ├── test_login.py

│   ├── test_invalid_login.py

│   ├── test_logout.py

│   ├── test_dashboard_menu.py

│   ├── test_new_user_creation.py

│   ├── test_search_user.py

│   ├── test_forgot_password.py

│   ├── test_myinfo_menu.py

│   ├── test_assign_leave.py

│   └── test_submit_claim.py

│

├── utilities/

│   ├── waits.py

│   └── logger.py

│

├── test_data/

│

├── reports/

│   └── report.html

│

├── logs/

│   └── automation.log

│

├── screenshots/

│

├── conftest.py

├── pytest.ini

├── requirements.txt

└── README.md

---

## Test Cases Covered

### TC01 - Login Validation

Verify successful login with valid credentials.

### TC02 - Invalid Login Validation

Verify error handling for invalid credentials.

### TC03 - Logout Validation

Verify successful logout from the application.

### TC04 - Dashboard Menu Validation

Verify all dashboard menu items are displayed.

### TC05 - Create New User

Create a new system user through the Admin module.

### TC06 - Search User

Search and validate the newly created user.

### TC07 - Forgot Password Validation

Validate forgot password functionality.

### TC08 - My Info Menu Validation

Verify all My Info submenu items are present.

### TC09 - Assign Leave

Assign leave to an employee and validate assignment.

### TC10 - Submit Claim

Create and validate a claim request.

---

## Prerequisites

Before running the project, ensure the following are installed:

* Python 3.14
* Google Chrome Browser
* PyCharm IDE (Optional)
* Git

---

## Installation

Clone the repository:

git clone <repository-url>

Navigate to project folder:

cd Project_2_HR_Management_Application

Install dependencies:

pip install -r requirements.txt

---

## Test Execution

Run all test cases:

pytest tests/ -v

Run a specific test case:

pytest tests/test_login.py -v

---

## Generate HTML Report

Execute:

pytest tests/ --html=reports/report.html --self-contained-html

Report Location:

reports/report.html

---

## Logging

Execution logs are automatically generated and stored in:

logs/automation.log

Logging captures:

* Test execution status
* Success messages
* Failure messages
* Error details

---

## Exception Handling

All critical test cases include:

* Try-Except blocks
* Logging of failures
* Screenshot capture on failure
* Proper exception re-raising

---

## Browser Supported

* Google Chrome

---

## Author

Name: Dhanusriya Sugananth

Project: HR Management Application Automation Testing

Framework: Selenium + Python + Pytest + POM
