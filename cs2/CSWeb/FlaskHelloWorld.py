
from flask import Flask, render_template, request  # From module flask import class Flask
import csv


app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/')   # URL '/' to be handled by main() route handler
def main():
    #print(app.url_map)
    #print('line 17')            # Print statements go to your console
    
    #return render_template("index.html")
    return render_template("template1.html")  # Return this html  as a response to the client

@app.route('/submit', methods=["GET"])
def submit():
    q1 = request.args.get("q1")
    q2 = request.args.get("q2")
    q3 = request.args.get("q3")
    q4 = request.args.get("q4")

    return f"{q1}, {q2}, {q3}, {q4}"



if __name__ == '__main__':  # Script executed directly?
    app.run(host="0.0.0.0", port=5000, debug=True)