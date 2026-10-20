import time
difficulty = ""
print("-------------------------------------------------------------")
print("             Welcome to the Python Cafe Game!")
print("-------------------------------------------------------------")
time.sleep(0.5)
print("Difficulty : Easy : Medium : Hard : Extreme")
time.sleep(0.5)
difficulty_selector = input("Please select a difficulty!")
if difficulty_selector == 'Easy':
    difficulty = "Easy"
    print(f"Difficulty Selected : {difficulty}")
elif difficulty_selector == 'Medium':
    difficulty = "Medium"
    print(f"Difficulty Selected : {difficulty}")
elif difficulty_selector == 'Hard':
    difficulty = "Hard"
    print(f"Difficulty Selected : {difficulty}")
elif difficulty_selector == 'Extreme':
    difficulty = "Extreme"
    print(f"Difficulty Selected : {difficulty}")
