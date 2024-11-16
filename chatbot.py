import openai
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# OpenAI API Key (replace with your actual API key)
openai.api_key = "your_openai_api_key"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    
    # Default response if no input is provided
    if not user_message:
        return jsonify({"reply": "I’m here to help! Please ask a question about tours and travel."})
    
    # Prompt setup for the chatbot
    prompt = f"""
    You are a chatbot for a tours and travel company. Answer questions about destinations, travel packages, flight bookings, accommodations, and itineraries. 
    Always provide friendly and helpful responses. If unsure, recommend contacting a travel agent.
    
    User: {user_message}
    Chatbot:
    """
    
    try:
        # Call OpenAI's GPT model
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=["User:", "Chatbot:"],
            temperature=0.7
        )
        reply = response.choices[0].text.strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": "I’m having trouble responding right now. Please try again later."})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
