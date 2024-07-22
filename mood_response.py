import re

def mood_response(text):
    happy = r"good|happy|well"
    sad = r"(sad|bad|mad)"
    neutral = r"(fine|ok|comme ci comme ca)"
    var = re.search(happy, text)
    var2 = re.search(sad, text)
    var3 = re.search(neutral, text)
    if var:
        print("u rock keep it up")
    elif var2:
        print("don worry it gets better")
    elif var3:
        print("get off the fence already")
    else:
        print("your mood is not valid")

