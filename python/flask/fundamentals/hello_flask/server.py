from flask import Flask, render_template # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html')


@app.route('/success')
def success():
    return "Success"


@app.route('/hello/<string:banana>/<int:num>') #<banana> can be anything
def hello(banana, num): # you have to bring in banana in your method
    return render_template("hello.html", banana=banana, num=num)









if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=8000)    # Run the app in debug mode. SHOULD ALWAYS BE AT THE BOTTOM OF server.py

