import firebase_admin
from firebase_admin import db

from flask import render_template, request, session
from flask import redirect, jsonify, redirect
from app import app

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/page1')
def page1():
	return render_template('page1.html')