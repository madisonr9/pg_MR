import webbrowser
name = "Madison"

subjects = ["English","Spanish","History","Math","Science"]

print("Hello " + name)

for i in subjects:
    print("one of my classes is " + i)
    
tvshows = ["How I Met Your Mother","Friends", "One Tree Hill", "Gossip Girl", "Vampire Diaries"]

for i in tvshows:
    if i == "One Tree Hill":
        print(i + " is such a dramatic, but good show. ")
    elif i == "How I Met Your Mother":
        print(i + " Is one of the best shows ever. ")
    elif i == "Vampire Diaries":
        print(i + " Is not that good of a show. ")
    else:
        print("one of my favorite tv shows is " + i)
colors = []

while True:
    print(" What is your favorite color? Type 'end' to quit.")
    answer = input()
    if answer == "end":
        break
    else:
        colors.append(answer)

for i in colors:
    print("One of your favorite colors is " + i)
    webbrowser.open(i)
    
