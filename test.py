# test.py
from barre import b
from time import sleep

# Test avec simple range
print("Test 1: Simple range")
for x in b(range(10)):
    sleep(0.2)  # Pour voir la progression

# Test avec liste
print("\nTest 2: Liste personnalisée")
items = ["item1", "item2", "item3", "item4"]
for x in b(items):
    sleep(0.5)  # Simulation de traitement