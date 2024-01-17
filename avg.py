def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

num_count = int(input("Enter the number of values : "))
user_numbers = []

for i in range(num_count):
    user_input = float(input(f"Enter number {i + 1}: "))
    user_numbers.append(user_input)

avg_result = calculate_average(user_numbers)
print("Average : ", avg_result)
