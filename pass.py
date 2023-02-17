import random
import tkinter


def mix(string):
    characterList = list(string)
    random.shuffle(characterList)
    return ''.join(characterList)


upperLetter1 = chr(random.randint(65, 90)) #random from A-Z uppercase
upperLetter2 = chr(random.randint(65, 90))

lowerLetter1 = chr(random.randint(97, 122)) #random a-z lowercase
lowerLetter2 = chr(random.randint(97, 122))

digit1 = chr(random.randint(48, 57)) #random 
digit2 = chr(random.randint(48, 57))

punct1 = chr(random.randint(33, 152))
punct2 = chr(random.randint(33, 152))

password = upperLetter1 + upperLetter2 + lowerLetter1 + lowerLetter2 + digit1 + digit2 + punct1 + punct2
password = mix(password)



def label1(root):
    label = tkinter.Label(root, text = "password: " + password)
    label.pack()
    
def Window():
    window1 = tkinter.Tk()
    window1.title("Random Generator")
    label = tkinter.Label(window1, text = "Want to generate a random password?")
    label.pack()
    points = 0
    i = points + 1
    button = tkinter.Button(window1, text = "Generate", command=lambda root = window1: label1(root))
    button.pack()

    window1.mainloop()


print(Window())


