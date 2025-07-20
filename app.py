from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# 🔑 Replace with your actual Bing API key
BING_API_KEY = 'YOUR_BING_API_KEY'
BING_SEARCH_URL = "https://api.bing.microsoft.com/v7.0/search"

def detect_problem_from_image(image_data):
    # Placeholder for real AI model
    # You can integrate OpenAI Vision or Google Vision later
    return "leaf blight in rice crop"

def search_web_solution(query):
    headers = {"Ocp-Apim-Subscription-Key": BING_API_KEY}
    params = {"q": query + " treatment in agriculture", "count": 1}

    response = requests.get(BING_SEARCH_URL, headers=headers, params=params)
    response.raise_for_status()
    results = response.json()
    
    if 'webPages' in results and results['webPages']['value']:
        top_result = results['webPages']['value'][0]
        return f"{top_result['snippet']} (Read more: {top_result['url']})"
    
    return "No suitable solution found online."

@app.route("/analyze", methods=["POST"])
def analyze_image():
    data = request.get_json()
    image_b64 = data.get("image")
    if not image_b64:
        return jsonify({"error": "No image provided"}), 400

    problem = detect_problem_from_image(image_b64)
    solution = search_web_solution(problem)
    return jsonify({"problem": problem, "solution": solution})

if __name__ == "__main__":
    app.run(debug=True)
