from flask import Flask, jsonify,request
import pandas as pd

app = Flask(__name__)

dataset = pd.read_csv("https://raw.githubusercontent.com/team-medibot/flutter_flask_chatbot/main/Training.csv")

@app.route("/bot", methods=["POST"])
def response():
    query = dict(request.form)['query']
    if(query == "Hi"):
        result = "Hello"                                                                                                                                                       
    return jsonify({"response" : result})
if __name__=="__main__":
    app.run(host="0.0.0.0",)
'''


from flask import Flask, jsonify,request
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
import seaborn as sns
import random

app = Flask(__name__)
query = ''
response= ''
def load_data():
	train = pd.read_csv("https://raw.githubusercontent.com/team-medibot/flutter_flask_chatbot/main/Training.csv")
	train = shuffle(train)
	test = pd.read_csv("https://raw.githubusercontent.com/team-medibot/flutter_flask_chatbot/main/Testing.csv")
	test = shuffle(test)
	return train,test
def train_test(train, test):
	x = train.drop('prognosis', axis=1)
	y = train['prognosis']
	rfc = RandomForestClassifier(n_jobs=-1)
	rfc.fit(x, y)

	x_test = test.drop('prognosis', axis=1)
	y_test = test['prognosis']
		
	file = "model.pkl"
	fileobj = open(file, 'wb')
	pickle.dump(rfc,fileobj)

	

	predict = rfc.predict(x_test)
	return rfc
	
def predict_disease2(model,data):
    #print("Bot: Hi, This is your Virtual Assisstant, May i know your name")
    getResponse()
    name = query
    #print("Bot: Could you please help me out to know about your symptoms better")
    #print("Bot: Please answer the following symptoms with 'yes' or 'no' only\n Type quit whenever you want to end the chat")
    i = 0
    result = dict(zip(data.columns,[0]*len(data.columns)))
    
    pd.options.mode.chained_assignment = None  # default='warn'

    while(len(data.columns) > 0):
        col = data.columns[random.randint(0,len(data.columns)-1)]
       # print(f"\nBot: {name}, Are you having {col}.")
        setResponse(f"{name}, Are you having {col}.")
       
        getResponse()
        userInput = int(query) #0 and 1
        if(userInput==1):
            BotResponse='yes'
        else:
            BotResponse='no'
        #print(f"{name}: {BotResponse}")
        setResponse(f"{name}: {BotResponse}")
        if(BotResponse=="quit"):
            break
        
        if(BotResponse=="yes"):
            data = data[data[col]==1]
            result[col]=1
        elif(BotResponse=="no"):
            data = data[data[col]==0]
        else:
            while(BotResponse not in ['yes','no','quit']):
                setResponse("Bot: Oops...Wrong Input, Try again")
                #print("Bot: Oops...Wrong Input, Try again")
                getResponse()
                BotResponse=query
                BotResponse=BotResponse.lower()
            
            if(BotResponse=="yes"):
                data = data[data[col]==1]
                result[col]=1
            elif(BotResponse=="no"):
                data = data[data[col]==0]
            else:
                break

        data.drop(col,axis=1,inplace=True)
        
        for col in data:
            l=0
            for row in data[col]:
                if(row==0):
                    l=l+1
            if(l==len(data)):
                data.drop(col,axis=1,inplace=True)
        i=i+1
    
    pred_data=np.zeros(len(result))
    j=0
    for i in result:
        if(result[i]==1):
            pred_data[j]=result[i]
        j=j+1

    pred_data = pred_data.reshape(1,-1)
    setResponse("Process Completed")
    #print("\nProcess Completed")
    return model.predict(pred_data)


def main():
    train, test = load_data()

    #analyze_data(train)

    model = train_test(train,test)

    disease = predict_disease2(model,train.drop('prognosis',axis=1))
    #print(f'\nyou may have {disease[0]}')

@app.route("/bot", methods=["POST"])
def getResponse():
    query = dict(request.form)['query']                                                                                                                                                    
    #return jsonify({"response" : result})
@app.route("/bot", methods=["POST"])
def setResponse(query):
    #query = dict(request.form)['query']                                                                                                                                                    
    return jsonify({"response" : query})
if __name__=="__main__":
    #main()
    train, test = load_data()

    #analyze_data(train)

    model = train_test(train,test)

    disease = predict_disease2(model,train.drop('prognosis',axis=1))
    #print(f'\nyou may have {disease[0]}')
    app.run(host="0.0.0.0",)'''
