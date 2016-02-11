#!/usr/bin/python
# -*- coding: utf-8 -*-

# PEP8 QUALITY CHECK THE LINK BELOW FOR MORE INFORMATION :
# https://www.python.org/dev/peps/pep-0008/
# http://pep8online.com/

"""
==============================================================================
                          Work Time Management System
==============================================================================
                            OBJECT SPECIFICATION
==============================================================================
$ProjectName: $
$Source: Work_Time.py
$Revision: 1.1 $
$Author: David Szurovecz $
$Date: 2016/02/08 16:41:32CEST $
$Name:  $
Improvements : .Set functions removed (redundant code)
................Training function added
................More Data Indenpendency
................Added safe input method
................Added ValueError exception for integer types
................Added Actual Month Recognition Functions
................Added new function menufour month datas
................
................
Needed to fix : When asking for input datas 
............... Needed to ask about leaving date too.
............... Need an encrypt function for files
................Color highlights for hours
................
(Bug)fixes:.....When viewing training menu  hour datas now expanded with zeros
................When adding more input data in menu one and hitting next button
................multiple time the window wont crash.
............... More redundant code.
................Menu oriented sequence.
................Working hours algorithm is perfect now.
................
...............
History:........2015.11.23 - New Listing View on Menu 2
................2016.02.02 - Text format instead of Listbox nice tabulated rows
................2016.02.04 - Now Txt File is generating too for future printing
................2016.02.10 - Now it shows your current standing in requried hours
................2016.02.11 - Now Handle Years not just months
============================================================================
"""

from Tkinter import Tk, Frame, BOTH, Label, Button, Entry, Scrollbar, \
    RIGHT, Y, Text, TOP, NONE, END, W, LEFT
from PIL import Image, ImageTk
import os
import re
import sys
import time
import directory
import dates
import messagebox
import datetime
import calendar
import GUI

PATH = os.getcwd()
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime(
    '%Y. %m. %d. %H:%M:%S')
x = ' '

main_title = 'Munkaido Nyilvantarto Rendszer'
main_button1_title = 'Ido adatainak megadasa'
main_button2_title = 'Ido adatok attekintese'
main_button3_title = 'Ido adatok torlese'
main_button4_title = 'Elozo havi idoadatok'
main_button5_title = 'Kilepes'
menuone_button1_title = 'Adja meg a Datumot: '
menuone_button2_title = 'Adja meg a Belepes idejet : '
menuone_button3_title = 'Adja meg a Kilepes idejet : '
menuone_button4_title = 'Ebedeltel ? (i/n): '
menufour_title = ' Dolgozo idoadatai'
seperatesign = ( 
    "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
    "- - - - - - - - - - - - - - - - - - - - - - -\n" )
worktime_report1 = (
    "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
    "- - - - - - - - - - - - - - - - - - - - - - -"
    "\nIdo kimutatasi Riport ...Datum : %s" 
    "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
    "- - - - - - - - - - - - - - - - - - - - - - -" 
    "\nDatum / Belepes ideje             Datum / Kilepes ideje                Munkaora"
    "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
    "- - - - - - - - - - - - - - - - - - - - - - -\n") %(st)
warempty_one = 'Nem sikerult megnyitni.'
warempty_two = 'Nem letezik ilyen fajl.'

ListOfMainButtons = [
            main_button1_title,
            main_button2_title,
            main_button3_title,
            main_button4_title,
            main_button5_title,
            ]
			
months = [
            'None','januar', 'februar',
            'marcius','aprilis', 'majus',
            'junius','julius', 'augusztus',
            'szeptember', 'oktober','november',
            'december',
            ]
Years = [
            '2010', '2011', '2012',
            '2013', '2014', '2015',
            '2016', '2017', '2018',
            '2019',
            ]
			
			
class Menu:

    def __init__(self, master):
        '''Main Menu container Items'''
        self.MainMenuContainer = Frame(master)
        self.MainButtonContainer = Frame(master)
        self.MenuFourContainer = Frame(master)
        self.MenufourYearsContainer = Frame(master)
        root.title(main_title)
        self.initUI()

    def initUI(self):
        
        self.image('MainPic.jpg')
        Label(self.MainMenuContainer, 
              text=main_title,
              font=15,
              padx=10,
              pady=10).pack()
        self.MainMenuContainer.pack(
            fill=BOTH, expand=1)
        self.MainButtonContainer.pack()
        self.MenufourYearsContainer.pack() 
        Label(self.MainMenuContainer, 
		      text=dates.date()).pack()

        CommandOfMainButtons = [
            self.menu_one,
            self.menu_two,
            self.menu_three,
            self.menu_four,
            self.menu_five,
            ]

        GUI.ButtonCreator(self.MainButtonContainer, 
                          ListOfMainButtons,
                          CommandOfMainButtons, 5)

      

