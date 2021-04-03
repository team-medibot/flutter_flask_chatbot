from flask import Flask, jsonify,request
import pandas as pd

app = Flask(__name__)

dataset = pd.read_csv("https://github.com/team-medibot/flutter_flask_chatbot/blob/main/Training.csv")

@app.route("/bot", methods=["POST"])
def response():
    query = dict(request.form)['query']
    if(query == "Hi"):
        result = "Hello"                                                                                                                                                       
    return jsonify({"response" : result})
if __name__=="__main__":
    app.run(host="0.0.0.0",)
