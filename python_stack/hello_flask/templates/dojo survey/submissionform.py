from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Hellotime'

@app.route('/')
def index():
    option_list = ["Antarctica", "California", "Mexico","The Abyss"]
    language_list = ["Ruby", "C#", "Python", ":("]
    return render_template("submission3.html", option_list=option_list, language_list=language_list)

@app.route('/process', methods=['POST'])
def create_user():
    session['names'] = request.form['names']
    session['Location'] = request.form['Location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/process')

@app.route('/process')
def show_user():
    return render_template('submissionresults.html')

app.run(debug=True)
