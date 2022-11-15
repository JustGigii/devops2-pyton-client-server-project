

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
def workerdetails(workerid):
    print("worker ",workerid,": { firstname: ",workers[workerid].firstname,"lastname: ",workers[workerid].lastname,"age: ",workers[workerid].age,"id: ",workers[workerid].id,"email: ",workers[workerid].email,"profession: ",workers[workerid].profession,"salary: ",workers[workerid].salary,"experience: ",workers[workerid].experience,"department: ",workers[workerid].department)


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
    print("RemoveWorker")
def UpdateWorker():
    print("UpdateWorker")
def ShowWorker():
    select = int(input("which worker you want to see"))
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
    print('the program stop')
if __name__ =='__main__':
    main()