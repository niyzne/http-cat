import webbrowser
import random

times = int(input("Enter A number: "))

for i in range(times):
    status = str(random.choices(range(100, 599 + 1)))
    webbrowser.open(f"https://http.cat/{status[1:-1]}")
