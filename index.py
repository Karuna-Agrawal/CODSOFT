# TO DO LIST
taskList={"study":"incomplete",
           "dance":"incomplete"} 

def viewtasklist():
    print(taskList)
print("hey!I am your task manager,here is your TO DO List")
if len(taskList)==0:
    print("OOPS!It's empty...Wanna add one\n")
    inp=input("Yes or No\n")
    if (inp=="yes"):
        task= input("Enter your first task:")
else:
    viewtasklist()

flag = True           
while flag==True:
   print("What you want next?Here are some functions:\n 1.Add task \n 2.Mark as done \n 3.Delete task \n 4.View TO DO List \n 5.End the loop\n" )
   inp2 =int(input("Enter your number:"))
   if (inp2== 1):
           task= input("\nEnter your task:\n")
           taskList[task]= "incomplete"
           print("Done Successfully\n")
   elif( inp2== 2) :
           task = input("\nEnter your task which is completed")
           taskList[task]="completed"
           print("Done Successfully\n")
   elif inp2== 3:
           task = input("\nEnter task which you want to delete:")
           taskList.pop(task)
           print("Done Successfully\n")
   elif inp2== 4:
            viewtasklist()    
   else:
           flag= False     
  
                  
    

    
