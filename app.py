# app.py
from flask import Flask, render_template, request
from rock_paper_scissors import play_rps

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def game():
    result = None
    if request.method == "POST":
        user_choice = request.form["choice"]
        result = play_rps(user_choice)
    return render_template("game.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
