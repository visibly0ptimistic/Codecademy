# Get = snack name
# Vote = keep track of snack votes

Votes = []

def Vote(name):
    Votes.append(name)
    return Votes

Vote("KitKat")

print(Votes)