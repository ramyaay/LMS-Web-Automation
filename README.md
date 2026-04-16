# LMS Web Automation

## Project Overview

This project focuses on automating the testing of a Learning Management System (LMS) web application.
It is developed using Python, Selenium WebDriver, and pytest to validate core LMS functionalities such as course management, user interactions, and workflow processes.

A Learning Management System (LMS) is a software platform used to create, manage, deliver, and track educational or training content in a centralized system. ([eLeaP®][1])

The automation framework follows the Page Object Model (POM) design pattern to ensure better code organization, reusability, and maintainability.

---

## Tech Stack

* **Programming Language:** Python
* **Automation Tool:** Selenium WebDriver
* **Testing Framework:** Pytest
* **Design Pattern:** Page Object Model (POM)
* **Reporting:** Allure Reports (if configured)

---

## Project Structure

LMS-Web-Automation/

├── tests/              # Test cases for LMS functionalities
├── pages/              # Page Object classes for UI interactions
├── utils/              # Utility/helper functions
├── config/             # Configuration files
├── requirements.txt    # Project dependencies
├── pytest.ini          # Pytest configuration
├── reports/            # Test execution reports
└── allure-report/      # Allure generated reports

---

## Key Features

* Automation of LMS web application workflows
* Validation of course management and user functionalities
* Page Object Model (POM) implementation
* Reusable and scalable automation framework
* Pytest-based execution and assertions
* Support for detailed test reporting

---

## How to Execute Tests

### 1. Install Dependencies

pip install -r requirements.txt

### 2. Run Test Cases

pytest

### 3. Generate Allure Report (Optional)

pytest --alluredir=reports
allure serve reports

---

## Reporting

The framework supports Allure reporting for better visualization of test execution results.
Reports include detailed insights into passed, failed, and skipped test cases.

---

## Author

**Ramya**


