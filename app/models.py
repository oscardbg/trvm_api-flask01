from app import mars
from app import db

class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(150), unique=True)
	description = db.Column(db.String(250))
	price = db.Column(db.Float)
	qty = db.Column(db.Integer)

	def __str__(self):
		return self.name
	
class ProductSchema(mars.Schema):
	class Meta:
		fields = ('id', 'name', 'description', 'price', 'qty')
