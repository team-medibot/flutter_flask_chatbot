from flask import Flask, jsonify,request

app = Flask(__name__)
@app.route("/bot", methods=["POST"])
def response():
    query = dict(request.form)['query']
    if(query == "Hi"):
        result = "Hello"                                                                                                                                                       
    return jsonify({"response" : result})
if __name__=="__main__":
    app.run(host="0.0.0.0",)
