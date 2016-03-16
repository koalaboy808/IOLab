from app import myapp,model
from flask import request, render_template, session, redirect, url_for, escape
import os
# from model import InsertDummyRecords

myapp.secret_key = os.urandom(24)

@myapp.route('/')
@myapp.route('/index')
def index():
	username = ''
	if 'username' in session:
		username = escape(session['username'])
		return render_template('survey.html', name=username)
	else:
		return render_template('login.html')

@myapp.route('/login', methods=['GET', 'POST'])
def login():
	if request.method=='POST':
		######## DELETE THIS PART FOR NUM. 3 ###########
		session['username'] = request.form['username']
		session['email'] = request.form['email']
		return redirect(url_for('index'))
		######## DELETE THIS PART FOR NUM. 3 ###########

@myapp.route('/logout')
def logout():
	session.pop('username', None)
	session.pop('email', None)
	return redirect(url_for('index'))

@myapp.route('/submit-survey', methods=['GET', 'POST'])
def submitSurvey():
	# model.InsertDummyRecords()
	# items = model.display()
	# for item in items.find():
	# 	print(item)
	username = ''
	email = ''
	if 'username' in session:
		username = escape(session['username'])
		email = escape(session['email'])

		surveyResponse = {}
		surveyResponse['color'] = request.form.get('color')
		surveyResponse['food'] = request.form.get('food')
		surveyResponse['vacation'] = request.form.get('vacation')
		surveyResponse['fe-before'] = request.form.get('feBefore')
		surveyResponse['fe-after'] = request.form.get('feAfter')

		dropdown = request.form.get('dropdown')
		print(dropdown)
		print(request.form.get('dropdown'))
		textarea = request.form.get('comment')
		print(textarea)
		print(request.form.get('textarea'))

		#insert code here to send surveyresponse into your mongoDB
		model.InsertNameEmail(username,email, surveyResponse, dropdown, textarea)
		items = model.display()
		# for item in items.find():
		# 	print(item)
		febefore_list = []
		feafter_list = []
		for item in items.find({}, { 'surveyResponse': 1, '_id':0} ):
			if item.get('surveyResponse') is not None:
				febefore_list.append(float(item.get('surveyResponse')['fe-before']))
				feafter_list.append(float(item.get('surveyResponse')['fe-after']))
		avg_febefore = sum(febefore_list)/float(len(febefore_list))
		avg_feafter  = sum(feafter_list)/float(len(feafter_list))

		return render_template('results.html', name=username, email=email, surveyResponse=surveyResponse,
			avg_febefore=avg_febefore, avg_feafter=avg_feafter, dropdown=dropdown, textarea=textarea)
	else:
		return render_template('login.html')

@myapp.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404