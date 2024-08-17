import random
def inp_func(user_input):
    if(user_input == 0):
        usr_ip = "rock"
    elif(user_input == 1):
        usr_ip = "scissors"
    elif(user_input == 2):
        usr_ip = "paper"
    else:
        usr_ip = "Invalid input"
    return usr_ip

usr_ip_num = int(input("Press 0 for rock, 1 for scissors, 2 for paper\n"))
usr_ip = inp_func(usr_ip_num)
print(f"User input : {usr_ip}")

com_ip_num = random.randint(0,2)
com_ip = inp_func(com_ip_num)
print(f"Computer input : {com_ip}")

if(usr_ip_num == com_ip_num):
    print("Game is draw")
elif( usr_ip_num == 1 and com_ip_num == 2):
    print("User wins!")
elif(usr_ip_num == 0 and com_ip_num == 1):
    print("User wins!")
elif(usr_ip_num == 2 and com_ip_num == 0):
    print("User wins!")
elif( usr_ip_num == 92 and com_ip_num == 1):
    print("Computer wins!")
elif(usr_ip_num == 1 and com_ip_num == 0):
    print("Computer wins!")
elif(usr_ip_num == 0 and com_ip_num == 2):
    print("Computer wins!")
else:
    print("Please enter a valid number between 0,1 and 2 to play")

