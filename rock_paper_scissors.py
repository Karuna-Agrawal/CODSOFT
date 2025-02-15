import random
print("Hey!Are You READY?\n")
#inp= input("Choose Rock,Paper,Scissor:")
arr = ["rock","paper","scissor"]
#com = random.choice(arr)
user_score =0
com_score= 0
flag =True
while(flag):
   inp= input("Choose Rock,Paper,Scissor:")
   com = random.choice(arr)
   if (inp==com):
      print("OOPS! It's a tie.")
   elif (inp=="rock" and com=="paper") or (inp=="scissor" and com=="rock") or (inp=="paper" and com=="scissor"):
      print("Computer win\n")
      com_score = com_score+1
   elif(com=="rock" and inp=="paper") or (com=="scissor" and inp=="rock") or (com=="paper" and inp=="scissor"):
      print("User Win\n")
      user_score= user_score+1
   print("User  Move:",inp ," Score:",user_score,"\n")
   print("Computer  Move:",com," Score:",com_score,"\n")  
   flag = input("Wanna play more: YES OR NO \n") 
   if flag == "no":
      flag= False 



