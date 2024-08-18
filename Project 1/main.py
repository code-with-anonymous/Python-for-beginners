import random

computer = random.choice([-1,0,1])
user= input("Enter your choice: ")
dic= {"s": 1, "w": -1, "g": 0}
resverse_dic= {1: "Snake", -1: "Water", 0: "Gun"}
you= dic[user]
print(you)
print(f"User choose {resverse_dic[you]}\nComputer choose {resverse_dic[computer]} ")

if(computer == you):
    print("Its a draw")

else:
    if(computer ==-1 and you == 1): 
        print("You win!")

    elif(computer ==-1 and you == 0):
        print("You Lose!")

    elif(computer == 1 and you == -1):
        print("You lose!")

    elif(computer ==1 and you == 0):
        print("You Win!")

    elif(computer ==0 and you == -1):
        print("You Win!")

    elif(computer == 0 and you == 1):
        print("You Lose!")

    else:
        print("Something went wrong!")