
# http://newsapi.org/v2/top-headlines?country=in&apiKey=8ee9901ff1d24245a324617fbbbda96e

import  requests
from win32com.client import Dispatch
import json

def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)


if __name__ == '__main__':
    speak("News for today.. Let's begin")
    req = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=8ee9901ff1d24245a324617fbbbda96e")
    print(req.text)

    # json converted to python dictionary
    parsed = json.loads(req.text)
    # print(parsed["articles"])

    for article in  parsed["articles"]:
        article_dictionary = dict(article)
        for akey,avalue in article_dictionary.items():

            # print("key: ",key)
            # print("value: ",value)
            if akey == "title":
                print("title: ", article_dictionary[akey])
                speak(article_dictionary[akey])


            if akey == "description":
                print("description: ",article_dictionary[akey])
                speak(article_dictionary[akey])
                speak("Thank for listening...")
                print()



