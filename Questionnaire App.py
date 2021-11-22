##where I will be putting my code following the ASI questions and ratings.


import time
print("Addiction Severity Index, based on 5th Addition")
total = []

#I've numbered where the questions will be, will most likely add more than listed below and it will be actual questions and not numbers holding the spots.
questions = ['1',         
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '10',
            '11',
            '12',
            '13',
            '14',
            '15',
            '16',
            '17',
            '18',
            '19',
            '20']

#once I figure out the number of answers for each question, this will be the first answer for each question or "a"
ans0 = ['a. ',
        'a. ',
        'a. ',
        'a. ',
        'a. ',
        'a. ',
        'a. ',
        'a. ',
        'a. ',
        'a. ',
        'a. ',
        'a. ',
        'a. ',
        'a. ',
        'a. ',
        'a. ',
        'a. ',
        'a. ',
        'a. ',
        'a. ']
#this will be the second answer for each question or "b"
ans1 = ['b. ',
        'b. ',
        'b. ',
        'b. ',
        'b. ',
        'b. ',
        'b. ',
        'b. ',
        'b. ',
        'b. ',
        'b. ',
        'b. ',
        'b. ',
        'b. ',
        'b. ',
        'b. ',
        'b. ',
        'b. ',
        'b. ',
        'b. ']
#this will be the third answer for each question or "c"
ans2 = ['c. ',
        'c. ',
        'c. ',
        'c. ',
        'c. ',
        'c. ',
        'c. ',
        'c. ',
        'c. ',
        'c. ',
        'c. ',
        'c. ',
        'c. ',
        'c. ',
        'c. ',
        'c. ',
        'c. ',
        'c. ',
        'c. ',
        'c. ']
ans3 = ['d. ',
        'd. ',
        'd. ',
        'd. ',
        'd. ',
        'd. ',
        'd. ',
        'd. ',
        'd. ',
        'd. ',
        'd. ',
        'd. ',
        'd. ',
        'd. ',
        'd. ',
        'd. ',
        'd. ',
        'd. ',
        'd. ',
        'd. ']
ans4 = ['e. ',
        'e. ',
        'e. ',
        'e. ',
        'e. ',
        'e. ',
        'e. ',
        'e. ',
        'e. ',
        'e. ',
        'e. ',
        'e. ',
        'e. ',
        'e. ',
        'e. ',
        'e. ',
        'e. ',
        'e. ',
        'e. ',
        'e. ']
ans5 = ['f. ',
        'f. ',
        'f. ',
        'f. ',
        'f. ',
        'f. ',
        'f. ',
        'f. ',
        'f. ',
        'f. ',
        'f. ',
        'f. ',
        'f. ',
        'f. ',
        'f. ',
        'f. ',
        'f. ',
        'f. ',
        'f. ',
        'f. ',]

def questionaire():
    rounds = 0
    while rounds < 20: #this number may change if I add more questions
        print('Question ')
        print(rounds + 1)
        print(category[rounds] + ':')
        print('0 :' + ans0[rounds])
        print('1 :' + ans1[rounds])
        print('2 :' + ans2[rounds])
        print('3 :' + ans3[rounds])
        print('4 :' + ans4[rounds])
        print('5 :' + ans5[rounds])
        q1 = input('Answer: \n')
        print(q1)
        # if q1 is not 0 or 1 or 2 or 3 or 4 or 5:
        #     print('Please select a valid answer')
        #     rounds = rounds
        if q1 is 0 or 1 or 2 or 3 or 4 or 5:
            total.append(int(q1))
            rounds = rounds + 1
            print('\n')
    else:
        print(total)
        print(sum(total))
questionaire()

#this is a work in progress on figuring out the scoring
progress = open("progress.txt", "w")
if 1 <= sum(total) <= 10:
    print('No problem')
    progress.write(time.ctime() + " SCORE:" + str(sum(total)) + " SEVERITY: No problem" + "\n")
elif 11 <= sum(total) <= 16:
    print('Slight Problem')
    progress.write(time.ctime() + " SCORE:" + str(sum(total)) + " SEVERITY: Slight Problem" + "\n")
elif 17 <= sum(total) <= 20:
    print('Moderate Problem')
    progress.write(time.ctime() + " SCORE:" + str(sum(total)) + " SEVERITY: Moderate Problem" + "\n")
elif 21 <= sum(total) <= 30:
    print('Severe Problem')
    progress.write(time.ctime() + " SCORE:" + str(sum(total)) + " SEVERITY: Severe Problem" + "\n")
elif 31 <= sum(total):
    print('Extreme Problem')
    progress.write(time.ctime() + " SCORE:" + str(sum(total)) + " SEVERITY: Extreme Problem" + "\n")
            
progress.close()

print ("INTERPRETING THE ADDICTION SEVERITY INDEX '\n'", "Total Score _______ Levels of Addiction '\n'",
      "1-10 _______ These ups and downs are considered normal '\n'", "11-16 _______ Slight Addiction '\n'",
      "17-20 ______ Moderate Addiction '\n'", "21-30 ______ Severe Addiction '\n'",
      "Over 31 ______ Extreme Addiction")
