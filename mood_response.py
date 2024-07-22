import re

def mood_response(text):
    text = input("How are you feeling today?: ")
    happy = r"(good|happy|well|fine)"
    sad = r"(sad|bad|mad)"
    neutral = r"(fine|ok|comme ci comme ca)"
    re.search(happy, sad, neutral, text)
    if happy in text:
        print("u rock keep it up")
    elif sad in text:
        print("don worryy it gets better")
    elif neutral in text:
        print("get off the fence already")

mood_response()