from flask import Blueprint, request, render_template, jsonify
from app.models import Product, ProductSchema
from app import db

views = Blueprint('views', __name__)

prod_schema = ProductSchema()
prod_schemas = ProductSchema(many=True)

@views.route('/')
def index():
	return render_template('index.html')

@views.route('/show')
def show():
	return jsonify({'msg': 'Hello from flask api'})

@views.route('/products')
def all_products():
	items = Product.query.all()
	result = prod_schemas.dump(items)

	return jsonify(result)

@views.route('/products/<id>')
def one_product(id):
	item = Product.query.get(id)
	return prod_schema.jsonify(item)

@views.route('/add', methods=['GET', 'POST'])
def add_product():
	name = request.json['name']
	description = request.json['description']
	price = request.json['price']
	qty = request.json['qty']

	new_prod = Product(name=name, description=description, price=price, qty=qty)
	db.session.add(new_prod)
	db.session.commit()

	return prod_schema.jsonify(new_prod)

@views.route('/products/<id>/update', methods=['GET', 'PUT'])
def update_product(id):
	item = Product.query.get(id)
	
	name = request.json['name']
	description = request.json['description']
	price = request.json['price']
	qty = request.json['qty']

	item.name = name
	item.description = description
	item.price = price
	item.qty = qty

	db.session.commit()

	return prod_schema.jsonify(item)

@views.route('/products/<id>/delete', methods=['GET', 'DELETE'])
def delete_product(id):
	item = Product.query.get(id)

	db.session.delete(item)
	db.session.commit()

	return prod_schema.jsonify(item)
