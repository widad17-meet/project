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


@app.route('/newCustomer', methods = ['GET','POST'])
def newCustomer():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        address = request.form['address']
        if name == “” or email == “” or password == “”:
            flash("Your form is missing arguments")
            return redirect(url_for('newCustomer'))
        if session.query(Customer).filter_by(email = email).first() is not None:
            flash("A user with this email address already exists")
            return redirect(url_for('newCustomer'))
        customer = Customer(name = name, email=email, address = address)
        customer.hash_password(password)
        session.add(customer)
        shoppingCart = ShoppingCart(customer=customer)
        session.add(shoppingCart)
        session.commit()
        flash("User Created Successfully!")
        return redirect(url_for('inventory'))
    else:
        return render_template('newCustomer.html')



if __name__ == "__main__":
	app.run(debug=True)