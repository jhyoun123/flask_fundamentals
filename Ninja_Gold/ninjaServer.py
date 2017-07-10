from flask import Flask, render_template, redirect, request, session
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = 'password'

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
	string = ""
	if 'gold' not in session: 
		session['gold'] = 0
	if 'activities' not in session:
		session['activities'] = []
	if request.form['building'] == 'farm':
		gold = random.randrange(10, 21)
	elif request.form['building'] == 'cave':
		gold = random.randrange(5, 11)
	elif request.form['building'] == 'house':
		gold = random.randrange(2, 6)
	elif request.form['building'] == 'casino':
		gold = random.randrange(-50, 51)

	if gold > 0:
		string = 'Earned ' + str(gold) + ' golds from the ' + str(request.form['building']) + '!'
	else:
		string = 'Entered a casino and lost ' + str(gold) + ' golds... Ouch...'

	time = datetime.now().strftime('%Y/%m/%d %I:%M %p')
	string += ' (' + str(time) + ')'
	session['gold'] += gold
	session['activities'].append(string)
	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session.clear()
	return redirect('/')

app.run(debug=True)