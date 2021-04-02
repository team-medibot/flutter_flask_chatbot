
from flask import Flask, jsonify,request
import time
app = Flask(__name__)
@app.route("/bot", methods=["POST"])
def response():
    query = dict(request.form)['query']
    if(query=="Hi"):
        res = "Hello MediBot here!" #+ " " + time.ctime()
    return jsonify({"response" : res})
if __name__=="__main__":
    app.run(host="0.0.0.0",)
