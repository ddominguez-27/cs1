"""
Flask
Author: Daniel Dominguez
Date: 5/29/26
Sources: Form made with AI, Flask code orginially from google classroom, 
Description:  Python file which runs using Flask allowing html form from templates folder to run on this computer
Log: 1.0
"""

from flask import Flask, render_template, request  # imports the necesary 
import csv


app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/')   # URL '/' to be handled by main() route handler
def main():

    
    return render_template("template1.html")  # Return this html  as a response to the client

@app.route('/submit', methods=["GET"])
def submit():
    q1 = request.args.get("q1")         #reads the answer for all 4 questions and assigns them to variables q1-4
    q2 = request.args.get("q2")
    q3 = request.args.get("q3")
    q4 = request.args.get("q4")

    with open("responses.csv", mode="a", newline="") as file:       #writes to the responses csv using append mode, so the file can accumulate data
        writer = csv.writer(file)

        writer.writerow([q1, q2, q3, q4])        # write one row using the variables of all 4 question inputs



    return "Responses submitted!"     #updates the page to confirm submission of response




if __name__ == '__main__':  # Script executed directly?
    app.run(host="0.0.0.0", port=5000, debug=True)     #