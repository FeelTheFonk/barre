# test.py
from barre import b
from time import sleep

# Simple range test
print("Test 1: Simple range")
for x in b(range(10)):
    sleep(0.2)  # progression

# List test
print("\nTest 2: Custom List")
items = ["item1", "item2", "item3", "item4"]
for x in b(items):
    sleep(0.5)  # simulation