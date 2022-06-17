import requests

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


deck = response.json()
deck_id = deck['deck_id']
remaining_cards=deck['remaining']
print(deck_id)
print(remaining_cards)
#Run the generated Python code

    #To run the generated Python code, you need to have a working Python environment set up. 
#1 Start up a virtual environment for Python, and make sure you install the requests library.
       #$ virtualenv venv
       #$ source venv/bin/activate
       #$ pip install requests

#$ virtualenv venv
#$ source venv/bin/activate
#$ pip install requests
#run code
#$ python deck_of_cards.py

#If you cannot get the generated code to run, check your environment. 
# One error you may see is: TypeError: 'instancemethod' object has no attribute '__getitem__', 
# #which means the requests library is not installed in the environment.




#Save the file as shufflecards.py. It should contain this code


#shuffle the cards python code for drawing cards



#n the editor, write these Python lines to put the returned deck_id into a variable. 
#Because the returned JSON data can be used as a Python dictionary, by putting the response.json() #into a dictionary variable, the code can get the exact ID we want, repeatably

