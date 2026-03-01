print("Select your ride:")
print("1. Bike")
print("2. Car")

choice = int(input("Enter your choice:") )

if (choice == 1):
    print("What type of bike?")
    print(" 1. scooty")
    print(" 2. scooter")

    choice2=int(input("Enter your choice"))
    if choice2==1:
       print("you have selected scooty")
    else:
       print("you have selected scooter")

elif(choice == 2):
   print("what type of car?" )
   print("1. Sedan")
   print("2. XUV")
   choice3=int(input("enter your choice3: "))


   if choice3==1:
      print("you have selected sedan")
   else:
      print("you have selected XUV") 