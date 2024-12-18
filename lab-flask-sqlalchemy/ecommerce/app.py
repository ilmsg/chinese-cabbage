from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
db = SQLAlchemy(app)

order_product = db.Table("order_product",
        db.Column("order_id", db.ForeignKey("order.id"), primary_key=True),
        db.Column("product_id", db.ForeignKey("product.id"), primary_key=True)
    )

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    date_joined = db.Column(db.DateTime)
    orders = db.relationship("Order", back_populates="user")
    
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Integer)
    user_id = db.Column(db.ForeignKey("user.id"))
    user = db.relationship("User", back_populates="orders")
    products = db.relationship("Product", secondary=order_product, back_populates="orders")

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    orders = db.relationship("Order", secondary=order_product, back_populate="products")

@app.route("/")
def index():
    return render_template("index.html", page_name="index", page_num=2)

@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html", number=5, data=[{'key': 'value1'},{'key': 'value2'},{'key': 'value3'}])

@app.route("/error")
def error():
    a = 1 / 0
    return "Error"
