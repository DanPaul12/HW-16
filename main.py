import mood_response
import textutils as tu

mood = input("How are you feeling today? ")
print(mood_response.mood_response(mood))

command = input("Would you like to 1. reverse or 2. capitalize your string? Enter 1 or 2: ")
if command == 1:
    string = input("What is your string?")
    print(tu.reverse_string(string))
elif command == 2:
    string = input("What is your string?")
    print(tu.capitalize_string(string))
