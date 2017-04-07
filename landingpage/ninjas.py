from flask import Flask, render_template

app=Flask( __name__)

@app.route ("/")
def ninjas():
    return render_template("ninja_start.html")

@app.route("/form")
def form():
    return render_template("ninjaform.html")

@app.route("/main")
def main():
    return render_template("ninjas.html")

app.run(debug=True)
