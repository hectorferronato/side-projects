
# Transfer Db.py to a txt file,
# so it does not forget,
# and checks memory before webSearching.

# Ask if user wants to know more about a subject,
# then search again. ChatBot knows we are in one subject,
# ask if want to stay or switch subjects and talk about other things.

# Activate translation.

# Make both ChatBot online.

import time
from time import gmtime, strftime
import random
import os
import re
import wikipedia
import requests.packages.urllib3

from rake import Rake
from amarBotDB import  (engagementPairs,
                        confused_responses,
                        farewell_responses,
                        filtered_responses,
                        filtered_words,
                        memory,)

requests.packages.urllib3.disable_warnings()

class Amar():
    def __init__(self):
        self.lang = 'en-US'
        self.speed = .5

    def __alpha__(self,userInput):
        regex = re.compile('[^a-zA-Z]')
        return regex.sub('',userInput)

    def __filterWord__(self,userInput):
        clean = self.__alpha__(userInput)
        if(clean not in filtered_words): 
            return clean 
        else: 
            return "Blocked"

    def __getInputCategory__(self,userInput):
        # checked = {} ; duplicate checks are happening

        for pairIdx in range(len(engagementPairs)):
            for answerIdx in range(len(engagementPairs[pairIdx][0])):
                filteredInput = self.__filterWord__(userInput)

                if filteredInput == "Blocked":
                    return filtered_words

                answer = engagementPairs[pairIdx][0][answerIdx].lower()
                if filteredInput == self.__filterWord__(answer): 
                    return engagementPairs[pairIdx][0]

    def __getOutputCategory__(self,inputCategory):
        category = []

        for pairIdx in range(len(engagementPairs)):
            if inputCategory==engagementPairs[pairIdx][0]:
                if len(engagementPairs[pairIdx][1])==1:
                    category=engagementPairs[pairIdx][1][0]
                else:
                    category=random.choice(engagementPairs[pairIdx][1])

        return category

    def __getMainWords__(self,userInput):
        rake = Rake("SmartStoplist.txt")
        keywords = rake.run(userInput)
        return keywords

    # def __remember__(self,input,answer):
    #input = self.__getMainWords__(input)
    #     if input in memory:
    #         memory[input].append(answer)
    #     else: memory[input] = [answer]

    # def __format__(self,):
    #     make it a visually appealing string

    def __think__(self,userInput):
        answer = "Thinking..."

        #subject = random.choice(self.__getMainWords__(userInput))[0]
        answer = wikipedia.summary(userInput,sentences=.5,auto_suggest=True,redirect=True)
        if answer == "missing": 
            answer = "Sorry, I don't know about it.. you are the only thing that matters!"
                
        return answer

    def reply(self,userInput):
        inputCategory = self.__getInputCategory__(userInput)
        if inputCategory:
            outputCategory = self.__getOutputCategory__(inputCategory)
            outputAnswer = random.choice(outputCategory)
        else: 
            outputAnswer = self.__think__(userInput)
            #self.__remember__(userInput,outputAnswer)

        #time.sleep(self.speed)
        return outputAnswer
