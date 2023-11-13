import time

message = input("Input : ").lower()
COMBINATIONS = 'abcdefghijklmnopqrstuvwxyz1234567890'

def combineArr(arr):
    str = ""
    
    for i in arr:
        str += i
    
    return str

currentState = []
letterCount = 0;

for i in message:
    letterCount +=1

    for x in COMBINATIONS:
        if i == " ":
            currentState.append(" ")
            break

        # If this spot in array is empty, add something as placeholder
        if len(currentState) < letterCount:
            currentState.append(x)

        currentState[letterCount - 1] = x

        # Handle special chars
        if x == "0" and i != x:
            currentState[letterCount - 1] = i

        print(combineArr(currentState))
        time.sleep(0.1) # For the extra cool effect of "brute force"