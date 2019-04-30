#!/usr/bin/env python
MAX_COUNT = 5

count = 0
while True:
    user_name = input("What is your name (q to quit)? ")
    if user_name == 'q':
        count = 0
        print("Buh-bye!")
        break
    if user_name == '':
        print("Please enter a name")
        count = count + 1
        if count >= MAX_COUNT:
            print("Why are you just hitting ENTER?")
        continue
    print(f"Processing {user_name}")
