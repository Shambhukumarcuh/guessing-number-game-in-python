winning_no =27
user_input = input("Enter your guess no b/w 1 to 100 :")
user_input = int(user_input)
if user_input == winning_no:
    print( " Congratulations you are win.!")
else:
    if user_input<winning_no:
        print("TOO LOW")
    else:
        print( " TOO HIGH ")
