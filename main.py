import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

api_key = os.getenv("API_KEY")
url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"


@app.route("/")
def home():
    sol = request.args.get("sol")  # Get the "sol" parameter from the URL query string
    if sol is None:
        sol = 100  # Default sol value if not provided in the URL

    params = {
        "sol": sol,
        "api_key": api_key
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    image_count = len(data["photos"])

    photos = data["photos"]
    return render_template("index.html", photos=photos, sol=sol, image_count=image_count)


if __name__ == "__main__":
    app.run(debug=True)
