# Import packages
from flask import Flask, render_template

# Custom package
from api import random_dogs

# Initialise app
app = Flask(__name__)

@app.route('/')
def index():
    # Call our custom function to load api data
    data = random_dogs.get_api_data([])

    return render_template("index.html", items=data)

# Run application
if __name__ == "__main__":
    app.run(debug=True, port=5001)