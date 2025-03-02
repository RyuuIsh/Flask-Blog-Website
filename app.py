import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    URL = "https://api.npoint.io/ff92afaab9a74c6246f9"
    response = requests.get(URL)
    data = response.json()
    return render_template("index.html", data=data)

@app.route('/post/<int:get_id>')
def post(get_id):
    URL = "https://api.npoint.io/ff92afaab9a74c6246f9"
    response = requests.get(URL)
    data = response.json()
    show_data = [post for post in data if post["id"] == get_id]
    return render_template("post.html", show_data=show_data)

if __name__ == "__main__":
    app.run(debug=True)
