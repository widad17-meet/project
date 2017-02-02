from database_setup import *

from flask import Flask ,render_template, redirect

app = Flask(__name__)


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

@app.route('/logout')
def logout():
	session.pop('user_id', None)
	return redirect(url_for('mainpage'))

@app.route('/SignIn', methods=['GET', 'POST'])
def SignIn():
	if (request.method == 'POST'):
		email = request.form['email']
		password = request.form['password']
		user = dbsession.query(Person).filter_by(email = email).first()
		if user == None or user.password != password:
			return render_template('sign_in.html', error = True)
		else:
			session['person_id'] = person.id
			return render_template('mainpage.html')
	else :
		return render_template('sign_in.html')

if __name__ == "__main__":
	app.run(debug=True)