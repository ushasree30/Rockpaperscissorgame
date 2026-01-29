import random
item=["Rock","Paper","Scissors"]
computer=random.choice(item)
user=input("Enter your move = Rock,Paper,Scissors:")
print(f"user:{user},\n computer:{computer}")
if user==computer:
    print("Both choice is same,It's a tie")
elif user=="Rock":
    if computer=="Paper":
        print("Paper cover the rock computer wins")
    else:
        print("Rock smashes Scissors user wins")
elif user=="Paper":
    if computer=="Scissors":
        print("Scissors cut the paper computer wins")
    else:
        print("Paper covers the rock user wins")
elif user=="Scissors":
    if computer=="Rock":
        print("Rock smashes the scissors computer wins")
    else:
        print("Scissors cut the paper user wins")
        