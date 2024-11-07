from tkinter import *
#imported

"""
Purpose:Develop an app for the purpose of plotting dot graphs of similarities
	given any 2 different DNA/RNA/Protein sequences with user interface.

Requirements:    1.Uploading two different sequences into the app from files.
		 2.Using matplotlib for better visualizing.
"""

def button_file_clicked():
	from fastq_to_fasta import read_sequences
	x = str(file.get())
	y = bool(fasta.get())
	if x=="":
		return None
	else:
		return read_sequences(x,y)
	""" When clicked; file browser will be opened
	    then sequence file will be loaded into app."""

def button_plot_clicked():
	check_file=button_file_clicked()
	if check_file is not None:
		try:
			x=str(check_file[0])
			y=str(check_file[1])
			error.set("File name")
		except:
			error.set("Input file must have at least 2 sequences!!!")
			return None
	else:
		x = str(seqx.get())
		y = str(seqy.get())
	z = int(window.get())
	t = int(threshold.get())
	plotgraph(x,y,z,t)
	""" When clicked; graph will be plotted with the
	    given sequence files."""

def button_exit_clicked():
	from matplotlib.pyplot import close
	close('all')
	main.destroy()
	""" When cliked; app will be killed."""

def button_view_clicked():
	""" When clicked; graph will be maximized."""
	pass

def button_info_clicked():
	""" When clicked; info on screen will be appear."""
	pass

def plotgraph(seqx="CAT",seqy="SITTING",window=1,threshold=1):
	def delta(x,y): return 0 if x == y else 1
	def M(seq1,seq2,i,j,k): return max(delta(x,y) for x,y in zip(seq1[i:i+k],seq2[j:j+k])) # or sum with a threshold
	def makeMatrix(seq1,seq2,k): return [[M(seq1,seq2,i,j,k) for j in range(len(seq2)-k+1)] for i in range(len(seq1)-k+1)]

	def dotplot2(seqx, seqy, window, threshold=1):
		import numpy as np
		import matplotlib.pyplot as plt

		M = np.array(makeMatrix(seqx,seqy,window))

		dotplot=plt.imshow(M, cmap='binary_r')

		if len(seqx) > 50 or len(seqy) > 50:
			plt.tick_params(top=False, labeltop=False, bottom=False, labelbottom=False, left=False, labelleft=False)
		else:
			plt.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)

		xt=plt.xticks(np.arange(len(list(seqx)))+.5,list(seqx))
		yt=plt.yticks(np.arange(len(list(seqy)))+.5,list(seqy))
		plt.show()

		# Drawing inside of the APP. (not worked)
		"""
		from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
		from matplotlib.figure import Figure

		fig = Figure(figsize = (3, 3),dpi = 100)
		canvas = FigureCanvasTkAgg(fig, master=main)
		canvas.draw()

		# placing the canvas on the Tkinter window
		canvas.get_tk_widget().grid(row=2,column=2)

		# creating the Matplotlib toolbar

		toolbar = NavigationToolbar2Tk(canvas,main)
		toolbar.update()

		# placing the toolbar on the Tkinter window
		canvas.get_tk_widget().grid(row=4,column=2)
		"""

	dotplot2(seqx,seqy,window,threshold=1)
	"""When clicked; graph will be plotted"""

#main frame
main=Tk()
#main title
main.title("Dot Plotter APP")

red="#ff6b6b"
black="#000000"
yellow="#e0af46"

seqx=StringVar()
seqy=StringVar()
window=IntVar()
threshold=IntVar()
file=StringVar()
fasta=BooleanVar()
error=StringVar()

class App: #Tkinter things are here.

	# Row and Column Configurations.
	for _ in range(4):
		main.columnconfigure(_, weight=1)
		main.rowconfigure(_, weight=1)

	# Sequence1 entry widget
	dot_seqx_text= Label(main, text="Sequence")
	dot_seqx_text.grid(row=0, column=1, stick="s")
	dot_entry_seqx = Entry(main, textvariable=seqx)
	dot_entry_seqx.grid(row=1,column=1, stick="n")

	# Sequence2 entry widget
	dot_seqy_text= Label(main, text="Sequence")
	dot_seqy_text.grid(row=0, column=2, stick="s")
	dot_entry_seqy = Entry(main, textvariable=seqy)
	dot_entry_seqy.grid(row=1,column=2, stick="n")

	# Window Entry widget
	dot_window_text= Label(main, text="window")
	dot_window_text.grid(row=2, column=1, stick="nsw")
	window.set("1")
	dot_entry_window = Entry(main, textvariable=window, width=4)
	dot_entry_window.grid(row=2,column=0)

	# Threshold Entry widget
	dot_threshold_text= Label(main, text="threshold")
	dot_threshold_text.grid(row=3, column=1, stick="nsw")
	threshold.set("1")
	dot_entry_threshold = Entry(main, textvariable=threshold, width=4)
	dot_entry_threshold.grid(row=3,column=0)

	# File name entry widget
	error.set("File name")
	dot_file_text= Label(main, textvariable=error)
	dot_file_text.grid(row=0,column=0, stick="nsw")
	dot_file_entry= Entry(main, textvariable=file, width=10)
	dot_file_entry.grid(row=0,column=0,stick="nw")

	# Checkbutton widget
	dot_is_fasta_text= Label(main, text="file is fasta")
	dot_is_fasta_text.grid(row=0,column=1,stick="new")
	fasta.set(1)
	dot_is_fasta_check= Checkbutton(main, variable=fasta)
	dot_is_fasta_check.grid(row=0,column=1,stick="nw")

	# Dot Plotter button
	dot_plotter_button = Button(master=main,command=button_plot_clicked,text="Dot Plot",bg=yellow)
	dot_plotter_button.grid(row=2,column=2)

	# Exit button
	button_exit = Button(main, text="X", command=button_exit_clicked, bg=red)
	button_exit.grid(row=0,column=3,stick="ne")

	# Credits.
	label_bot = Label(main, text="Made by Yusuf I.UNAL")
	label_bot.grid(row=4,column=2, stick="s")

#main window size
main.geometry("480x260")
#main looper
main.mainloop()
