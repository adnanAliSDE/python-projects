'''
This program determines your speed of typing
'''
import time

# Program
t=time.time()
inp=input("Start typing: ")
t2=time.time()
inpList=inp.split(" ")
print(f"Your typing speed is: {60*(len(inpList)/(t2-t))} wpm")