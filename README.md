How to Run

1. Open terminal and navigate to the project folder:
   cd path/to/your/project

2. Create a virtual environment (if you don’t have one):
   Windows: python -m venv venv
   Mac/Linux: python3 -m venv venv

3. Activate the virtual environment:
   Windows: venv\Scripts\activate
   Mac/Linux: source venv/bin/activate

4. Install required packages:
   pip install -r requirements.txt

5. Apply database migrations:
   python manage.py makemigrations
   python manage.py migrate

6. Run the development server:
   python manage.py runserver

7. Open your web browser and go to:
   http://127.0.0.1:8000/
