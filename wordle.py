import sys                    # call the sys library

WoD = sys.argv[1]                                          # Run the program in the terminal window.
for i in range(0, 6):                                       # User will hav 6 guesses thanks to the for loop
    guess = input("Enter your 5-letter guess :")
    if WoD != guess:
        print("The length of word must be five!")

    if WoD == guess:

        print("Congratulations! You guess right in " + str(i+1) + "th shot!")

        break               # Loop ends if condition comes true
    if i == 5:
        print("you lost the right word is : ", WoD)
    else:
        x = 0          # It checks the elements of the array in  order
        y = 0          # It checks the elements of the WoD in  order

        for letter in guess:           # this for loop checks every letter
            counter = 0           # It's
            if len(WoD) == len(guess):
                if WoD.__contains__(guess[y]) is True:          # This  Boolean function checks the letter exist in th WoD or not
                    if guess[x] == WoD[y]:
                        print(guess[y], "letter exists and located in right position")

                    else:
                        print(guess[y], " letter exists but located in wrong position")

                else:
                    print(guess[y], "letter does not exist.")

            x += 1               # Increments the 'counter' after every letter of guess.
            y += 1               # Increments the counter after every letter of WoD.