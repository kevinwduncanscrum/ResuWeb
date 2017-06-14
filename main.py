from flask import Flask, render_template
app = Flask(__name__)


@app.route("/Kev_ResuWebb/<name>")
def profile(name):
    return render_template("Kev_ResuWebb.html", name=name)


if __name__ == "__main__":
    app.run()