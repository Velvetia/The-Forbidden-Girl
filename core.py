import random
import time

threedots = [".", "..", "..."]
fivedots = [".", "..", "...", "....", "....."]


def beat(dots):
    for i in range(len(dots)):
        print(dots[i])
        time.sleep(1.5)


print("Hello. You don't seem to be around these parts. Mind telling me about yourself?")
time.sleep(7)
print("For starters, what's your name?")
name = str(input())
print("Ahh... so your name is " + name + "...")
time.sleep(2.5)
print("I think it's nice!")
time.sleep(5)
print("So... uh... what's your gender, anyway? I don't want to assume; that's just rude, y'know?")
gender = str(input(
    "*psst! hey! it'll be easier if you use formal names for this instead of 'he' or 'she', so try those!* "))  # There's a better way of doing this, I'm sure. I'm too lazy to figure it out though.

if gender is "female":
    print("Oh, so you're a girl! Heh, it's rare to see one out in the wilderness here, all by your lonesome, no less!")
elif gender is "male":
    print(
        "Ahhh, so you're a boy! Gonna grow up to be tough through and through, like the trees surrounding you, right?")
else:
    time.sleep(1.5)
    beat(threedots)
    print("....What?")
    time.sleep(2.5)
    print("W-whatever. I'll figure it out later, when we get you somewhere safe.")
