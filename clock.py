import datetime
import time
from os import system


while True:
	s = "# The real time clock!\n\nEver wanted to know what the time is? Well, your journey is about to end!\n\n**The time is "
	t = datetime.datetime.now().strftime('%b %d, %Y, %H:%M') + "**"

	with open("readme.md", "w") as f:
		f.write(s + t)
		
	system("git add .")
	system("git commit -m \"Update time\"")
	system("git push origin master")
	time.sleep(600)