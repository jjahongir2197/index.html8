from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def word_count():

    if request.method == "POST":

        text = request.form["text"]
        words = text.split()

        return f"So‘zlar: {len(words)}"

    return render_template("index.html")

app.run(debug=True)
