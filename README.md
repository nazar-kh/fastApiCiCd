# FastAPI Application

Welcome to the FastAPI Application! This project is a Python-based web application using the FastAPI framework, designed for high-performance and easy-to-build web APIs.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

## Features

- **High Performance**: FastAPI is one of the fastest Python frameworks available.
- **Easy to Use**: Designed to be easy to use and learn, with minimal boilerplate code.
- **Automatic Documentation**: Provides automatic interactive API documentation with Swagger UI and ReDoc.
- **Dependency Injection**: Built-in dependency injection system for managing dependencies.
- **Asynchronous Support**: Full support for asynchronous programming with `async` and `await`.

## Installation

To install the application, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/nazar-kh/fastApiCiCd.git
    cd fastApiCiCd
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To use this application, follow these steps:

1. Start the application:
    ```sh
    uvicorn main:app --reload
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000`.

## Configuration

Configuration settings for the application are stored in the `config.py` file. Adjust these settings as necessary for your environment.

## Running the Application

To run the application locally, use the following command:
```sh
uvicorn main:app --reload
