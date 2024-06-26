# Importing the Flask class from flask module
from flask import Flask, render_template

# Let's see the content of the flask module
# print(dir(flask))
 
# Let's create the object of the Flask class
app = Flask(__name__)

#This gives the name of the file
# __name__: Tell from which file we are running the code
# Return __main__ if we run the code from the same file otherwise return the file name
# print(__name__)

# First route: Index route/default route
@app.route('/')
# How server response to the request on '/'
def index():
    # Returning the response
    return render_template('index.html')

# Second route: Contact Us
@app.route('/contact')
# How server response to the request on 'contact'
def contact():
    # Returning the response
    return render_template('contact.html')

# Third route: About Us
@app.route('/about')
# How server response to the request on 'about'
def about():
    # Returning the response
    return render_template('about.html')

# Let's run the flask application
app.run(debug=True)
# debug=True: We don't have to reload our server again and again
# host='0.0.0.0': The server application is available for all devices in the same network
# app.run(debug=True, host='0.0.0.0')
