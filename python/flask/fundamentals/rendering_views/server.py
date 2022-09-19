from flask import Flask, render_template  # Import Flask to allow us to create our app, 
# render_template = to access our html files 

app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def template_example():
    return render_template("index.html") # used render_template and then called the html file name






if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

