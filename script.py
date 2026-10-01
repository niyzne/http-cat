import webbrowser
import random
import longlist

def random_links():
    times = int(input("How many links would you like?: "))

    for i in range(times):
        status = random.choice(list(longlist.http_cats))
        webbrowser.open(f"https://http.cat/{status}")
        print(f"Link {i+1} sent: https://http.cat/{status}")
