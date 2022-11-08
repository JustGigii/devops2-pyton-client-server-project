

workers =[]
isopen= True

class worker:
    def __init__(self,firstname,lastname,age,id,email,profession,salary,experience,department):
        self.workerid
        self.firstname
        self.lastname
        self.age
        self.id
        self.email
        self.profession
        self.salary
        self.experience
        self.department
  
def Show():
    print('for add worker press 1')    
    print('for remove worker press 2')
    print('for update worker press 3')
    print('for view worker press 4')
    print('for view all workers press 5')  
    print('for exit press 6')      
def Exit():
    global isopen
    isopen = False
def AddWorker():
    print("pls enter a firstname,lastname,age,id,email,profession,salary,experience,department with ,")
    #omri,gigi,22,000,mail,proggramer,65000,3,a
    answer = input()
    answer = answer.split()
    newWorker = worker(answer['firstname'],answer['lastname'],answer['age'],answer['id'],answer['email'],answer['profession'],answer['salary'],answer['experience'],answer['department'])
def RemoveWorker():
    print("RemoveWorker")
def UpdateWorker():
    print("UpdateWorker")
def ShowWorker():
    print("ShowWorker")
def ShowAllWorker():
    workers
    print("ShowAllWorker\n")
    print(worker)
    
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