import string
import random
len = int(input("Enter length of your password:"))
cat = input("enter password category like weak,strong,very strong:")

if cat=="weak" :
    all_charac= string.ascii_lowercase
elif cat=="strong":
    all_charac= string.ascii_letters + string.digits
else:
     all_charac = string.ascii_letters + string.punctuation + string.digits        

ranArr = random.choices(all_charac,k=len)
ranStr = "".join(ranArr)
print(ranStr)



