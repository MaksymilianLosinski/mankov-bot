import os.path
import json

#source: https://www.youtube.com/watch?v=L97yQMT0jn8

def main(sentence=""):
    dictionaryFile = "dictionary.json"
    inputFile = sentence
    dictionary = loadDictionary(dictionaryFile)

    if inputFile != "":
      learn(dictionary, sentence)
      updateFile(dictionaryFile, dictionary)
      
    else:
        with open("message_list.txt", "r") as file:
          lines = file.readlines()
          for sentence in lines:
              sentence = sentence.replace("\n", "")
              if "-|-" in sentence:
                sentences = sentence.split("-|-")
                for sentence in sentences:
                  learn(dictionary, sentence)
                  updateFile(dictionaryFile, dictionary)
              else:
                learn(dictionary, sentence)
                updateFile(dictionaryFile, dictionary)
        # #Interactive mode
        # while True:
        #     userInput = input(">> ")
        #     if userInput == "":
        #         break

        #     dictionary = learn(dictionary, userInput)
        #     updateFile(dictionaryFile, dictionary)

def loadDictionary(filename):
    if not os.path.exists(filename):
        file = open(filename, "w")
        json.dump({}, file)
        file.close()

    file = open(filename, "r")
    dictionary = json.load(file)
    file.close()
    return dictionary

def learn(dict, input):
    tokens = input.split(" ")
    for i in range(0, len(tokens)-1):
        currentWord = tokens[i]
        nextWord = tokens[i+1]

        if currentWord not in dict:
            # Create new entry in dictionary
            dict[currentWord] = {nextWord: 1}
        else:
            # Current word already in dictionary
            allNextWords = dict[currentWord]

            if nextWord not in allNextWords:
                # Add new text state
                dict[currentWord][nextWord] = 1

            else:
                # Already exists, just increment
                dict[currentWord][nextWord] = dict[currentWord][nextWord] + 1

    return dict

def updateFile(filename, dictionary):
    file = open(filename, "w")
    json.dump(dictionary, file)
    file.close()
