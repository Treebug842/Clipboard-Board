import pickle
import tkinter as tk

editMode = 0
currentFrame = 1

root = tk.Tk()

buttonTitles = []
buttonData = []

with open("data", 'rb') as file:
	buttonTitles, buttonData = pickle.load(file)

# Clear Variables
buttonTitles = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
buttonData = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

def save_data():
	with open("data", 'wb') as file:
		pickle.dump([buttonTitles, buttonData], file)

root.title("Clipboard Board")
root.geometry("570x300")
# root.iconbitmap("lib/icon.ico")

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
frame4 = tk.Frame(root)
bFrame = tk.Frame(root)

def changeFrame(framenumber):
	global currentFrame
	exec(f"frame{currentFrame}.grid_forget()")
	exec(f"frame{framenumber}.grid(row=2, column=0, columnspan=11)")
	exec(f"frame{currentFrame}Button.configure(bg='SystemButtonFace')")
	exec(f"frame{framenumber}Button.configure(bg='red')")
	currentFrame = framenumber


frame1Button = tk.Button(bFrame, text="1", font='Helvetica 12 bold', height=1, width=2, command=lambda:changeFrame(1)); frame1Button.grid(row=0, column=0)
frame2Button = tk.Button(bFrame, text="2", font='Helvetica 12 bold', height=1, width=2, command=lambda:changeFrame(2)); frame2Button.grid(row=0, column=1)
frame3Button = tk.Button(bFrame, text="3", font='Helvetica 12 bold', height=1, width=2, command=lambda:changeFrame(3)); frame3Button.grid(row=0, column=2)
frame4Button = tk.Button(bFrame, text="4", font='Helvetica 12 bold', height=1, width=2, command=lambda:changeFrame(4)); frame4Button.grid(row=0, column=3)

def editClick():
	global editMode
	if editMode == 1:
		editMode = 0
		editButton.configure(bg="SystemButtonFace")
	elif editMode == 0:
		editMode = 1
		editButton.configure(bg="cyan")

editButton = tk.Button(root, text="⚙️", font='Helvetica 14 bold', command=editClick); editButton.grid(row=0, column=0, sticky=tk.W)
title = tk.Label(root, text="Clipboard Board", font='Helvetica 16 bold'); title.grid(row=0, column=6)
bFrame.grid(row=0, column=8, columnspan=4)


class createButtons:
	def __init__(self, frame, number):
		self.frame = frame
		self.number = number
		createCMD = f"self.button = tk.Button({frame}, text='{buttonTitles[(number - 1)]}', font='Helvetica 14 bold', width=11, height=1, command=lambda: createButtons.click({number}))"
		exec(createCMD)


	@staticmethod
	def editEntry(buttonNumber):
		editBox = tk.Tk()
		editBox.title(f"Edit Button {buttonNumber}")
		editBox.geometry("300x300")

		titleLabel = tk.Label(editBox, text=f"Edit Title", font='Helvetica 10 bold'); titleLabel.pack(pady=3)
		titleBox = tk.Entry(editBox, width=20); titleBox.pack(pady=3)
		dataLabel = tk.Label(editBox, text="Edit Data", font='Helvetica 10 bold'); dataLabel.pack(pady=3)
		dataBox = tk.Text(editBox, height=10, width=30); dataBox.pack(pady=3)

		editBox.mainloop()

	@staticmethod
	def copyToClipboard(buttonNumber):
		print("Copied to clipboard")



	@staticmethod
	def click(number):
		global editMode
		if editMode == 1:
			createButtons.editEntry(number)
		elif editMode == 0:
			createButtons.copyToClipboard(number)





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
frame1Button.configure(bg="red")
root.mainloop()
