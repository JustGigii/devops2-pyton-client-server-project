import json
from flask import Flask, request,jsonify,render_template
from  WorkeClassr import worker

workers =[]

#Create an intance of Flask
app = Flask(__name__)

#get to homepage
@app.route("/", methods= ['Get'])
def gethomepage():
    return render_template('index.html')

@app.route("/addworker",methods= ['POST'])
def addworker():
    jsondata = request.get_json() 
    newWorker = worker(jsondata["workerid"],jsondata["firstname"],jsondata["lastname"],jsondata["age"],jsondata["id"],jsondata["email"],jsondata["profession"],jsondata["salary"],jsondata["experience"],jsondata["department"])
    for workerin in workers:
        if(newWorker.workerid == workerin.workerid):
            response = jsonify("worker in the system")
            response.status_code=400
            return response
    workers.append(newWorker)
    response = jsonify("worker add to the system")
    response.status_code=200
    return response


if __name__ == "__main__":
    app.run(debug=True)
    