#  **************SUB MENU METHODS***************

    def menu_one(self):
        run.menuone()

    def menu_two(self):
        os.chdir (os.getcwd() + '\\' + str(dates.actualyear()))
        File = Month = dates.actualmonth(months)
        run.showdata(
		    Month.title() + 
		    ' honap idoadatai', File,
            ' \nLedolgozott napok szama: \t%s')

    def menu_three(self):
        messagebox.yesorno()

    def menu_four(self):
        self.destroy_mainbutton()
        self.menufour()

    def menu_five(self):
        root.destroy()

          
    def quit_menutwo(self):
        self.f4.destroy()

    def quit_menuone(self):
        self.MenuOneContainer.destroy()

    def quit_menufour(self):
        os.chdir(PATH) 
        self.MainMenuContainer.destroy()
        self.MenufourYearsContainer.destroy()
        run = Menu(root)

    def act(self, Month):
        File = Month
        run.showdata(
            Month.title() + ' honap idoadatai',
			File,'\nLedolgozott napok szama : \t%s')

    def setdata(self, data):
        data = int(data.get())
        return data

    def destroy_mainbutton(self):
        self.MainButtonContainer.destroy()

#  **************MENU METHODS***************

    def menuone(self):
        '''Menu one waiting for user input and store the data'''
        Ido = Tk()
        self.MenuOneContainer = Ido
        Label(self.MenuOneContainer,
              text=menuone_button1_title).grid(row=4, sticky=W)
        Label(self.MenuOneContainer,
              text=menuone_button2_title).grid(row=5, sticky=W)
        Label(self.MenuOneContainer,
              text=menuone_button3_title).grid(row=6, sticky=W)
        Label(self.MenuOneContainer,
              text=menuone_button4_title).grid(row=7, sticky=W)
        self.date = Entry(
		    self.MenuOneContainer, bd=5, width=14)
        self.date.grid(row=4, column=1, sticky=W)
        self.in_hour = Entry(
            self.MenuOneContainer,
            bd=5, width=5)
        self.in_hour.grid(row=5, column=1, sticky=W)
        self.in_min = Entry(
            self.MenuOneContainer, bd=5, width=5)
        self.in_min.grid(row=5, column=1)
        self.out_hour = Entry(
		    self.MenuOneContainer, bd=5, width=5)
        self.out_hour.grid(row=6, column=1, sticky=W)
        self.out_min = Entry(
		    self.MenuOneContainer, bd=5, width=5)
        self.out_min.grid(row=6, column=1)
        self.Meal = Entry(
		    self.MenuOneContainer, bd=5, width=14)
        self.Meal.grid(row=7, column=1, sticky=W)
        self.b5 = Button(
		    self.MenuOneContainer, text='Vissza',
            height=1, width=20,
            command=self.quit_menuone).grid(row=28)
        self.b6 = Button(
		    self.MenuOneContainer, text='Tovabb',
            height=1, width=20,command=self.print_write).grid(row=28,
                column=1)

    def menufour(self):
        '''This function checks if the The Year is available 
        in the current folder'''
        Label(self.MenufourYearsContainer, text='Éves Adatok ', font=12,
              padx=10, pady=10).pack(side=TOP)
        self.ListOfFiles = directory.fileall(Years,PATH)
        length = len(self.ListOfFiles)
        for i in range(0, length):
            self.menu_four_sub_one(i)
        Button(self.MenufourYearsContainer, text='Vissza', height=1,
               width=20, command=self.quit_menufour).pack()
	   

    def menu_four_sub_one(self, i):
        '''It create a button for the file what its found in the list'''
        self.Month = self.ListOfFiles[i]
        Button(self.MenufourYearsContainer, text=self.Month, height=1,
               width=20, command=lambda : \
               self.menu_four_sub_two(self.ListOfFiles[i])).pack()
			   
    def menu_four_sub_two(self,i):
        '''It creates buttons for the available month files 
        from the current year directory '''
        self.MenufourYearsContainer.destroy()
        self.ListOfFiles = directory.fileall(months,PATH + '\\' + i)
        length = len(self.ListOfFiles)
        Label(self.MainMenuContainer, text='Havi Adatok ', font=12,
              padx=10, pady=10).pack()
        for i in range(0, length):
            self.Buttonpointer(i)
        Button(self.MainMenuContainer, text='Vissza', height=1,
               width=20, command=self.quit_menufour).pack()
			
    def Buttonpointer(self, i):
        '''It create a button for the file what its found in the list'''
        self.Month = self.ListOfFiles[i]
        Button(self.MainMenuContainer, text=self.Month, height=1, width=20,
               command=lambda: self.act(self.ListOfFiles[i])).pack()
			   
