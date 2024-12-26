numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while True:
    UserInput = input("Enter a number \"(Q)uit\": ")
    if UserInput.upper() == "Q":
        break
    elif (UserInput).isdigit() == False:
        print("Please enter a valid digit!")
        continue
    print(f"La table de multiplication du nombre {UserInput}:")
    for number in numbers:
        print(f"{UserInput} x {number} = {int(UserInput) * number}")
