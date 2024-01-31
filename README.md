# ReqRes API Testing Project

## Overview
This project is focused on testing the ReqRes API, which provides endpoints for user-related operations. The goal is to practice and demonstrate skills in testing CRUD (Create, Read, Update, Delete) operations using various test scenarios.

## Table of Contents
- [Introduction](#introduction)
- [Endpoints](#endpoints)
- [Testing Scenarios](#testing-scenarios)
- [Setup](#setup)
- [Running the Tests](#running-the-tests)
- [Test Results](#test-results)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The ReqRes API is a public API that allows developers to test and prototype their applications by providing endpoints for user-related actions. This project focuses on creating automated tests for CRUD operations using this API.

## Endpoints
The following endpoints are utilized in this project:

- **Create User:** `POST /api/users`
- **Read User:** `GET /api/users/{user_id}`
- **Update User:** `PUT /api/users/{user_id}`
- **Delete User:** `DELETE /api/users/{user_id}`

For more details on the ReqRes API, refer to the [official documentation](https://reqres.in/).

## Testing Scenarios
The project covers various testing scenarios for each CRUD operation, including positive and negative cases. The test scenarios include data validation, response code verification, and more.

## Setup
To set up the project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/reqres-api-testing.git`
2. Install the necessary dependencies: `pip install -r requirements.txt`

## Running the Tests
Execute the automated tests using your preferred test runner. For example:

```bash
python test_crud_operations.py
