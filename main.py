import pickle
import pyperclip
import tkinter as tk

editMode = 0
currentFrame = 1

root = tk.Tk()

buttonTitles = []
buttonData = []

with open("data", 'rb') as file:
	buttonTitles, buttonData = pickle.load(file)

# Clear Variables
# buttonTitles = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
# buttonData = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

def save_data():
	with open("data", 'wb') as file:
		pickle.dump([buttonTitles, buttonData], file)

root.title("Clipboard Board")
root.geometry("562x256")
# root.iconbitmap("lib/icon.ico")

mainwindow = tk.Frame(root); mainwindow.pack(anchor=tk.CENTER)

frame1 = tk.Frame(mainwindow)
frame2 = tk.Frame(mainwindow)
frame3 = tk.Frame(mainwindow)
frame4 = tk.Frame(mainwindow)
bFrame = tk.Frame(mainwindow)

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

editButton = tk.Button(mainwindow, text="⚙️", font='Helvetica 13 bold', command=editClick); editButton.grid(row=0, column=0, sticky=tk.W)
title = tk.Label(mainwindow, text="Clipboard Board", font='Helvetica 16 bold'); title.grid(row=0, column=6)
bFrame.grid(row=0, column=8, columnspan=4)


class createButtons:
	def __init__(self, frame, number):
		self.frame = frame
		self.number = number
		createCMD = f"self.button = tk.Button({frame}, text='{buttonTitles[(number - 1)]}', font='Helvetica 14 bold', width=11, height=1, command=lambda: createButtons.click({number}), relief='solid', borderwidth=1)"
		exec(createCMD)



	@staticmethod
	def editEntry(buttonNumber):
		editBox = tk.Tk()
		editBox.title(f"Edit Button {buttonNumber}")
		editBox.geometry("300x400")

		titleLabel = tk.Label(editBox, text=f"Edit Title", font='Helvetica 10 bold'); titleLabel.grid(row=0, column=0, columnspan=2)
		titleBox = tk.Entry(editBox, width=20); titleBox.grid(row=1, column=0, columnspan=2)
		titleBox.insert(0, buttonTitles[buttonNumber - 1])
		dataLabel = tk.Label(editBox, text="Edit Data", font='Helvetica 10 bold'); dataLabel.grid(row=2, column=0, columnspan=2)
		dataBox = tk.Text(editBox, height=10, width=40); dataBox.grid(row=3, column=0, columnspan=2, padx=20)
		dataBox.insert(tk.INSERT, buttonData[buttonNumber - 1])

		def saveEntry(buttonNumber):
			global buttonTitles
			entry = titleBox.get()
			buttonTitles[buttonNumber - 1] = entry
			exec(f"button{buttonNumber}.button.configure(text='{entry}')")

			global buttonData
			entry = dataBox.get("1.0", "end-1c")
			buttonData[buttonNumber - 1] = entry
			save_data()
			# Dosnt work

			editBox.destroy()
			editClick()

		def cancelEntry():
			editClick()
			editBox.destroy()


		saveButton = tk.Button(editBox, text="Save", font='Helvetica 14 bold', command=lambda:saveEntry(buttonNumber), padx=10); saveButton.grid(row=5, column=0, sticky=tk.E)
		cancelButton = tk.Button(editBox, text="Close", font='Helvetica 14 bold', command=cancelEntry()); cancelButton.grid(row=5, column=1, sticky=tk.W)

		editBox.mainloop()

	@staticmethod
	def copyToClipboard(buttonNumber):
		pyperclip.copy(buttonData[buttonNumber - 1])
		print(buttonData[buttonNumber - 1])



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
mainwindow.mainloop()
