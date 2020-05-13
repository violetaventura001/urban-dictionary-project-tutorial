import requests, os, sys

# Retrieve your API credentials from the .env file
if os.getenv("API_KEY") is None or os.getenv("API_KEY") == "":
    print("ERROR! Make sure you have created your .env file with your API credentials (look for the .evn.example as an example and replace it with your own API credentials that you got from RapidAPI)")
    exit(1)

# Get credentials from the .env file
API_HOST = os.getenv("API_HOST")
API_KEY = os.getenv("API_KEY")

# continue with your application here

def sync_word(_word,_permission,_data):
    print("#####", _word, _permission, _data)
    text_file = open( "data/"+_word + ".txt",_permission)
    print("**",text_file)
    if _permission =="w+": 
        text_file.write(_data)
    else:
        return text_file.read()
    text_file.close()

word = ""

if len(sys.argv) ==1:
    word = input("What term do you want to look for?")
else:
    word = sys.argv[1]

if os.path.isfile("./src/"+ word + ".txt"):
    print("fetching")
    print(sync_word(word,"r"))
else:
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define?term=" + word

    headers = {
            'x-rapidapi-host': API_HOST,
            'x-rapidapi-key': API_KEY
            }

    response = requests.request("GET", url, headers=headers)

    body = response.json()

    print("****",body['list'][0]['definition'])
    sync_word(word,"w+",body['list'][0]['definition'])

