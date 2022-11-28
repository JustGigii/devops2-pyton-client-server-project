import json
from flask import Flask, request, jsonify, render_template
from WorkeClassr import worker

workers = [
              {'workerid': 1, 'firstname': 'omri', 'lastname': 'gigi', 'age': 22, 'id': '000', 'email': 'mail', 'profession': 'proggramer', 'salary': 65000, 'experience': 3, 'department': 'a'},
              {'workerid': 2, 'firstname': 'alon', 'lastname': 'choen', 'age': 34, 'id': '123', 'email': 'mail', 'profession': 'proggramer', 'salary': 65000, 'experience': 3, 'department': 'a'}
          ]

# Create an intance of Flask
app = Flask(__name__)

# get to homepage


@app.route("/", methods=['Get'])
def gethomepage():
    return render_template('index.html')


@app.route("/addworker", methods=['POST'])
def addworker():
    newWorker = request.get_json()
    for workerin in workers:
        if (newWorker['workerid'] == workerin['workerid']):
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

@app.route('/worker/<workerid>', methods=['GET'])
def getuser(workerid):
    for worker in workers:
        if worker['workerid'] == int(workerid):
            response = jsonify(worker)
            response.status_code = 200
            return response
    response = jsonify("worker no found")
    response.status_code = 404
    return response 

@app.route('/worker/<workerid>', methods=['DELETE'])
def deleteuser(workerid):
    for worker in workers:
        if worker['workerid'] == int(workerid):
            workers.remove(worker)
            response = jsonify("succses to delete worker")
            response.status_code = 200
            return response
    response = jsonify("worker no found")
    response.status_code = 404
    return response 

@app.route("/worker", methods=['PUT'])
def updateworker():
    newWorker = request.get_json()
    for workerin in workers:
        if (newWorker['workerid'] == workerin['workerid']):
            workers.remove(workerin)
            workers.append(newWorker)
            response = jsonify("worker update")
            response.status_code = 200
            return response
    workers.append(newWorker)
    response = jsonify("worker add to the system")
    response.status_code = 200
    return response

if __name__ == "__main__":
    app.run(debug=True)
