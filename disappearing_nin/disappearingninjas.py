from flask import Flask, render_template, request, session, flash, redirect
app = Flask(__name__)
app.secret_key = "secretninjas"

@app.route ("/")
def nonninja():
    return render_template("disappearingninja.html")

@app.route("/appear")
def appear():
    return render_template("appear.html", color="default")

@app.route("/appear/<color>")
def route_appear(color):
    print color
    return render_template("appear.html", color=color)

app.run(debug=True)
