from flask import Flask, render_template # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/play')          # The "@" decorator associates this route with the function immediately following
def level_1():
    return render_template("index.html", num=3, color="blue")

@app.route('/play/<int:num>')
def level_2(num):
    return render_template("index.html", num=num, color="blue")

@app.route('/play/<int:num>/<color>')
def level_3(num,color):
    return render_template("index.html", num=num, color=color)


if __name__ == "__main__":
    # need to add port=8000 FOR MAC USERS
    app.run(debug=True, port=8000)


