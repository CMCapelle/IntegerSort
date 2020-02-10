import random

#create list with range of 0-9
unordered = list(range(10))

#create empty list to append to
ordered = []

#create variable to increment through indexes
i = 0

#shuffle list
random.shuffle(unordered)

#initialize variable for lowest digit equal to first index in unordered list
lowest = unordered[0]

#print(len(unordered))

#loop through unordered list to remove and append lowest digits to ordered list
while len(unordered) > 0:
    if  unordered[i] < lowest:
        lowest = unordered[i]
    i += 1
    if i == len(unordered):
        ordered.append(lowest)
        unordered.remove(lowest)
        if unordered:
          lowest = unordered[0]
        i = 0

print(ordered)

input("\n\nPress the enter key to exit")
