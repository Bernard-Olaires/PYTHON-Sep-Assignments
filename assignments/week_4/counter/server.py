from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "gang gang counter"


@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += 1
    return render_template("index.html")

@app.route('/add2')
def add2():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += 2
    return render_template("index.html")

@app.route('/custom', methods=['POST'])
def custom_increment():
    
    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=8000)