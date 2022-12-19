from flask import Flask, request, jsonify, render_template
from flaskext.mysql import MySQL

# Create an intance of Flask
app = Flask(__name__)

# Create an intance of MySQL
mysql = MySQL()

# workers = [
#               {'workerid': 1, 'firstname': 'omri', 'lastname': 'gigi', 'age': 22, 'id': '000', 'email': 'mail', 'profession': 'proggramer', 'salary': 65000, 'experience': 3, 'department': 'a'},
#               {'workerid': 2, 'firstname': 'alon', 'lastname': 'choen', 'age': 34, 'id': '123', 'email': 'mail', 'profession': 'proggramer', 'salary': 65000, 'experience': 3, 'department': 'a'}
#           ]

#set database credentials in config
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'workers'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

#Initialize the MySql 
mysql.init_app(app)


# get to homepage
@app.route("/", methods=['Get'])
def gethomepage():
    return render_template('index.html')


@app.route("/addworker", methods=['POST'])
def addworker():
    newWorker = request.get_json()
    # for workerin in workers:
    #     if (newWorker['workerid'] == workerin['workerid']):
    #         response = jsonify("worker in the system")
    #         response.status_code = 400
    #         return response
    # workers.append(newWorker)
    # response = jsonify("worker add to the system")
    # response.status_code = 200
    # return response
    conncetion = mysql.connect()
    cursor = conncetion.cursor()
    cursor.execute(""" SELECT * FROM workers where id = %s """,int(newWorker['id']))
    rows = cursor.fetchall()
    if(len(rows) > 0):
        response = jsonify("worker in the system")
        cursor.close()
        conncetion.close()
        response.status_code = 400
        return response 
    else:
        query = "INSERT into workers(firstname,lastname,age,id,email,profession,salary,experience,department) VALUES (%s, %s ,%s,%s, %s ,%s,%s, %s ,%s)"
        cursor.execute(query,(newWorker["firstname"],newWorker["lastname"],int(newWorker["age"]),newWorker["id"],newWorker["email"],newWorker["profession"],int(newWorker["salary"]),int(newWorker["experience"]),newWorker["department"]))
        conncetion.commit()
        cursor.close()
        conncetion.close()
        response = jsonify("worker add to the system")
        response.status_code = 200
        return response
    

@app.route("/workers", methods=['Get'])
def getallworkes():
    # send = []
    # for wokerid in range(len(workers)):
    #     send.append(str(workers[wokerid]))
    # response = jsonify(send)
    conncetion = mysql.connect()
    cursor = conncetion.cursor()
    cursor.execute(""" SELECT * FROM workers """)
    rows = cursor.fetchall()
    response = jsonify(rows)
    cursor.close()
    conncetion.close()
    response.status_code = 200
    return response

@app.route('/worker/<workerid>', methods=['GET'])
def getuser(workerid):
    # for worker in workers:
    #     if worker['workerid'] == int(workerid):
    #         response = jsonify(worker)
    #         response.status_code = 200
    #         return response
    # response = jsonify("worker no found")
    # response.status_code = 404
    # return response 
    conncetion = mysql.connect()
    cursor = conncetion.cursor()
    cursor.execute(""" SELECT * FROM workers where workerid = %s """,int(workerid))
    rows = cursor.fetchall()
    cursor.close()
    conncetion.close()
    if(len(rows) > 0):
        response = jsonify(rows)
        response.status_code = 200
        return response
    else:
        response = jsonify("worker no found")
        response.status_code = 404
        return response 
    
@app.route('/worker/<workerid>', methods=['DELETE'])
def deleteuser(workerid):
    # for worker in workers:
    #     if worker['workerid'] == int(workerid):
    #         workers.remove(worker)
    #         response = jsonify("succses to delete worker")
    #         response.status_code = 200
    #         return response
    # response = jsonify("worker no found")
    # response.status_code = 404
    # return response 
    conncetion = mysql.connect()
    cursor = conncetion.cursor()
    cursor.execute(""" SELECT * FROM workers where workerid = %s """,int(workerid))
    rows = cursor.fetchall()
    if(len(rows) > 0):
        cursor.execute(""" DELETE FROM workers where workerid = %s """,int(workerid))    
        conncetion.commit()
        cursor.close()
        conncetion.close()
        response = jsonify("succses to delete worker")
        response.status_code = 200
        return response
    else:
        cursor.close()
        conncetion.close()
        response = jsonify("worker no found")
        response.status_code = 404
        return response     
        
        
@app.route("/worker", methods=['PUT'])
def updateworker():
    newWorker = request.get_json()
    # for workerin in workers:
    #     if (newWorker['workerid'] == workerin['workerid']):
    #         workers.remove(workerin)
    #         workers.append(newWorker)
    #         response = jsonify("worker update")
    #         response.status_code = 200
    #         return response
    # workers.append(newWorker)
    # response = jsonify("worker add to the system")
    # response.status_code = 200
    # return response
    conncetion = mysql.connect()
    cursor = conncetion.cursor()
    cursor.execute(""" SELECT * FROM workers where workerid = %s """,int(newWorker['workerid']))
    rows = cursor.fetchall()
    if(len(rows) == 0):
        response = jsonify("worker not found")
        cursor.close()
        conncetion.close()
        response.status_code = 400
        return response 
    else:
        query = "UPDATE workers firstname= %s,lastname= %s,age= %s,id= %s,email= %s,profession= %s,salary= %s,experience= %s,department= %s WHERE workerid = %s"
        cursor.execute(query,(newWorker["firstname"],newWorker["lastname"],int(newWorker["age"]),newWorker["id"],newWorker["email"],newWorker["profession"],int(newWorker["salary"]),int(newWorker["experience"]),newWorker["department"],int(newWorker['workerid'])))
        conncetion.commit()
        cursor.close()
        conncetion.close()
        response = jsonify("worker update in the system")
        response.status_code = 200
        return response
    
if __name__ == "__main__":
    app.run(debug=True)
