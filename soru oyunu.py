from tkinter.messagebox import YES
print('welcome')
player=input('What''s your name?')
print(f"Welcome to the quiz game {player}.This game including 10 questions.") 
playing=input("Do you want to play?  ")
if playing.lower() != "yes":
   quit
print('okey let''s play the game :)  ')
points=0 

print(f'{player} For now your points is {points} but it will be change  :)  ')

answer=input('what does IT workers?')
if answer.lower() == "they are working for it companies":
    print('you are right')    
    points+=1
    print(f'Congrats {player} !Your point is {points}')
else:
     print('you are wrong')
     points-=1
     print(f'Sorry your points {points} try to next time.:) ') 

print('congrats you have passed first question.')
answer=input('What is salesforce?')
if answer=='salesforce is a crm':
    points+=1
    print(f'Congrats {player} !Your point is {points}')
else:
     points-=1
     print('you are wrong')
     print(f'Sorry {player} your points {points} try to next time.:) ')

answer=input('What is Phyton?')
if answer.lower()=='phyton is a software language':
    points+=1
    print(f'Congrats {player} !Your point is {points}')
else:
     print('you are wrong')
     points-=1
     print(f'Sorry your points {points} try to next time.:) ')
     
answer=input('Who is the father of Computer science?')
if answer.lower()=='Charles Babbage':
    points+=1
    print(f'Congrats {player} !Your point is {points}')
else:
     print('you are wrong')
     points-=1
     print(f'Sorry your points {points} try to next time.:) ')

answer=input('Which services for cloud we have?')
if answer.lower()=='google,amazon,cloud':
    points+=1
    print(f'Congrats {player} !Your point is {points}')
else:
     print('you are wrong')
     points-=1
     print(f'Sorry your points {points} try to next time.:) ')

answer=input('In which type of computer, data are represented as discrete signals?')
if answer.lower()=='Digital Computer':
    points+=1
    print(f'Congrats {player} !Your point is {points}')
else:
     print('you are wrong')
     points-=1
     print(f'Sorry your points {points} try to next time.:) ')

answer=input('What is FORTRAN?')
if answer.lower()=='Formula Translation':
    points+=1
    print(f'Congrats {player} !Your point is {points}')
else:
     print('you are wrong')
     points-=1
     print(f'Sorry your points {points} try to next time.:) ')

answer=input('Where does most data go first with in a computer memory hierarchy?')
if answer.lower()=='RAM':
    points+=1
    print(f'Congrats {player} !Your point is {points}')
else:
     points-=1
     print('you are wrong')
     print(f'Sorry your points {points} try to next time.:) ')

answer=input('A program that performs a useful task while simultaneously allowing destructive acts is _______?')
if answer.lower()=='Trojan Horse':
    points+=1
    print(f'Congrats {player} !Your point is {points}')
else:
     print('you are wrong')
     points-=1
     print(f'Sorry your points {points} try to next time.:) ') 

answer=input('Full form of NOS?')
if answer.lower()=='Network Operating system':
    points+=1
    print(f'Congrats {player} !Your point is {points}')
else:
     print('you are wrong')
     points-=1
     print(f'Sorry your points {points} try to next time.:) ')

answer=input('BCD is _______?')
if answer.lower()=='Binary Coded Decimal':
    points+=1
    print(f'Congrats {player} !Your point is {points}')
else:
     print('you are wrong')
     points-=1
     print(f'Sorry your points {points} try to next time.:) ')

answer=input('	To move a copy of file from one computer to another over a communication channel is called?')
if answer.lower()=='File Transfer':
     points+=1
     print(f'Congrats {player} !Your point is {points}')
else:
     print('You are wrong')
     points-=1
     print(f'your point is {points}')

result=points
print(f'Well done {player} you have been answering 12 questions,your result is {result} and your percantage'+  str((result/12)*100))
if result<5:
 print(f'what a donkey!')
elif 10>result>5:
    print(f'More then expectation.Great.Congrat''s {player} ')
else:
 print(f'Out of this world!!  {player} quite good your result {result}')
quit