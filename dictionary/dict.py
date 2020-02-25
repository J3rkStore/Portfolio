import json
import difflib

""" instead of difflib.get_close_matches() you can use:
from difflib import SequenceMatcher
SequenceMatcher(None, 'rainn', 'rain').ratio()"""

data = json.load(open('dictionary\data.json')) #must be changed to wherever data.json is saved

def translate(word):   
    if word in data:
        return data[word]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        closest_words = difflib.get_close_matches(word, data, 10, 0.75)
        word_dex = 0
        #print('similar words: ' + str(closest_words))
        if closest_words == []:
            return 'I\'m sorry but that word does not resemble a real word.'
        else:
            for i in range(len(closest_words)):
                #print('word dex: ' + str(word_dex))
                closest_word = str(closest_words[word_dex])
                message = input('That word is not in the dictionary.  Perhaps you are bad at speling?  Did you mean "' + closest_word + '"? Type "yes" for definition. ')
                if message.lower() == 'yes':
                    return data[closest_word]
                    break
                elif word_dex >= len(closest_words) - 1:
                    return 'okay then.'
                else:
                    word_dex += 1
                

word = input('Enter word: ')

output = translate(word.lower())

for item in output:
    if type(output) == str:
        print(output)
        break
    else:
        print(item)