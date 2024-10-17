print("Welcome to Kaun Banega Carorpati(KBC)")

questions = [
    "Who was the first President of the United States?",
    "What is the capital city of France?",
    "Which planet is known as the Red Planet?",
    "What is the largest ocean on Earth?",
    "In which year did World War II end?",
    "Who wrote the play: Romeo and Juliet?",
    "Which element has the chemical symbol 'O'?",
    "What is the longest river in the world?",
    "Which country is known as the Land of the Rising Sun?",
    "Who painted the Mona Lisa?"
]

print("Game Rule: The total winning amount is $10,000; each correct answer contains $1,000. If you give any wrong answers, the game will end and you will only win money according to your correct answers")
print("=====================================================================================================================================")

# Question 1
print("Question 1: ", questions[0])
print("Options: 1) George Washington , 2) Imran Khan,  3) Obama,  4) Donald Trump")
A1 = input("Answer: ")

if A1 == "George Washington" or A1 == "george washington":
    print("Correct answer")
    print("Your Current Balance is: $1000")
    print("=====================================================================================================")
    print("Question 2: ", questions[1])
    print("Options: 1) Paris , 2) New York,  3) Amsterdam,  4) Portugal")
else:
    print("Incorrect answer")
    print("You lose")
    print("Your Current Balance is: $0")

# Question 2
A2 = input("Answer: ")

if A2 == "Paris" or A2 == "paris":
    print("Correct answer")
    print("Your Current Balance is: $2000")
    print("=====================================================================================================")
    print("Question 3: ", questions[2])
    print("Options: 1) Jupiter , 2) Uranus,  3) Saturn,  4) Mars")
else:
    print("Incorrect answer")
    print("Your Current Balance is: $1000")

# Question 3
A3 = input("Answer: ")

if A3 == "Mars" or A3 == "mars":
    print("Correct answer")
    print("Your Current Balance is: $3000")
    print("=====================================================================================================")
    print("Question 4: ", questions[3])
    print("Options: 1) Arabian Sea , 2) Atlantic Ocean,  3) Indian Ocean,  4) Pacific Ocean")
else:
    print("Incorrect answer")
    print("Your Current Balance is: $2000")

# Question 4
A4 = input("Answer: ")

if A4 == "Pacific Ocean" or A4 == "pacific ocean":
    print("Correct answer")
    print("Your Current Balance is: $4000")
    print("=====================================================================================================")
    print("Question 5: ", questions[4])
    print("Options: 1) 1878 , 2) 1942,  3) 2000,  4) 1945")
else:
    print("Incorrect answer")
    print("Your Current Balance is: $3000")

# Question 5
A5 = input("Answer: ")

if A5 == "1945":
    print("Correct answer")
    print("Your Current Balance is: $5000")
    print("=====================================================================================================")
    print("Question 6: ", questions[5])
    print("Options: 1) Oscar Wilde , 2) John Milton,  3) John Keats,  4) William Shakespeare")
else:
    print("Incorrect answer")
    print("Your Current Balance is: $4000")

# Question 6
A6 = input("Answer: ")

if A6 == "William Shakespeare" or A6 == "william shakespeare":
    print("Correct answer")
    print("Your Current Balance is: $6000")
    print("=====================================================================================================")
    print("Question 7: ", questions[6])
    print("Options: 1) Carbon monoxide , 2) Hydrogen,  3) Oxygen,  4) Nitrogen")
else:
    print("Incorrect answer")
    print("Your Current Balance is: $5000")

# Question 7
A7 = input("Answer: ")

if A7 == "Oxygen" or A7 == "oxygen":
    print("Correct answer")
    print("Your Current Balance is: $7000")
    print("=====================================================================================================")
    print("Question 8: ", questions[7])
    print("Options: 1) Amazon River , 2) River Irtysh,  3) Congo River,  4) The Nile River")
else:
    print("Incorrect answer")
    print("Your Current Balance is: $6000")

# Question 8
A8 = input("Answer: ")

if A8 == "The Nile River" or A8 == "the nile river":
    print("Correct answer")
    print("Your Current Balance is: $8000")
    print("=====================================================================================================")
    print("Question 9: ", questions[8])
    print("Options: 1) China , 2) Japan,  3) Indonesia,  4) Australia")
else:
    print("Incorrect answer")
    print("Your Current Balance is: $7000")

# Question 9
A9 = input("Answer: ")

if A9 == "Japan" or A9 == "japan":
    print("Correct answer")
    print("Your Current Balance is: $9000")
    print("=====================================================================================================")
    print("Question 10: ", questions[9])
    print("Options: 1) Michelangelo, 2) Monet,  3) Leonardo da Vinci,  4) Salvador Dalí")
else:
    print("Incorrect answer")
    print("Your Current Balance is: $8000")

# Question 10
A10 = input("Answer: ")

if A10 == "Leonardo da Vinci" or A10 == "leonardo da vinci":
    print("Correct answer")
    print("Your Current Balance is: $10000")
    print("CONGRATULATIONS!! YOU WON THE GAME")
else:
    print("Incorrect answer")
    print("Your Current Balance is: $9000")