#  **************SYSTEM METHODS***************

    def print_write(self):
        '''This method sets the datas calls a calculate
         method and calls a messagebox data'''
        try:
            self.__in_hour = self.setdata(self.in_hour)
            self.__in_min = self.setdata(self.in_min)
            self.__out_hour = self.setdata(self.out_hour)
            self.__out_min = self.setdata(self.out_min)
            self.date = self.date.get()
            self.Meal = self.Meal.get()
            if self.__in_hour not in range(0, 24) or self.__out_hour \
                not in range(0, 24) or self.__in_min not in range(0,
                    60) or self.__out_min not in range(0, 60) \
                or self.Meal != 'i' and self.Meal != 'n':
                messagebox.single('HIBA', 'A bevitt adatok hibasak')
            else:
                self.execute()
        except ValueError:
            messagebox.single('HIBA', 'A bevitt adatok hibasak')

    def printfile(self, File):
	
        ''' p = win32print.OpenPrinter (printer_name)
		job = win32print.StartDocPrinter (p, 1, ("test of raw data", None, "RAW")) 
		win32print.StartPagePrinter (p)
		win32print.WritePrinter (p, "data to print") 
		win32print.EndPagePrinter (p)'''
        act = os.getcwd() + '\\' + File + 'print' 
        os.startfile(act)

    def execute(self):
        ''' This methods only approve the safe input datas'''
        hoursandmins = dates.worktimecalc(
            self.__in_hour,
            self.__in_min,
            self.__out_hour,
            self.__out_min,
            self.Meal)
        self.expandallwithzero(hoursandmins[0], hoursandmins[1])
        Message = 'Datum ' + self.date + '\n' + 'Belepes ideje ' \
            + self.Arrive + '\n' + 'Kilepes ideje ' + self.Out + '\n' \
            + 'Munkaido ' + self.WorkTime
        Data = 'Datum ' + self.date + ' Belepes ' + self.Arrive + 9 * x \
            + self.date + ' Kilepes ' + self.Out + ' Ebed ' + self.Meal \
            + 13 * x + ' Munkaido ' + self.WorkTime
        messagebox.getdata(Message)
        Directory = dates.actualyear()
        os.chdir(os.getcwd() + '\\'+ str(Directory))
        File = dates.actualmonth(months)
        directory.filewrite(File, Data)
        self.MenuOneContainer.destroy()
        run.menuone()

    def expandallwithzero(self, work_time_hour, work_time_min):
        '''it expands the time expression where only 1 digit number found '''
        self.WorkTime = dates.maketimeformat(
		    work_time_hour, work_time_min)
        self.Arrive = dates.maketimeformat(
            self.__in_hour, self.__in_min)
        self.Out = dates.maketimeformat(
		    self.__out_hour, self.__out_min)
        self.date = str(self.date)

    def image(self, nameofpic):
        image = Image.open(nameofpic)
        photo = ImageTk.PhotoImage(image)
        label = Label(self.MainMenuContainer, image=photo)
        label.image = photo
        label.pack()


   # Show Time Datas

    def showdata(
        self, Title,
        Fajl, Days ):
        '''This method i'''
        Fajl= os.getcwd() + '\\' + Fajl
        self.Title = Title
        self.Fajl = Fajl
        IdoFajl = open(Fajl, 'a')
        IdoFajl.seek(0, 2)
        IdoFajlHossz = IdoFajl.tell()
        if IdoFajlHossz == 0L:
            messagebox.single(warempty_one, warempty_two)
            IdoFajl.close()
        else:
            showdata = Tk()
            self.f4 = showdata
            showdata.title(menufour_title)
            scrollbar = Scrollbar(showdata)
            scrollbar.pack(side=RIGHT, fill=Y)
            IdoFajl = open(Fajl, 'r')
            data_hours = data_min = 0
            bejegyzes = 5
            nap = 0

            Label(showdata, text=Title, font='Bold', padx=10,
                  pady=10).pack()
            begin = 0
            # Start to Read from file
            while 1:
                IdoAdatok = IdoFajl.readline()
                Bont_result = re.match('(.*)(Munkaido)\s*(\d+:\d+)',
                        IdoAdatok)
                Datum_result = re.match('(.*)(Datum)\s*(\d+.\d+.\d+)',
                        IdoAdatok)

                whatday = dates.whatday(Datum_result)

                if Bont_result:
                    work_time = Bont_result.group(3)
                    hours = work_time.split(':')[0]
                    mins = work_time.split(':')[1]
                    data_hours += int(hours)
                    data_min += int(mins)

                if IdoAdatok != '':
                    FilePrint = self.Fajl + 'print'
                    if begin == 0:
                        try:
                            os.remove(FilePrint)
                        except WindowsError:
                            pass
                        directory.filewrite(FilePrint, self.Title + '\n'
                                )
                        directory.filewrite(FilePrint, worktime_report1)
                        begin = 1
                    s = re.sub('[DatumBelepesKilepesEbedMunkaIdo]', '',
                               IdoAdatok)

                    if whatday == 0:
                        directory.filewrite(FilePrint, ' MON \t' + s)
                    elif whatday == 1:
                        directory.filewrite(FilePrint, ' TUE \t' + s)
                    elif whatday == 2:
                        directory.filewrite(FilePrint, ' WED \t' + s)
                    elif whatday == 3:
                        directory.filewrite(FilePrint, ' THU \t' + s)
                    elif whatday == 4:
                        directory.filewrite(FilePrint, ' FRI \t' + s)
                    elif whatday == 5:
                        directory.filewrite(FilePrint, ' SAT \t' + s)
                    elif whatday == 6:
                        directory.filewrite(FilePrint, ' SUN \t' + s)

                    bejegyzes = bejegyzes + 1
                    nap = nap + 1
					  
					
                else:
                    requiredmins = (nap*8)*60
                    currentmins = (data_hours *60 + data_min) -requiredmins
                    ShowMin = dates.mintotime(currentmins)
                    
                    
                    if data_min > 60:
                        plus_hours = data_min / 60
                        data_min = data_min % 60
                        data_hours += plus_hours
                    data_hours = dates.ExpandWithZero(data_hours)
                    data_min = dates.ExpandWithZero(data_min)
                    directory.filewrite(FilePrint, '\n' + seperatesign)
                    directory.filewrite(FilePrint,
                            'Osszegzesi informaciok :\n')
                    directory.filewrite(FilePrint,
                            'Havi munkaorak szama :  \t%s:%s'
                            % (data_hours, data_min))
                    directory.filewrite(FilePrint, Days % nap)
                    directory.filewrite(FilePrint,
                            '\nJelenlegi óraszám :  \t%s'
                            % (ShowMin))
					#Create a copy of File					
                    with open (FilePrint) as copy_of_file:
                        file_content = copy_of_file.read()					
					#Create a Testbox for Showing Information
                    Ido_lista = Text(
                        showdata,
                        yscrollcommand=scrollbar.set,
                        width=63,
                        height=20,
                        font='Bold')
                    Ido_lista.pack(
                        side=TOP,
                        fill=NONE,
                        padx=10,
                        pady=10)
                    scrollbar.config(command=Ido_lista.yview)
                    Ido_lista.insert(END, file_content)
                    Next = Button(
                        showdata,text='Tovabb', 
                        height=1,width=20, 
                        command=self.quit_menutwo)
                    Next.pack(
                        side=LEFT,fill=NONE,
                        padx=10, pady=10)
                    Back = Button(
                        showdata, text='Nyomtat',
                        height=1, width=20, 
                        command=lambda : \
                        self.printfile(Fajl))
                    Back.pack(
                        side=LEFT, fill=NONE,
                        padx=10, pady=10)
                    Ido_lista.configure(state='disabled')
                    break
                    IdoFajl.close()


root = Tk()
run = Menu(root)
root.mainloop()