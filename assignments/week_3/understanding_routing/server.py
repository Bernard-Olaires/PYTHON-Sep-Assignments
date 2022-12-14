from flask import Flask # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello():
    return "Hello!"
@app.route('/dojo')
def dojo():
    return F"Dojo!"

@app.route('/say/<name>')
def say(name):
    return f"Hi {name}"

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num,word):
    output = ''
    for i in range(0,num):
        output += f"<p>{word}</p>"
    return output



if __name__== "__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=8000)    # Run the app in debug mode.

