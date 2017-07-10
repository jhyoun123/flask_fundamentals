from flask import Flask, render_template, session, request, redirect
import random
app = Flask(__name__)
app.secret_key = "password"
@app.route('/')
def home():
	return render_template('index.html')

@app.route('/answer', methods=['POST'])
def answer():
	if 'rand' not in session:
		session['rand'] = random.randrange(1, 101)
        print session['rand']
	guess = int(request.form['guess'])
	if session['rand'] > guess:
		session['guess'] = 'too low'
	elif session['rand'] < guess:
		session['guess'] = 'too high'
	else: 
		session['guess'] = 'correct'
	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session.clear()
	return redirect('/')

app.run(debug=True)