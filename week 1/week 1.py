#WARM-UP EXERCISES:
#Complete the three short scripts sketched below.  Comments indicate which lines need to be added or modified. Use the ''' to active each question as you move through

#0) Dummy variables (no work to do here):
print('Question 0: Dummy variables \n__________________')
name = 'Marcus'
rating = 4.4
output = f'{name} is feeling {rating}/6 today'
print(output)


#1.1) Take input:
print('\n__________________\nQuestion 1: Take Input \n__________________')
name = 'Oliver'
rating = float(input("What is your happiness score?"))#ask user to enter a happiness score from 1-6
output = f'{name} is feeling {float(rating)}/6 today'
print(type(rating))
print(output)


#1.2) Convert to float:
ratingAsFloat = rating #convert happiness score into a decimal number
print(type(ratingAsFloat))
ratingOutOfTen = (ratingAsFloat/6)*10 #convert so that score is out of 10
output = f'{name} is feeling {ratingOutOfTen:.0f}/10 today'
print(output)

#2.1) Collective happiness:
print('\n__________________\nQuestion 2: Collective Happiness \n__________________')
persons = ['Jack','Jill','Mary','Tom','Peter']
happinessScores = []
for x in persons: #Loop across the persons list
    rating10 = input(f'How happy is {x} today? (1-10)')
    happinessScores.append(float(rating10))
print(happinessScores)

#2.2) Mary's mood:
i = 2
# Use index i to access the name and happiness of someone from the persons list


#3.1) What's the mood?
print('\n__________________\nQuestion 3: What\'s the Mood? \n__________________')
groupMood = sum(happinessScores)/len(happinessScores)
print(groupMood)
#Split the mood at 5/10 (modify line below)
if groupMood >= 5:
    print('What a fantastic day.')
else:
    print('Not the best day.')

#3.2) Be more specific:
if "groupMood" in globals():
    mean = sum(happinessScores)/len(happinessScores)
else:
    groupMood = 6.4
# Modify the if block below to print either "High times!", "But not an all time high/ low.", or "Very poor, in fact." depending on the collective happiness score:
if groupMood >= 8:
    print('High times!')
elif 8 > groupMood >= 5:
    print('But not an all time high/ low.')
#Lines needed here
else:
    print('Very poor, in fact.')