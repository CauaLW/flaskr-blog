# Flaskr Project

![Flaskr Logo](<path_to_your_logo_or_icon>)

## Introduction

Flaskr is a web application developed using the Flask framework, serving as a learning project following the official Flask tutorial. The project extends beyond the tutorial, incorporating additional functionalities for a more comprehensive understanding of Flask development.

## Features

- **User Authentication**: Implement user registration and login functionalities.
- **Post Management**: Enhance post handling with features like editing and deleting.
- **Blueprints**: Organize your application using Flask blueprints for better modularization.
- **Custom Styling**: Implement custom styling for a more visually appealing user interface.
- **Tests**: Implement testing for the project.

## Getting Started

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/caualw/flaskr-blog.git
   ```

2. Navigate to the project directory:

   ```bash
   cd flaskr-project
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On Unix or MacOS:

     ```bash
     source venv/bin/activate
     ```

5. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

3. Initialize the database:

   ```bash
   flask --app flaskr init-db
   ```

4. Run the application:

   ```bash
   flask --app flaskr run
   ```

   The application will be accessible at `http://localhost:5000/` in your web browser.

### Testing

Run the tests to ensure that everything is working correctly:

```bash
pytest
```

## Project Structure

The project follows the following structure:

```
/flaskr
  /tests
  __init__.py
  config.py
  db.py
  auth.py
  blog.py
  /static
  /templates
  /venv
README.md
requirements.txt
```

## Acknowledgments

- Flask Documentation: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- Official Flask Tutorial: [https://flask.palletsprojects.com/tutorial/](https://flask.palletsprojects.com/tutorial/)