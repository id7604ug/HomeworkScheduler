# Create db
from database import db

from schedule_item import ScheduleItem

db.create_all()
db.session.commit()
