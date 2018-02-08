import pyautogui as pg
import time
import webbrowser

points = 0

# Question 1

answer = pg.prompt(
"""
Which would you rather do?

a) Go to a record store
b) shop for clothes
c) play basketball at the park

"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3



# Question 2

answer = pg.prompt(
"""
Who do you hate?

a) Derek
b) Chris 
c) Dan

"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3


# Question 3

answer = pg.prompt(
"""
Who is your best friend?

a) Brooke
b) Jamie 
c) Skills

"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3


# Question 4

answer = pg.prompt(
"""
Who do you like the most?

a) Lucas
b) Julian
c) Chase

"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3



# Question 5

answer = pg.prompt(
"""
Where do you want to live?

a) Los Angeles
b) New York City
c) Europe

"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3


# Question 6

answer = pg.prompt(
"""
Where do you work?

a) Record shop
b) Clothing shop
c) Scott Auto body shop

"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3


# Question 7

answer = pg.prompt(
"""
Who's your favorite enemy?

a) Dan
b) Nanny Carrie
c) Nathan 

"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

# Question 8

answer = pg.prompt(
"""
Who is your favorite character?

a) Chris Keller
b) Mouth Mcfadden
c) Coach Whitey Durham

"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3


#END OF SURVEY

pg.alert("You are...")

# Peyton
if points < 13:
    pg.alert("Peyton Sawyer")
    webbrowser.open("https://assets-auto.rbl.ms/e134cd2da6f5e964ea2554a757e5fddf5e459cb7bd5aadbf753f279004556663")

# Brooke
elif points >= 14 and points < 19:
    pg.alert("Brooke Davis")
    webbrowser.open("https://data.whicdn.com/images/70320651/original.gif")

# Lucas
elif points >= 19 :
    pg.alert("Lucas Scott")
    webbrowser.open("http://78.media.tumblr.com/80a4ce1e44c13721ce975c33dabb335b/tumblr_mg887cfe8F1rypsblo4_250.gif")
    
