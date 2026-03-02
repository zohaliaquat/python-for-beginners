print("WELCOME TO THE NIM GAME")
print("There are 7 sticks on the table.")
print("Each turn you may take 1, 2, or 3 sticks.")
print("Whoever takes the LAST stick loses.\n")

sticks = 7

# Who goes first
choice = input("Do you want to go first? (yes/no): ").lower()

# Computer first move
if choice == "no":
    print("Computer takes 2 sticks.")
    sticks -= 2
    print("Sticks left:", sticks)

# Game loop
while sticks > 0:

    # ----- Player turn -----
    player = int(input("How many sticks do you take (1-3)? "))

    # validate input
    while player < 1 or player > 3 or player > sticks:
        player = int(input("Invalid choice. Pick 1, 2, or 3 sticks: "))

    sticks -= player
    print("Sticks left:", sticks)

    # check winner
    if sticks == 0:
        print("You took the last stick. Computer wins!")
        break

    # ----- Computer turn -----
    # Winning strategy (leave 5, then 1)
    if sticks > 1:
        computer = 4 - player
        if computer > sticks:
            computer = 1
    else:
        computer = 1

    print("Computer takes", computer, "stick(s).")
    sticks -= computer
    print("Sticks left:", sticks)

    # check winner
    if sticks == 0:
        print("Computer took the last stick. You win!")
        break