import requests
import math
from time import sleep
print("Please enter your API key, we will check if you have permission to access this model.")
api_key = input()
API_URL = "https://api-inference.huggingface.co/models/datasciencemmw/current-best"
headers = {"Authorization": "Bearer " + api_key}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
print("Please type in the input for the AI to process.")	
usrinput = input()
output = query({
	"inputs": usrinput,
})
print("Expert mode or Noob mode? Type E for Expert mode and N for Noob mode!")
mode = input("E or N? ")
lst = output[0]
out = lst[0]
if mode.lower() == 'n':
    print("Score: " + out['label'] + " Confidence: " + str(math.trunc(out['score']*100)))
elif mode.lower() == 'e':
    print("Would you like the confidence level raw or in decimals? R for raw and D for decimals.")
    confidencelvl = input("R or D? ")
    if confidencelvl.lower() == 'r':
        print("Score: " + out['label'] + " Confidence: " + str(out['score']))
    elif confidencelvl.lower() == 'd':
        print("Score: " + out['label'] + " Confidence: " + str(out['score']*100))
    else:
        print("ERROR 400: Bad Request")
        sleep(3.7)
        print("The mode you provided is not valid.")
        sleep(2)
        print("Restart this program to try again.")
else:
    print("ERROR 400: Bad Request")
    sleep(3.7)
    print("The mode you provided is not valid.")
    sleep(2)
    print("Restart this program to try again.")