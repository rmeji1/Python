import os, time 
import fnmatch

startDir = "fortune1" ;
fileList = [] ;
#print("starting");
def traverse(start_dir) :
	for dirPath, dirs, files in os.walk(start_dir):
		for singleFile in files:
			if fnmatch.fnmatch(singleFile, "*txt") or fnmatch.fnmatch(singleFile, "*log"):
				absPath = os.path.join(dirPath, singleFile) ;
				f = open(absPath) ;
				f = f.read();
				mDate = time.ctime(os.path.getmtime(absPath));
				size = os.path.getsize(absPath);
				fileList.append((absPath,f,mDate,size)) ;
		print(fileList) ;

traverse(startDir);
