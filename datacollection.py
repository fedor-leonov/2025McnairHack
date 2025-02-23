def askState(message):
    return input("From a scale of 1-10, how " + message)
def getHourlyStats():
    appetite = askState("hungry are you?")
    energy = askState("energetic are you?")
    happiness = askState("happy are you?")
    wellness = askState("well are you?")

getHourlyStats()
