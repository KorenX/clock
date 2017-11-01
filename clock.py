import datetime
from os import system

s = "# The real time clock!\n\nEver wanted to know what the time is? Well, your journey is about to end!\n\n**The time is "
time = datetime.datetime.now().strftime('%b %d, %Y, %H:%M') + "**"

with open("readme.md", "w") as f:
	f.write(s + time)
	
system("git add .")
system("git commit -m \"Update time\"")
system("git push origin master")