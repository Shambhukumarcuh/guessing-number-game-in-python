# guessing-number-game-in-python
this code to help to create a python game for users , guess a random number and win 
winning_no =27
user_input = input("enter your guess no b/w 1 to 100 :")
user_input = int(user_input)
if user_input == winning_no:
    print( " you win!!")
else:
    if user_input<winning_no:
        print("TO LOW")
    else:
        print( " TO HIGH ")
