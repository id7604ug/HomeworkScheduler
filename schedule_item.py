from scheduler_flask import db
# Class to create schedule objects
class ScheduleItem(db.Model):

	# Table name
	__tablename__ = 'scheduleitems'

	# Variables/columns
	id = db.Column(db.Integer, primary_key=True)
	class_name = db.Column(db.String)
	name = db.Column(db.String)
	complete = db.Column(db.Boolean)
	description = db.Column(db.String)
	date_due = db.Column(db.String)

	# Initializer
	def __init__(self, class_name, name, complete, description, date_due=None):
		self.class_name = class_name
		self.name = name
		self.complete = complete
		self.description = description
		# Handles a default due date
		# The defualt due date is 1 week
		if date_due == None:
			date_due = datetime.date.today() + datetime.timedelta(days=7)
		self.date_due = date_due

	# Method to set db item properties NOT USED
	def read_db_item(self, id, name, complete, description, date_due):
		self.id = id
		self.name = name
		self.complete = complete
		self.description
		self.date_due = date_due

	def __repr__(self): # Returns string representation of this item
		return "ID: {}; Name: {}; IsComplete: {}; Description: {}; DueDate: {}".format(self.id, self.name, self.complete, self.description, self.date_due)
