import time
from flask import Flask, send_file, render_template, send_from_directory, request
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)


@app.route('/')
def upload_form():
    return render_template('ui.html')

@app.route("/url", methods =["GET", "POST"])
def add_url():
    if request.method == "POST":
        # if "test.txt" not in os.listdir():
        response = requests.get(request.form.get("title"))
        content = response.text
        soup = BeautifulSoup(content, "html.parser")


        with open("test.txt", mode="w", encoding="utf-8") as file:
            file.write(str(soup))

    return render_template("url.html")


@app.route('/ui', methods =["GET", "POST"])
def download_file():
        time.sleep(5)
        path = "test.txt"
        return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)

