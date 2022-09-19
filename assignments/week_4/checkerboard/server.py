from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def checkerboard():
    return render_template("index.html",row=8,col=8,color_one='red',color_two='black')

@app.route('/<int:num>')
def checkerboard_int(num):
    return render_template("index.html", row=num, col=8, color_one='red', color_two='black')

@app.route('/<int:x>/<int:y>')
def checkerboard_xy(x,y):
    return render_template("index.html", row=x, col=y, color_one='red', color_two='black')

@app.route('/<int:x>/<int:y>/<color>')
def row_col_one(x,y,color):
    return render_template("index.html", row=x, col=y, color_one=color, color_two='black')

@app.route('/<int:x>/<int:y>/<one>/<two>')
def row_col_two(x,y,one,two):
    return render_template("index.html", row=x, col=y, color_one=one, color_two=two)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=8000)    # Run the app in debug mode.

