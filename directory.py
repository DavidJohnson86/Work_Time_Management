#------------------------------------------------- Directory Operations ------------------------------------------------- 

import os

def fileexist(param,path):
		'''This methods returns True if the file in the home
		directory exists. example os.getcwd() - The actual 
		directory of the python.exe file. + sub is the 
		subdirectory in this case. C:\Docand sett\User\sub '''
		os.chdir(path) 
		act=os.getcwd() +  '\\' + param 
		a=os.path.exists(act)
		return a
		
		
def fileall(param,path):
		'''This method is waiting for a list parameter for 
		input (the list of subdirectory names) if the subdirectory
		exists it will return an array included with the name of 
		existing subdirectories'''		
		i=1
		MonthList=[]
		length = len(param) 
		for i in range (1, length)  :
			if fileexist(param[i],path) == 1 :
				MonthList.append(param[i])
	        return MonthList
			

			
def filewrite(File,Data):
		''' File Write function '''
		File = open( File , 'a')
		File.write(Data)
		File.close()
		return
	
	
		