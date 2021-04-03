from flask import Flask, jsonify,request

app = Flask(__name__)
@app.route("/bot", methods=["POST"])
def response():
    query = dict(request.form)['query']
    (query == "Hi")?return jsonify({"response" : "Hello"}):return null
if __name__=="__main__":
    app.run(host="0.0.0.0",)
