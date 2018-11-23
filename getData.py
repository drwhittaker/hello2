# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:37:37 2016

@author: ericgrimson


def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)   
        if t[1] not in words:   
            words = words + (t[1],)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return (min_nums, max_nums, unique_words)


(small, large, words) = get_data(((1, 'mine'), 
                                  (3, 'yours'),
                                  (5, 'ours'),
                                  (7, 'mine')))

animals=('Dog', 'cat')
new =()
a = (('Lyon','Doggie'), ('david','person'))
b = (('klinka','cat'), ('allison','wife'))
c = a + b
print(str(c))

print()
for t in a:
    print(t)
    new = new + (t[0],)
    if t[1] in animals:
        print("it is an animal")
        
    
print(new)
 """

listA = [1,4,3,0]   
listA
    

import pyttsx3
engine = pyttsx3.init()
pyttsx3.engine.Engine
engine.setProperty('rate', 200)


engine.say("I will speak this text")
engine.runAndWait() 


voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)
   print(voice.id)
   engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()


import win32com.client as wincl

name = input('What is your name?')
proceed = input('Would you like to proceed? ')
if proceed == "yes":
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak("Hello" + name + " How are you doing today? Happy Thanksgiving! Have a good time today!" )
    speak.Speak(name)
else:
    print('ok')
dog = ' cats and dogs'  
engine.say(dog)

