from flask import render_template, request, session
from flask import redirect, jsonfiy, redirect
from app import app
import random

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/get_events')
def get_events():
	return jsonify(events=test_events)