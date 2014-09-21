import sys, os, datetime, fileinput, shutil, commands

wd = os.getcwd()
lwd = os.path.join(wd,'scripts')

lastrun = open('lastrun.dat', 'r+')
lastrunmemory = lastrun.readlines()
lastrun.close()
def getFiles():
	files = []
	for file in os.listdir(lwd):
		if file.endswith('.py'):
			files.append(file)
	return files

def getFileLastrun(file_):
	try:
		for line in lastrunmemory:
			if file_ in line:
				date = line.split(",")[1].replace('\n','')
				date = datetime.datetime.strptime(date, ' %Y-%m-%d %H:%M:%S')
				return date
			else:
				pass
		return None
	except ValueError:
		print 'seems none for ', file_
		return None
def getFileSchedule(file_):
	splits = file_.split('-')
	for split in splits:
		if 's.py' in split:
			schedule = split.replace('s','').replace('.py',' ')
			schedule = int(schedule)
			schedule = datetime.timedelta(seconds=schedule)
			return schedule
	return None

def fileRunner(file_, lastrun, schedule):
	if schedule == None or lastrun == None or lastrun + schedule <= datetime.datetime.now():
		output = commands.getoutput('ps aux')
		if file_ not in output:
			os.system('python '+ os.path.join(lwd,file)+ ' >>' + os.path.join(wd,'logs',file)+'.log' + '&')		
			print 'running ', file.replace('py','')
			return True
		else:
			return False
	else:
		return False

def lastrunUpdate(changedfiles, unchangedfiles):
	tmpfile = open('lastruntmp.dat', 'w')
	lines=[]
	for file in unchangedfiles:
		line = file + ' , ' + str(getFileLastrun(file)) + '\n'
		lines.append(line)
	for file in changedfiles:
		line = file + ' , ' + str(datetime.datetime.now().replace(microsecond=0)) + '\n'
		lines.append(line)
	for line in lines:
		tmpfile.write(line)
	tmpfile.close()
	shutil.move('lastruntmp.dat', 'lastrun.dat')
	

files = getFiles()
unchangedfiles = []
changedfiles = []
for file in files:
	lastrun = getFileLastrun(file)
	schedule = getFileSchedule(file)
	if fileRunner(file, lastrun, schedule):
		changedfiles.append(file)
	else:
		unchangedfiles.append(file)
lastrunUpdate(changedfiles, unchangedfiles)
