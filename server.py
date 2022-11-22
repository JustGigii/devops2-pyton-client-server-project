from flask import Flask, request,jsonify



#Create an intance of Flask
app = Flask(__name__)

#get to homepage
@app.route("/", methods= ['Get'])
def gethomepage():
    return "<h1>wellcome to worker system servise. you can do alot of options with this api</h1>"





if __name__ == "__main__":
    app.run(debug=True)
    