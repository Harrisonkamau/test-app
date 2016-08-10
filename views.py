from flask import Flask, render_template
# create a constructor
app = Flask(__name__)


# create a home route
@app.route('/')
def index():
    return render_template('index.html')
# start the server
if __name__ == "__main__":
    app.run(debug=True)
