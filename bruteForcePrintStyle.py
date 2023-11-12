import time

MESSAGE = 'hello world69' # Change to your heart's content
COMBINATIONS = 'abcdefghijklmnopqrstuvwxyz1234567890'

def combineArr(arr):
    str = ""
    
    for i in arr:
        str += i
    
    return str

currentState = []
letterCount = 0;

for i in MESSAGE:
    letterCount +=1

    for x in COMBINATIONS:
        if i == " ":
            currentState.append(" ")
            break

        # If this spot in array is empty, add something as placeholder
        if len(currentState) < letterCount:
            currentState.append(x)

        currentState[letterCount - 1] = x

        print(combineArr(currentState))
        time.sleep(0.1) # For the extra cool effect of "brute force"
        
        if i == x:
            break