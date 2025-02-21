# AI Writing Companion

A Django-based web application that offers AI-powered writing assistance. This app includes user authentication, profile management, and integration with the OpenAI API for generating content.

## Features

- User registration, login, and profile management
- Integration with OpenAI for generating text
- A clean, responsive user interface
- RESTful API endpoints for additional functionality

## Requirements

- Python 3.11 or higher
- Django 4.2.9 or higher
- Other dependencies listed in `requirements.txt`

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/rashSinha/writing-assistant.git
   cd your-repo-name

2. **Create and activate a virtual environment:**

    ```bash
    Copy
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt

4. **Set up environment variables:**

Create a `.env` file in the project root with the following content (adjust as needed):

    ```bash
    SECRET_KEY=your-secret-key
    DEBUG=True
    DATABASE_URL=sqlite:///db.sqlite3
    OPENAI_API_KEY=your-openai-api-key
    ```

5. **Apply database migrations and create a superuser (optional, for admin access):**

    ```bash
    python manage.py migrate
    python manage.py createsuperuser

## Running the Application

To start the Django development server, run:

    ```bash
    python manage.py runserver
    ```

Then, open your browser and navigate to `http://127.0.0.1:8000/` to see the application in action.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
