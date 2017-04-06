from flask import Flask, render_template

app=Flask( __name__)

@app.route ("/")

def assignment2_hello():
    return render_template("assignment2.html")
#app.run(debug=True)

@app.route("/part2")

def part2():
    return render_template("part2.html")
#app.run(debug=True)

@app.route("/part3")

def part3():
    return render_template("part3.html")
app.run(debug=True)
