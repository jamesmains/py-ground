import requests
city = input("What city would you like to get weather information about?\n")
#city = "London"
print("Getting weather information...")
response = requests.get(f"https://wttr.in/{city}?0")
print(response.text)