from flask import Blueprint, json, render_template, jsonify

views = Blueprint('views', __name__)

@views.route('/')
def index():
	return render_template('index.html')

@views.route('/show')
def show():
	return jsonify({'msg': 'Hello from flask api'})