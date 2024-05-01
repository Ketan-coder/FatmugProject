# Vendor Management System

This is a Django project gives you APIs for Vendor Management System.

## Getting Started

To run the project locally, follow these steps:

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/ketan-coder/Vendorms.git
   ```

2. Navigate to the project directory:

   ```
   cd Vendorms
   ```

3. Create a virtual environment and activate it:

   ```
   python -m virtualenv env
   # On Linux/Mac:
        source env/bin/activate   
   # On Windows: 
        venv\Scripts\activate
   ```

4. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

5. Set up the database (if required) and perform migrations:

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser (if needed) to access the Django admin (there is one created by me in [creationals.txt](creationals.txt)):

   ```
   python manage.py createsuperuser
   ```
7. Generate the Secret Key before running and keep it in FatmugSK.txt file:

   ```
   # Generate the Secret key using this command for quick start
   python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

   Also change the path of the secret key in `settings.py` in line 24. Give it Absolute path like 'D:\Documents\Django\FatmugSK.txt'

8. Start the development server:

   ```
   python manage.py runserver 127.0.0.1:5050
   ```

   The development server will start at http://localhost:5050/.

## Usage

- Access the Django admin at http://localhost:8000/admin/ to manage your project.
- Explore the API endpoints at http://localhost:8000/api/vendors/ or other urls.
- You can also test the status of the web api with the [WebsiteTester.py](WebsiteTester.py) script.

## Notes

- Customize the settings in `settings.py` for your specific requirements.
- Some elements may be not in order espicially in settings.py and static or template folder is been created with no work that's because of I am using [DjangoAutomation](https://github.com/Ketan-coder/Django_automation) which is made by me which does the initialization for me.
- Ensure proper security measures are implemented before deploying to production and please refer to the [Django documentation](https://docs.djangoproject.com/en/4.1/topics/security/) for more information.
