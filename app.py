
from flask import Flask, jsonify,request

app = Flask(__name__);
@app.route("/Bot", methods=["POST"])
def response():
    query = dict(request.form)['query']
    if(query=='Hi'):
        res='Hello'
    return jsonify({"response" : res})
if __name__=="__main__":
    app.run(host="0.0.0.0",)
