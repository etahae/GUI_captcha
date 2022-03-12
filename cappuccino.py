from captcha.image import ImageCaptcha
from random import sample
from tkinter import messagebox, Label, Entry, Tk, PhotoImage

liist = "abcdefghijklmnopqrstuvwxzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def main():

	image = ImageCaptcha(width = 250, height = 200)

	captchatext = "".join(sample(liist, 5))

	data = image.generate(captchatext)

	image.write(captchatext, "captcha.png")

                        #################################################
	win = Tk()
	
	ws = win.winfo_screenwidth()
	hs = win.winfo_screenheight()
	
	xx = 250
	yy = 230
	
	x = ws/2 - xx/2
	y = hs/2 - yy/2

	win.geometry("%dx%d+%d+%d" % (xx, yy, x, y))	

	win.resizable(0, 0)

	win.title("captcha")

	capochino = PhotoImage(file='captcha.png')

	Label(win, image = capochino).place(x = 0, y = 0)

	def message():
		global msg
		msg = messagebox.askquestion(title = "captcha", message = "Your captcha session has expired !\nDo you want to retry ?")
		if msg == "no":
			win.destroy()
		else:
			win.destroy()
			main()

	win.after(30000, message)
	
	entry = Entry(width = 10, bd = 3, justify = "center")
	
	def getinput(click):
		e = entry.get()
		if e == captchatext :
			win.destroy()
			
			# here goes the followed program after captcha verification !
			
			
			
			
			# here ends
			
		else :
			mssg = messagebox.askquestion(title = "captcha", message = "Your captcha verification is wrong !\nDo you want to retry ?")
			if mssg == "yes":
				win.destroy()
				main()
			else :
				win.quit()
			
	win.bind("<Return>", getinput)
	
	entry.place(x = 80, y = 203)
	
	win.mainloop()

main()
