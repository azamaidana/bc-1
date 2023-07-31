from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost/clients"
db.init_app(app)


class ClientOrder(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    contact = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)



class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    order_count = db.Column(db.Integer)




class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=True)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)





@app.route('/')
def home_order():
    orders = db.session.execute(db.select(ClientOrder)).scalars()
    clients = db.session.execute(db.select(Client)).scalars()
    cars = db.session.execute(db.select(Car)).scalars()
    return render_template('index.html',
    orders=orders,
    clients=clients,
    cars=cars
                           )


@app.route('/order/<int:id>')
def shop_info(id):
    shop_object = db.get_or_404(ClientOrder, id)
    return render_template('order1.html', order_info=shop_object)

@app.route('/orders')
def orders_list():
    order_query = db.session.execute(db.select(ClientOrder)).scalars()
    return render_template('order2.html', orders=order_query)


@app.route('/car/<int:id>')
def car_info(id):
    car_object = db.get_or_404(Car, id)
    return render_template('cars1.html', car_info=car_object)

@app.route('/cars')
def cars_list():
    cars_query = db.session.execute(db.select(Car)).scalars()
    return render_template('cars2.html', cars=cars_query)

@app.route('/clients')
def client_list():
    clients_query = db.session.execute(db.select(Client)).scalars()
    return render_template('clients2.html', clients=clients_query)

@app.route('/client/<int:id>')
def client_info(id):
    client_object = db.get_or_404(Client, id)
    return render_template('clients1.html', client_info=client_object)


with app.app_context():
     db.create_all()




