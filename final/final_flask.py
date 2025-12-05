#AE FINAL: Staycation Project

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route ("/")
def home():
    return render_template("final.html")

@app.route ("/activities")
def activities():
    return render_template("activities.html")

@app.route ("/lessons")
def lessons():
    return render_template("ski_lessons.html")

if __name__ == "__main__":
    app.run(debug=True)