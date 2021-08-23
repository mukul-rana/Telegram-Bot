
from win10toast import ToastNotifier
import random

file = open("files\\curi.txt","r")
c = (file.read()).split("\n")
c = c[1:]
c.remove('')
topic = random.choice(c).strip()  +  "\n\nand " + str(len(c)-1) + " more tasks."


print(c)

curi = ToastNotifier()
curi.show_toast("Curiousity",topic,duration=5)


file = open("files\\todo.txt","r")
c = (file.read()).split("\n")
c = c[1:]
c.remove('')
todo = random.choice(c).strip() + "\n\nand " + str(len(c)-1) + " more tasks."
print(c)

toast2 = ToastNotifier()
toast2.show_toast("Mukul you have some pending tasks",todo,duration=5)

