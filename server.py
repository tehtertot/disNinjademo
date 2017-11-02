from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    """this is the default page"""
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')

#http://localhost:5000/ninja/purple

@app.route('/ninja/<color>')
def show_colored_ninja(color):
    name = "April"

    if color == "blue":
        name = "Leonardo"
    elif color == "purple":
        name = "Donatello"
    elif color == "orange":
        name = "Michelangelo"
    elif color == "red":
        name = "Raphael"

    return render_template('color.html', ninja=name, color=color, num=34)

app.run(debug=True)
