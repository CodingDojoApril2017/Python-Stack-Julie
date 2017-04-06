from flask import Flask, render_template

app=Flask( __name__)

@app.route ("/")

def assignment1_hello():
    return render_template("assignment1.html")
app.run(debug=True)
