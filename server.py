import json
from flask import Flask, request, jsonify, render_template
from WorkeClassr import worker

workers = []

# Create an intance of Flask
app = Flask(__name__)

# get to homepage


@app.route("/", methods=['Get'])
def gethomepage():
    return render_template('index.html')


@app.route("/addworker", methods=['POST'])
def addworker():
    jsondata = request.get_data()
    # newWorker = worker(int(jsondata["wokerid"]), jsondata["firstname"], jsondata["lastname"], int(jsondata["age"]), jsondata["id"],
    #                    jsondata["email"], jsondata["profession"], int(jsondata["salary"]), int(jsondata["experience"]), jsondata["department"])
    newWorker = json.loads(jsondata, object_hook=worker)
    for workerin in workers:
        if (newWorker.wokerid == workerin.workerid):
            response = jsonify("worker in the system")
            response.status_code = 400
            return response
    workers.append(newWorker)
    response = jsonify("worker add to the system")
    response.status_code = 200
    return response


@app.route("/workers", methods=['Get'])
def getallworkes():
    send = []
    for wokerid in range(len(workers)):
        send.append(str(workers[wokerid]))
    response = jsonify(send)
    response.status_code = 200
    return response


if __name__ == "__main__":
    app.run(debug=True)
