from flask import Flask, render_template


app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Hello World"

@app.route("/")
def index():
    return render_template("index.html",name="Bernard")

if __name__ == "__main__":
    # need to add port=8000 FOR MAC USERS
    app.run(debug=True, port=8000)
