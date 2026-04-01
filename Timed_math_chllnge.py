import random
import time

operators = ["+", "-", "*", "/"]
min_value = 1
max_value = 10
max_problems = 10


def generate_problem():
    num1 = random.randint(min_value, max_value)
    num2 = random.randint(min_value, max_value)
    operator = random.choice(operators)

    if operator == "+":
        return f"{num1} + {num2}", num1 + num2
    elif operator == "-":
        return f"{num1} - {num2}", num1 - num2
    elif operator == "*":
        return f"{num1} * {num2}", num1 * num2
    elif operator == "/": 
        num1 = num1 * num2  # Ensure the division results in an integer
            # Ensure no division by zero and integer division
        while num2 == 0:
            num2 = random.randint(min_value, max_value)

        return f"{num1} / {num2}", num1 // num2

wrong = 0
input("Welcome to the Math Quiz! Press Enter to start...")  

print("Let's get started! Solve the following problems:")
print("---------------------------------------------")
strt_time = time.time()  # Start the timer

for i in range(max_problems):
    problem, answer = generate_problem()
    while True:
        guess = input(f"Problem {i + 1}: {problem} = ? (Answer: )")
        star = int(guess)  # Convert the guess to an integer

        if star == answer:
            print("Correct!")
            break
        else:
            print("Incorrect. Try again.")
            wrong += 1

end_time = time.time()  # End the timer
elapsed_time = end_time - strt_time

print(f"Quiz completed! You had {wrong} wrong answers.")    
print("Thank you for playing the Math Quiz!")
print(f"Your total time: {elapsed_time:.2f} seconds")
print("Have a great day!")
print("----------------------------------------------")