import time
import math

def calculate_square_root(number):
    return math.sqrt(number)

input_number = int(input("Enter the number: "))
delay_ms = int(input("Enter the delay time in milliseconds: "))

time.sleep(delay_ms / 1000)  
result = calculate_square_root(input_number)

print(f"The square root of number {input_number} after {delay_ms} milliseconds is {result}")