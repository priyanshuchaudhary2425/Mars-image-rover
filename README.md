# Mars Image Rover 🚀

Explore Mars from your browser! This project uses the **NASA Mars Rover API** to fetch images taken by rovers on any given **sol (Martian day)**, along with details like camera, rover name, and earth date.  

Built with **Flask** and **REST APIs**, this project helped me learn how to interact with external APIs while following my love for space.

## Features
- Fetch Mars rover images by sol (Martian day)  
- Shows details: camera, rover, and earth date  
- Web-based interface using Flask  

## Requirement
1. Create a `.env` file in the project root  
2. Get your **NASA API key** from [https://api.nasa.gov/](https://api.nasa.gov/)  
3. Add it to your `.env` file:
```

API_KEY=your_api_key

````

## How to Use
Open your terminal and run all at once:
```bash
git clone https://github.com/priyanshuchaudhary2425/Mars-image-rover.git && cd Mars-image-rover && pip install -r requirements.txt && python main.py
````

Then open your browser at:
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

* Optionally, add `?sol=200` in the URL to view images from a specific Martian day, e.g.:

```
http://127.0.0.1:5000/?sol=200
```

Enjoy exploring the Red Planet! 🪐
