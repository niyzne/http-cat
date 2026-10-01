import webbrowser
import random
import longlist

times = int(input("Enter A number: "))

for i in range(times):
    status = random.choice(list(longlist.http_cats))
    webbrowser.open(f"https://http.cat/{status}")
