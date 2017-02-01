# HomeworkScheduler

# Summary:
This program tracks homework/assignments and tracks the date they are due

# Features:
  - Ability to add homework/assignments
  - Update assignments
  - Delete assignments

# Setup
  - Required libraries include:
    - Flask
    - flask_sqlalchemy
    - SQLAlchemy
  - If database does not exist run the create_db.py file
  - Flask environment setup:
    (PC)
    - set FLASK_APP=scheduler_flask.py
    - set FLASK_DEBUG=1
    (Mac)
    - export FLASK_APP=app.py
    - export FLASK_DEBUG=1
    - To run the app use: flask run
