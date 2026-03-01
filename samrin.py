from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    
    ans1 = request.form.get("q1")
    ans2 = request.form.get("q2")
    ans3 = request.form.get("q3")

    if ans1.lower() == "yes":
        score += 1

    if ans2.lower() == "antonio guterres":
        score += 1

    if ans3.lower() == "ktm":
        score += 1

    return f"<h1>Your Total Score is {score}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
