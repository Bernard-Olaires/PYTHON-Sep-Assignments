# DO NOT FORGET TO : pipenv install flask
# AND:  pipenv shell (to get enviroment going)

from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response








# this should always be at the bottom
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=8000)    # Run the app in debug mode, port= 8000 for MAC users cause port 5000 is being taken up by cloud

