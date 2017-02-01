from scheduler_flask import db
class ScheduleItem(db.Model):

	# Table name
	__tablename__ = 'scheduleitems'

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


	# def set_item_name(self, name, description, date_due):
	# 	self.name = name
	# 	self.description = description
	# 	if date_due != None: # Check if user entered a due date
	# 		self.date_due = date_due
	#
	# # Return text name
	# def get_name(self):
	# 	return self.name

	# Return boolean complete
	def get_complete(self):
		return self.complete

	# Returns text description
	def get_description(self):
		return self.description

	# Returns datetime due date
	def get_due_date(self):
		return self.date_due

	# Checks if the due date is past due
	def is_past_due(self):
		if self.date_due < datetime.date.today():
			return "This is past due!"
		else:
			days_left = self.date_due - datetime.date.today()
			return "You have " + str(days_left) + " days left"

	def read_db_item(self, id, name, complete, description, date_due):
		self.id = id
		self.name = name
		self.complete = complete
		self.description
		self.date_due = date_due

	def __repr__(self): # Returns string representation of this item
		return "ID: {}; Name: {}; IsComplete: {}; Description: {}; DueDate: {}".format(self.id, self.name, self.complete, self.description, self.date_due)
