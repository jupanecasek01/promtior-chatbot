from flask import Flask, request, jsonify
import os
import asyncio
from bot import execute_agent

app = Flask(__name__)

@app.route("/api/messages", methods=["POST"])
@app.route("/api/messages", methods=["POST"])
def messages():
    question = request.json.get("question")
    conversation_id = request.json.get("conversation_id")

    # Llama a la función execute_agent de manera síncrona
    output = execute_agent(question, conversation_id)

    return jsonify({"response": output["final_response"]})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)