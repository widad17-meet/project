from database_setup import *

from flask import Flask, url_for, flash, redirect, request
from flask import session as login_session

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()

@app.route('/')
def mainPage():
	allSessions = session.query(Session).all()
	return render_template('main.html', allSessions = allSessions)


@app.route('/signup', methods = ['GET','POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        gender = request.form['gender']
        if name == “” or email == “” or password == “”:
            flash("Your form is missing arguments")
            return redirect(url_for('signup'))
        if session.query(Person).filter_by(email = email).first() is not None:
            flash("A user with this email address already exists")
            return redirect(url_for('newCustomer'))
        user = Person(name = name, email=email, gender = gender)
        Person.hash_password(password)
        session.add(user)
        session.commit()
        flash("User Created Successfully!")
        return redirect(url_for('mainpage'))
    else:
        return render_template('signup.html')



def verify_passsword(email,password):
    person= session.query(Person).filter_by(email=email).first()
    if not person or not person.verify_passsword(password):
        return False
    return True

@app.route('/SignIn', methods=['GET', 'POST'])
def SignIn():
	if request.method == 'GET':
        return render_template('singnin.html')
    elif request.method== 'POST':
		email = request.form['email']
		password = request.form['password']
        if email == “” or password == “”:
            flash('missing arguments')
            return redirect(url_for('login'))
        if verify_passsword(email,password):
            person= session.query(Person).filter_by(email=email).one()
            flash('login successful, welcome %s'%person.name)
            login_session['name']= person.name
            login_session['email']= person.email
            login_session['id']= person.id
            return redirect(url_for('mainpage'))
        else:
            flash('Incorrect username/password combination')
            return redirect(url_for('login'))

@app.route("/intructor/<int:instructor_id>")
def intructor(intructor_id):
    instructor= session.query(instructor).filter_by(id=instructor_id).one()
    return render_template('instructor.html', instructor=instructor)
 `


if __name__ == "__main__":
	app.run(debug=True)