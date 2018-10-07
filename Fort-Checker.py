import requests
from requests_html import HTMLSession

print("Fort-Checker\nCreated by AzureTheScripter / Azure#0263")
print("To begin, enter a username to find!")

username = input("Fortnite Name: ")
session = HTMLSession()

r = session.get(f"https://fortnitetracker.com/profile/search?q={username}")
if r.html.search('404 Not Found'):
    print(f"Name: '{username}' is available!")
    
else:
    print(f"Name: '{username}' is taken!\nAccount info:")
    if r.html.search('PSN'):
        print("Platform: PSN")
    if r.html.search('PC'):
        print("Platform: PC")
