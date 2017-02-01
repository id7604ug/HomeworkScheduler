# Quickstart guide:
# http://flask.pocoo.org/docs/0.12/quickstart/

from flask import Flask
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
from schedule_item import ScheduleItem

# Set root URL to execute this function
@app.route('/')
def index():
    return render_template('index.html')

# Set URL for the Add assignment page
@app.route('/add_assignment')
def add_assignment():
    return render_template('new_assignment.html')

# Set URL for viewing all assignments
@app.route('/view_all_assignments')
def view_all_assignments():
    assignment_list = ScheduleItem.query.all()
    # print(assignment_list)
    return render_template('view_all_assignments.html', assignment_list=assignment_list)

@app.route('/delete_assignment')
def delete_assignment_page():
    return render_template('delete_assignment.html')

@app.route('/delete_item', methods=['POST'])
def delete_item():
    item_id = request.form['id_to_delete']
    if item_id == None:
        print("Not deleting anything")
        return render_template('delete_assignment.html')
    schedule_item = ScheduleItem.query.get(item_id)
    if schedule_item:
        db.session.delete(schedule_item)
        db.session.commit()
        print("Item with id: " + item_id + " has beed deleted.")
        return render_template('delete_assignment.html')
    else:
        print("Error deleting schedule item")
        return render_template('error')

@app.route('/check_due_assignments')
def check_due_assignments():
    return render_template('check_due_assignments.html')

# Handle adding a schedule item
@app.route('/submit_item', methods=['POST'])
def add_schedule_route():
    schedule_item = [request.form['class'], request.form['name'], request.form['is_complete'], request.form['description'], request.form['due_date']]
    if verify_schedule_data(schedule_item):
        print("valid data")
        print(request.form)
        item = ScheduleItem(schedule_item[0], schedule_item[1], schedule_item[2] == "True", schedule_item[3], schedule_item[4])
        db.session.add(item)
        db.session.commit()
    else:
        print("invalid data")
    return render_template('new_assignment.html')

@app.route('/update_item', methods=['POST'])
def update_schedule_item():
    request_id = request.form.get('item_id')
    if int(request_id) > 0:
        complete = False
        if request.form.get('complete'):
            complete = True
        # Update
        # http://docs.sqlalchemy.org/en/latest/orm/query.html
        db.session.query(ScheduleItem).filter_by(id=request_id).update({ScheduleItem.class_name: request.form.get('class_name'), ScheduleItem.name: request.form.get('name'), ScheduleItem.complete: complete, ScheduleItem.description: request.form.get('description'), ScheduleItem.date_due: request.form.get('due_date')}, synchronize_session=False)
        # item.
        # item.name =

        # item.description =
        # item.schedule =
        # db.session.add(item)
        db.session.commit()
        return render_template('view_all_assignments.html')
    else:
        return render_template('error')


# @app.teardown_request
# def shutdown_session(exception=None):
#     db.remove()

def verify_schedule_data(schedule_item):
    try:
        str(schedule_item[0])
        str(schedule_item[1])
        bool(schedule_item[2])
        str(schedule_item[3])
        date = schedule_item[4].split('-')
        if len(date[0]) == 4 and len(date[1]) == 2 and len(date[2]) == 2:
            return True
        else:
            return False
    except ValueError:
        print("Invalid input was recieved")

# TO RUN (Commands): ----------
# export FLASK_APP='appname'
# OR on windows
# set FLASK_APP='appname'
# flask run
