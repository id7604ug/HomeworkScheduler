# Create db by running this script
from database import db

# Import all class modules used
from schedule_item import ScheduleItem

# Create each table the class modules use
db.create_all()
# Commit changes to the db
db.session.commit()
