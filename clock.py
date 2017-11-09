import datetime
import time
from os import system

t1 = 0
while True:
	s = "# The real time clock!\n\nEver wanted to know what the time is? Well, your journey is about to end!\n\n**The time is "
	t = datetime.datetime.now().strftime('%b %d, %Y, %H:%M') + "**"
	if t1 is not 0:
		if t1 is not t:
			with open("readme.md", "w") as f:
				f.write(s + t)
		
	system("git add .")
	system("git commit -m \"Update time\"")
	system("git push origin master")
	t1 = t
	time.sleep(1)
	