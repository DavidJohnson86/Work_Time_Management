#------------------------------------------------- MessageBox Methods ------------------------------------------------- 
from Tkinter import*
import tkMessageBox
					
def single(title, message) :
	tkMessageBox.showwarning(title, message)
		
def getdata(ShowItems):
	'''This method prints the values what user added'''	
	tkMessageBox.showwarning("Az alabbi adatokat adta meg: ",ShowItems)
	return
		
def yesorno():
	tkMessageBox.askyesno("FIGYELEM !!!!", "Az osszes adat elvesz biztosan torlod?")