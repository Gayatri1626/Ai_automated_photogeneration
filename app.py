from flask import Flask, render_template, request, jsonify, session
import os
import requests
import replicate
import json
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "default_secret_key")

# Hardcoded API keys for testing (⚠️ do not push to production like this)


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN

# Load shots.json
with open("shots.json", "r") as f:
    shots_data = json.load(f)

@app.route("/")
def index():
    return render_template("index.html", shots=shots_data)

@app.route("/generate_image/<int:index>", methods=["POST"])
def generate_image(index):
    prompt = shots_data[index]["mjPrompt"]

    try:
        response = requests.post(
            "https://api.openai.com/v1/images/generations",
            headers={
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "dall-e-3",
                "prompt": prompt,
                "n": 1,
                "size": "1024x1024",
                "quality": "standard"
            }
        )

        if response.status_code == 200:
            image_url = response.json()["data"][0]["url"]
            images = session.get("images", {})
            images[str(index)] = image_url
            session["images"] = images
            return jsonify({"image_url": image_url})
        else:
            return jsonify({"error": "OpenAI image generation failed"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/upscale_image/<int:index>")
def upscale_image(index):
    if "images" not in session or str(index) not in session["images"]:
        return jsonify({"error": "No image found for this index."}), 400

    original_url = session["images"][str(index)]

    try:
        output = replicate.run(
            "stability-ai/sdxl:7762fd07cf82c948538e41f63f77d685e02b063e37e496e96eefd46c929f9bdc",
            input={
                "width": 1024,
                "height": 1024,
                "prompt": "Enhance quality of the image: " + original_url,
                "refine": "expert_ensemble_refiner",
                "apply_watermark": False,
                "num_inference_steps": 25
            }
        )
        upscaled_url = str(output[0])
        return jsonify({"upscaled_url": upscaled_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
