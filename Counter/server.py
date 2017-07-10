from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "ThisIsSecret"


@app.route('/')
def index():
    session['counter'] += 1
    return render_template('index.html')

@app.route('/two', methods=['POST'])
def addTwo():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['counter'] = 1
    return render_template('index.html')

app.run(debug=True)