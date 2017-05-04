#Transporting Elephants
#Adva Masliah
#Python 3.4
#Mr.Noukhovitch
def right_path(correct, allstops): # Ask if the stops are correct and replaces them if they are not.
    if correct == "no" or correct == "No":
        while correct == "no" or correct == "No":
            changed = 0
            print("Which stop is incorrect?")#Get incorrect stop name.
            stop_incorrect = input()
            for s in range(len(allstops)):#Check if incorrect stop name is on the list.
                if allstops[s] == stop_incorrect:
                        print("What is the CORRECT Name of the stop?")#If incorrect stop name is on the list, asks for correct stop name.
                        correct_name = input()
                        allstops[s] = correct_name
                        changed = 1#Tells the following 'if' statement if the stop is on the list.
                
            if changed != 1:       
                print("Sorry that is not a stop on your path")
            print("Stops are: ", allstops)
            print("Are these all correct?")#Checks again.
            correct = input()#Able to loop forever untill all stops are correct.
print("Hello! Welcome to the Elephant Trip Stop Generator!")
print("Please make sure the elephants are fed before we start.")
print("How far are you travelling? please enter integer in km")
distance = input()
if distance.isdigit():#Checks if user entered a number.
    distance = int(distance)
while type(distance) != int:#Asks the user to retry if they inputted incorrect inputs.
    print("Incorrect input try again")
    distance = input()
    if distance.isdigit():
        distance = int(distance)
print("We assume your speed is 100km/h")
speed = 100
tstops = distance// 800#Must stop every 800km.
travel_time_h = distance// speed
travel_time_m = distance% speed
allstops = []
feeding_stops = []
feed_stops = 0
days_passed = 0
more_hours = 0
print("What time is it?(ex. 5:45)")
stime = input()
right_time = 0
while right_time != 1:
    for c in range(len(stime)):
        if stime[c] == ":" and len(stime[c+1:len(stime)]) == 2:
            right_time = right_time + 1
    if right_time != 1:
       print("Incorrect input try again")
       stime = input()
       right_time = 0
    
for i in range(len(stime)):# This loop divides the hours and the minues of the time given using the ':' then converts them into integers.
    if stime[i] == ":":
        hours = int(stime[0:i]) + travel_time_h
        minutes =  int(stime[i+ 1:len(stime)]) + travel_time_m
        while minutes >= 60:#Checks if hours have passed.
            minutes = minutes - 60
            more_hours = more_hours + 1
        while hours >= 24:#Checks if days have passed.
            hours = hours - 24 
            days_passed = days_passed + 1
        hours = hours + more_hours
        minutes = str(minutes)
        if len(minutes) < 2:# If minutes are only one digit adds a zero in the front ex. 5 into 05.
            minutes = "0" + minutes
endtime = str(hours) + ":" + str(minutes)#Time is converted back into a string.    

for i in range(tstops):#Appends list of stops, asks individually for each stop.
    ni = i + 1
    print("Where is the", ni, "place you will stop?")
    name = input()
    allstops.append(name)
print("Stops are:",allstops)
print("Are these all correct?")
print("Input 'yes' or 'no'")
correct = input()
right_path(correct, allstops)#Checks if all stops are correct.

for w in range(len(allstops)):#Since we stop every 800km every third stop is a feeding stop.
    feed_stops = feed_stops + 1
    if feed_stops % 3 == 0:
            feeding_stops.append(allstops[w])# Add each feeding stop to the list.
print("The feeding stops are:", feeding_stops)
print("Arrival Time =", endtime)
if days_passed > 0:
    print("Days passed =",days_passed)
print("Are you ready to go back")#Part two of the assignment.
Back = input()
while Back == "no" or Back == "No":
    print("Are you ready to go back")
    Back = input()
print("What is your final destination?")#Final Destination Question.
first_destination = input()
print("Is this the route you would like to take back?")
back_stops = []
going_back =len(allstops) - 2
for b in range(going_back, -1, -1):#Reverses the original stop list. 
    back_stops.append(allstops[b])
back_stops.append(first_destination)#Adds final destination to the end of the list.
print(back_stops)
correct = input()#Asks them if they would like to take any alternate routes.
right_path(correct,back_stops)


    


    
    
