

### 📝 `README.md`

```markdown
# 🏨 Hotel Photography Shot Generator

This is a Flask-based web app that helps generate and upscale hotel photography shots using AI models from OpenAI and Replicate.

---

## 🔧 Features

- 📸 Generate hotel photography visuals using **DALL·E 3 (OpenAI)**
- 🚀 Upscale the generated images using **SDXL model (Replicate)**
- 💾 Prompt data comes from a `shots.json` file
- 🖼️ View all shots, generate images,download them and upscale them — all from a web UI

---

## 📁 Project Structure

```

hotel-shot-generator/
├── app.py                # Main Flask app
├── templates/
│   └── index.html        # Frontend UI
├── shots.json            # JSON file with hotel shot prompts
├── .env                  # Environment variables (for API keys)
└── README.md             # Project overview

````

---

## 🔐 Setup & API Keys

You’ll need:

1. **OpenAI API Key** for image generation
2. **Replicate API Token** for upscaling

Create a `.env` file in the project root:

```env
FLASK_SECRET_KEY=your_flask_secret
OPENAI_API_KEY=your_openai_api_key
REPLICATE_API_TOKEN=your_replicate_api_token
````

---

## 📦 Install Dependencies

```bash
pip install flask requests python-dotenv replicate
```

---

## 🚀 Run the App

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser.

---

## 🧠 Data Format (`shots.json`)

Each entry in `shots.json` should follow this format:

```json
[
  {
    "area": "Lobby",
    "shotCode": "L01",
    "bestTime": "Evening",
    "mjPrompt": "Warm lobby lighting with guests entering, cinematic style."
  },
  ...
]
```

> 💡 You can create this manually or extract it from your assignment doc.

---

## 🛠 Troubleshooting

* ❌ `"No image found for this index"`: Happens when you upscale without generating first.
* ❌ `OpenAI image generation failed`: Check your OpenAI API key and quota.
* ❌ `ReplicateError: Invalid version`: Use correct model version ID and token.

---


