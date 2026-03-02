# SNAKE , GUN  , WATER
'''
Snake=1
Water=-1
Gun=0
'''
import random

Player_1 = random.choice([1, 0, -1])

you=input("Enter Your choice(s/w/g): ")
c_dict={"s":1, "w":-1 , "g":0 }
your_choice=c_dict[you]

reverse_dict={ 1:"Snake" , -1:"Water" , 0:"Gun"}
print(f"You choose: {reverse_dict[your_choice]}")
print(f"Player1 choose: {reverse_dict[Player_1]}")

# if Player_1 == your_choice:
#     print("Its a draw")
# else:
#     if Player_1 ==1 and your_choice == -1:
#         print("You Lose!")
#     elif  Player_1 ==0 and your_choice == -1:
#         print("You Win!")        
#     elif  Player_1 ==-1 and your_choice == 1:
#         print("You Win!") 
#     elif  Player_1 ==1 and your_choice == 0:
#         print("You Win!") 
#     elif  Player_1 ==0 and your_choice == 1:
#         print("You Lose!")
#     elif  Player_1 ==-1 and your_choice == 0:
#         print("You Lose!")                    
#     else: 
#         print("Something went wrong")    


       
        # OR

        # Result logic
if Player_1 == your_choice:
    print("It's a Draw!")

elif (your_choice == 1 and Player_1 == -1) or \
     (your_choice == -1 and Player_1 == 0) or \
     (your_choice == 0 and Player_1 == 1):
    print("You Win!")

else:
    print("You Lose!")