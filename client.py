import os
from WorkeClassr import worker
import json
import requests
import re
import csv
# workers = []
isopen = True
url = "http://127.0.0.1:5000"

def Show():
    print('for add worker press 1')
    print('for remove worker press 2')
    print('for update worker press 3')
    print('for view worker press 4')
    print('for view all workers press 5')
    print('for export all workers to csv press 6')
    print('for import workers from csv press 7')
    print('for exit press 8')


def ShowUpdate():
    print('for update worker press:')
    print('fristname:1\nlastname: 2\nage: 3\nid :4\nemail:5\nprofession :6\nsalary :7\nexperience: 8\n department 9\nexit 0')


# def workerdetails(workerid):
#     print("worker", "\n")
#     print(workerid, ": { firstname:", workers[workerid].firstname, "lastname:", workers[workerid].lastname, "age:", workers[workerid].age, "id:", workers[workerid].id, "email:", workers[
#         workerid].email, "profession:", workers[workerid].profession, "salary:", workers[workerid].salary, "experience:", workers[workerid].experience, "department:", workers[workerid].department,)

def valid(answer): #[Omri,Gigi,22,211881396,gigiomri@gmail.com,proggramer,65000,3,a] 
    if not re.search("^[A-Z][^A-Z0-9]*$", answer[0]):
        print("firstname must contain only uppercase letters.")
        return False
        
    if not re.search("^[A-Z][^A-Z0-9]*$", answer[1]):
        print("lastname must contain only uppercase letters and no numbers.")
        return False

    if (not re.search("^\d{9}$", answer[3]) ):
        print("ID is not valid")
        return False
    if (not valid_Id(answer[3])):
        print("ID is not valid")
        return False
    if not re.search("^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$", answer[4]):
        print("Invalid email address.")
        return False
    return True

def valid_Id(id):
    print("in"+ id)
    x = [1,2,1,2,1,2,1,2,1]
    id = int(id)
    for i in range(9):
        digit = id % 10
        temp = x[i] * digit
        if temp > 9 :
            while temp:
                sum += temp % 10 
                temp / 10 
        else:
            sum += temp 
        id = id / 10
    print(sum)
    if sum % 10 == 0 :
        return True
    else:
        return False



def Exit():
    global isopen
    isopen = False


def AddWorker():
    print("pls enter a firstname,lastname,age,id,email,profession,salary,experience,department with ,")
    # omri,gigi,22,000,mail,proggramer,65000,3,a
    #yohan,tubiana,35,123,yohantubiana@gmail.com,devops,70000,1,b
    try:
        answer = input()
        answer = answer.split(',')
        while valid(answer)==False:
            answer = input()
            answer = answer.split(',')
            
        newWorker = {
        "firstname":answer[0], #[A-Z]
        "lastname":answer[1], #[A-Z]
        "age": int(answer[2]),
        "id": answer[3],      #d+9
        "email": answer[4], # ___@___.com
        "profession":answer[5], #[A-Z]
        "salary": int(answer[6]),
        "experience": int(answer[7]),
        "department": answer[8] #a+
        }        
    except:
         print("the input is incorrect")
    # worker(int(answer[0]), answer[1], answer[2], int(
    #     answer[3]), answer[4], answer[5], answer[6], int(answer[7]), int(answer[8]), answer[9])
    # workers.append(newWorker)
    # x = requests.post(url+"/addworker", json=newWorker)
    # print(x.text)
    try:
        x = requests.post(url+"/addworker", json=newWorker)
        print(x.text)
    except:
        print("cannot connect to the sever")


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
            worker = {
                "workerid": int(updatemode[0]),
                "firstname":updatemode[1],
                "lastname":updatemode[2],
                "age": int(updatemode[3]),
                "id": updatemode[4],
                "email": updatemode[5],
                "profession":updatemode[6],
                "salary": int(updatemode[7]),
                "experience": int(updatemode[8]),
                "department": updatemode[9]
                }
            print(requests.put(url+'/worker',json=worker).text)
            updatemode = False


def ShowWorker():
    select = int(input("which worker you want to see\n"))
    print(requests.get(url+'/worker/'+str(select)).text)


def ShowAllWorker():
    # for wokerid in range(len(workers)):
    #     workerdetails(wokerid)
    print(requests.get(url+'/workers').text)

def exportTocsv():
    title = ['workerid','firstname','lastname','age','id','email','profession','salary','experience','department']
    name = input("how do you want to call the file")
    filename = name+'.csv'
    file = open(filename, 'w')
    writer = csv.writer(file)
    writer.writerow(title)
    workers= json.loads(requests.get(url+'/workers').text)
    for worker in workers:
        writer.writerow(worker)
        
    file.close()

def inportFrmcsv():
    print("in")
    name = input("what is the file name")
    filename = name+'.csv'
    with open(filename) as csv_file:
        data = csv.reader(csv_file)
        array = []
        ok = False
        for row in list(data):
            if not ok:
                ok= True
            else:
                array.append(row)
        print(array)


functions = {1: AddWorker,
             2: RemoveWorker,
             3: UpdateWorker,
             4: ShowWorker,
             5: ShowAllWorker,
             6: exportTocsv,
             7: inportFrmcsv,
             8: Exit}

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

# REGEX -done
# flask -done
# mysql -done
# csv  - to do
# datetime - done
# os -done