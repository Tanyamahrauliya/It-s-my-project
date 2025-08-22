message = "Hi! everyone"
print(message)
num = 0
while num <=10: 
    num +=1
    names = [
 "Aarav Mehta",
 "Priya Sharma",
 "Rohan Verma",
 "Anaya Singh",
 "Kabir Joshi",
 "Isha Patel",
 "Arjun Khanna",
 "Meera Nair",
 "Devansh Gupta",
 "Sanya Rao"
    ]
    name = input("👉  Enter your name :")
    if name.strip() in names:
         print(f"Hi!{name}✋")
         
    else:print("❌ Invalid input")
    number = input("👉  Enter your Roll number :") 
    if number =="1023" and name =="Aarav Mehta" :
         print(" Aarav Mehta is Present ✔✔👍 ")
    elif number =="1456":
         print(" Priya Sharma is Present ✔✔ 😊")
    elif number =="1890":
         print(" Rohan Verma is Present ✔✔ 😊")
    elif number =="2345":
         print("Anaya Singh is Present ✔✔ 😊")
    elif number =="2768 ":
         print(" Kabir Joshi is Present ✔✔ 😊")     
    elif number =="3129":
         print(" Isha Patel is Present ✔✔ 😊")
    elif number =="3567":
         print("Arjun Khanna is Present ✔✔ 😊")
    elif number =="4012": 
         print("Meera Nair is  Present ✔✔ 😊") 
    elif number =="4785":
         print("Devansh Gupta is Present ✔✔ 😊") 
    elif number =="5096":
         print(" Sanya Rao is Present ✔✔ 😊")  
    else:
        print(name,"this is not your roll number 😙\n Pleas enter your right roll number🤨")
    


     