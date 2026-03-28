from flask import Flask, request, jsonify

app = Flask(__name__)

AI_THRESHOLD = 65

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    score = float(data.get("ai_score", 0))

    if score >= AI_THRESHOLD:
        decision = "TAKE TRADE"
    else:
        decision = "SKIP TRADE"

    print(f"{decision} | Score: {score}")

    return jsonify({"decision": decision})

app.run(host="0.0.0.0", port=5000)
