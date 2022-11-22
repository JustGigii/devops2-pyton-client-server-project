import os

workers =[]
isopen= True

class worker:
    def __init__(self,firstname,lastname,age,id,email,profession,salary,experience,department):
        self.workerid = len(workers)
        self.firstname =firstname
        self.lastname =lastname
        self.age =age
        self.id =id
        self.email =email
        self.profession =profession
        self.salary = salary
        self.experience = experience
        self.department = department
  
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
   
   
def workerdetails(workerid):
    print("worker",workerid,": { firstname:",workers[workerid].firstname,"lastname:",workers[workerid].lastname,"age:",workers[workerid].age,"id:",workers[workerid].id,"email:",workers[workerid].email,"profession:",workers[workerid].profession,"salary:",workers[workerid].salary,"experience:",workers[workerid].experience,"department:",workers[workerid].department,"\n")


def Exit():
    global isopen
    isopen = False
    
    
def AddWorker():
    print("pls enter a firstname,lastname,age,id,email,profession,salary,experience,department with ,")
    #omri,gigi,22,000,mail,proggramer,65000,3,a
    answer = input()
    answer = answer.split(',')
    newWorker = worker(answer[0],answer[1],answer[2],answer[3],answer[4],answer[5],answer[6],answer[7],answer[8])
    workers.append(newWorker)


def RemoveWorker():
    select=int(input("pls enter the workerid\n"))
    workers.remove(workers[select])
    
    
def UpdateWorker():
    updatemode = True
    select = int(input("which worker you want to edit\n"))
    while updatemode:
        ShowUpdate()
        selectupdate = int(input("which details you want to edit\n"))
        if selectupdate != 0:
            value =input("pls enter value\n")
            match selectupdate: 
                case 1:
                    workers[select].firstname = value 
                case 2:
                    workers[select].lastname = value 
                case 3:
                    workers[select].age = value
                case 4:
                    workers[select].id = value
                case 5:
                    workers[select].email = value
                case 6:
                    workers[select].profession = value
                case 7:
                    workers[select].salary = value
                case 8:
                    workers[select].experience = value
                case 9:
                    workers[select].department = value  
                case _:
                    print("Worng number")
        else:
            updatemode=False
            
                        
def ShowWorker():
    select = int(input("which worker you want to see\n"))
    workerdetails(select)
   
    
def ShowAllWorker():
    for wokerid in range(len(workers)):
        workerdetails(wokerid)
        
    
functions = {1:AddWorker, 
             2:RemoveWorker,
             3:UpdateWorker,
             4:ShowWorker,
             5:ShowAllWorker,
             6:Exit }  


def main():
    print('welcome to the ultimate worker system\n')
    while(isopen):
        Show()
        select = int(input())
        functions[select]()
        input("pls press eny key to contune")
        os.system("cls") #  os.system("clear") to linux
        
    print('the program stop')
    
    
if __name__ =='__main__':
    main()