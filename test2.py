

def collatz(number):
	answer = 0
	if(number%2 == 0):
		answer = number // 2
	elif(number % 2 == 1):
		answer = number * 3 + 1
	return answer


print("Please input a number.")
try:
	userInput = int(input())
except Exception as e:
	print("Please input an integer.")
	print("exception is ", e)
	exit()

finalValue = userInput

while True:
    if finalValue != 1:
    	finalValue = collatz(finalValue)
    	print("Current value is ", finalValue)	
    elif finalValue == 1:
    	break
    	
   
print("The final value is ", finalValue)
