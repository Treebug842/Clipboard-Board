import pickle
import tkinter as tk

editMode = 0
currentFrame = 1

root = tk.Tk()

buttonTitles = []
buttonData = []

root.title("Clipboard Board")
root.geometry("600x300")
# root.iconbitmap("lib/icon.ico")

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
frame4 = tk.Frame(root)

def changeFrame(framenumber):
	global currentFrame
	exec(f"frame{currentFrame}.grid_forget()")
	exec(f"frame{framenumber}.grid(row=2, column=0, columnspan=11)")
	currentFrame = framenumber

frame1Button = tk.Button(root, text="1", font='Helvetica 10 bold', command=lambda: changeFrame(1)); frame1Button.grid(row=0, column=8)
frame2Button = tk.Button(root, text="2", font='Helvetica 10 bold', command=lambda: changeFrame(2)); frame2Button.grid(row=0, column=9)
frame3Button = tk.Button(root, text="3", font='Helvetica 10 bold', command=lambda: changeFrame(3)); frame3Button.grid(row=0, column=10)
frame4Button = tk.Button(root, text="4", font='Helvetica 10 bold', command=lambda: changeFrame(4)); frame4Button.grid(row=0, column=11)

def editClick():
	global editMode
	editMode = 1 if editMode == 0 else 0

editButton = tk.Button(root, text="⚙️", font='Helvetica 14 bold', command=editClick); editButton.grid(row=0, column=0)
title = tk.Label(root, text="Clipboard Board", font='Helvetica 16 bold'); title.grid(row=0, column=6)


class createButtons:
	def __init__(self, frame, number):
		self.frame = frame
		self.number = number

		
		createCMD = f"self.button = tk.Button({frame}, text='', width=18, height=2, command=lambda: createButtons.click({number}))"
		exec(createCMD)





	@staticmethod
	def click(number):
		print(f"Button {number} has been clicked")




for i in range(1, 25):
	command1 = f"button{i} = createButtons('frame1', {i})"
	exec(command1)

for i in range(25, 49):
	command1 = f"button{i} = createButtons('frame2', {i})"
	exec(command1)

for i in range(49, 73):
	command1 = f"button{i} = createButtons('frame3', {i})"
	exec(command1)

for i in range(73, 97):
	command1 = f"button{i} = createButtons('frame4', {i})"
	exec(command1)

count = 1

for i in range (0, 4):
	for x in range(1, 7):
		for y in range(1, 5):
			cmd = f"button{count}.button.grid(row={x}, column={y})"
			exec(cmd)
			count += 1







frame1.grid(row=2, column=0, columnspan=11)
root.mainloop()