from flask import Flask, url_for, flash, redirect, request, render_template
from flask import session as login_session
from database_setup import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()

@app.route('/')
def mainpage():
	allSessions = session.query(Session).all()
	return render_template('mainpage.html', allSessions = allSessions)

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/signup', methods = ['GET','POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        gender = request.form['gender']
        if name == "" or email == "" or password == "":
            flash("Your form is missing arguments")
            return redirect(url_for('signup'))
        if session.query(Person).filter_by(email = email).first() is not None:
            flash("A user with this email address already exists")
            return redirect(url_for('signup'))
        user = Person(name = name, email=email, gender = gender)
        user.hash_password(password)
        session.add(user)
        session.commit()
        flash("User Created Successfully!")
        return redirect(url_for('instructors'))
    else:
        return render_template('signup.html')



def verify_password(email,password):
    person= session.query(Person).filter_by(email=email).first()
    if not person or not person.verify_password(password):
        return False
    return True

@app.route('/SignIn', methods=['GET', 'POST'])
def SignIn():
	if request.method == 'GET':
		return render_template('login.html')
	elif request.method== 'POST':
		email = request.form['email']
		password = request.form['password']
		if email == "" or password == "":
			flash('missing arguments')
			return redirect(url_for('SignIn'))
		user=session.query(Person).filter_by(email=email).first()
        if user is None:
            flash("You are not registered.")
            return redirect(url_for('signup'))
        elif verify_password(email, password):
            person= session.query(Person).filter_by(email=email).one()
            flash('login successful, welcome %s'%person.name)
            login_session['id'] = person.id
            login_session['name']= person.name
            login_session['email']= person.email
            return redirect(url_for('instructors'))
        else:
			flash('Incorrect username/password combination')
			return redirect(url_for('instructors'))

@app.route('/instructors')
def instructors():
    inst=session.query(Instructors).all()
    print(inst)
    return render_template("instructors.html", inst=inst)

@app.route("/instructor/<int:instructors_id>")
def instructor(instructors_id):
    instructor= session.query(Instructors).filter_by(id=instructors_id).first()
    lessons=session.query(Session).filter_by(intructor_id=instructors_id).all()
    return render_template('instructor.html', instructor=instructor, lessons=lessons)
 
@app.route('/logout')
def logout():
    if login_session is None:
        flash("You must be logged in order to log out")
        return redirect(url_for('SignIn'))
    del login_session['name']
    del login_session['email']
    del login_session['id']
    flash("Logged Out Seccessfully")
    return redirect(url_for('SignIn'))

@app.route('/book/<int:session1>', methods=['POST', 'GET'])
def booklesson(session1):
    if login_session is None:
        flash("You must be logged in order to book a lesson")
        return redirect(url_for('SignIn'))
    else:
        lesson= session.query(Session).filter_by(id=session1).first()
        if lesson.person_id is not None :
            flash("The lesson is already booked!")
            return redirect(url_for('instructors'))
        else:
            if 'id' in  login_session:
                lesson.person_id = login_session['id']
                session.commit()
                return redirect(url_for('instructors'))
                flash("lesson booked successfully!")
            else:
                flash("You must be logged in order to book a lesson")
                return redirect(url_for("SignIn"))



if __name__ == "__main__":
	app.run(debug=True)