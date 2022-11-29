import os
from WorkeClassr import worker
import json
import requests
# workers = []
isopen = True
url = "http://127.0.0.1:5000"

def Show():
    print('for add worker press 1')
    print('for remove worker press 2')
    print('for update worker press 3')
    print('for view worker press 4')
    print('for view all workers press 5')
    print('for exit press 6')


def ShowUpdate():
    print('for update worker press:')
    print('fristname:1\nlastname: 2\nage: 3\nid :4\nemail:5\nprofession :6\nsalary :7\nexperience: 8\n department 9\nexit 0')


# def workerdetails(workerid):
#     print("worker", "\n")
#     print(workerid, ": { firstname:", workers[workerid].firstname, "lastname:", workers[workerid].lastname, "age:", workers[workerid].age, "id:", workers[workerid].id, "email:", workers[
#         workerid].email, "profession:", workers[workerid].profession, "salary:", workers[workerid].salary, "experience:", workers[workerid].experience, "department:", workers[workerid].department,)


def Exit():
    global isopen
    isopen = False


def AddWorker():
    print("pls enter a firstname,lastname,age,id,email,profession,salary,experience,department with ,")
    # omri,gigi,22,000,mail,proggramer,65000,3,a
    #yohan,tubiana,35,123,yohantubiana@gmail.com,devops,70000,1,b
    answer = input()
    answer = answer.split(',')
    newWorker = {
    "firstname":answer[0],
    "lastname":answer[1],
    "age": int(answer[2]),
    "id": answer[3],
    "email": answer[4],
    "profession":answer[5],
    "salary": int(answer[6]),
    "experience": int(answer[7]),
    "department": answer[8]
    }
    # worker(int(answer[0]), answer[1], answer[2], int(
    #     answer[3]), answer[4], answer[5], answer[6], int(answer[7]), int(answer[8]), answer[9])
    # workers.append(newWorker)
    tojson = newWorker
    x = requests.post(url+"/addworker", json=tojson)
    print(x.text)


def RemoveWorker():
    select = int(input("pls enter the workerid\n"))
    print(requests.delete(url+'/worker/'+str(select)).text)


def UpdateWorker():
    updatemode = True
    select = int(input("which worker you want to edit\n"))
    updateuser =  json.loads(requests.get(url+'/worker/'+str(select)).text)[0]
    print(updateuser)
    while updatemode:
        ShowUpdate()
        selectupdate = int(input("which details you want to edit\n"))
        if selectupdate != 0:
            value = input("pls enter value\n")
            match selectupdate:
                case 1:
                    updateuser[0] = value
                case 2:
                    updateuser[2] = value
                case 3:
                   updateuser[3] = int(value)
                case 4:
                   updateuser[4]= value
                case 5:
                   updateuser[5] = value
                case 6:
                   updateuser[6] = value
                case 7:
                   updateuser[7] = int(value)
                case 8:
                   updateuser[8] = int(value)
                case 9:
                   updateuser[9] = value
                case _:
                    print("Worng number")
        else:
            print(requests.put(url+'/worker',json=updateuser).text)
            updatemode = False


def ShowWorker():
    select = int(input("which worker you want to see\n"))
    print(requests.get(url+'/worker/'+str(select)).text)


def ShowAllWorker():
    # for wokerid in range(len(workers)):
    #     workerdetails(wokerid)
    print(requests.get(url+'/workers').text)


functions = {1: AddWorker,
             2: RemoveWorker,
             3: UpdateWorker,
             4: ShowWorker,
             5: ShowAllWorker,
             6: Exit}


def main():
    print('welcome to the ultimate worker system\n')
    while (isopen):
        Show()
        select = int(input())
        functions[select]()
        input("pls press eny key to contune")
        os.system("cls")  # os.system("clear") to linux

    print('the program stop')


if __name__ == '__main__':
    main()
#yohan,tubiana,35,123,yohantubiana@gmail.com,devops,70000,1,b