from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('all.html')

@app.route('/ninja/<color>')
def color(color):
    color = color.lower()
    if (color == "blue"):
        return render_template('image.html', ninja = "/static/images/Leonardo.jpg")
    elif (color == "orange"):
        return render_template('image.html', ninja = "/static/images/Michelangelo.jpg")
    elif (color == "red"):
        return render_template('image.html', ninja = "/static/images/Raphael.jpg")
    elif (color == "purple"):
        return render_template('image.html', ninja = "/static/images/Donatello.jpg")
    else:
        return render_template('image.html', ninja = "/static/images/notapril.jpg")

app.run(debug=True)