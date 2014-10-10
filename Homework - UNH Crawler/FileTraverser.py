import os, time 
import fnmatch
import pickle

startDir = "fortune1" ;
fileList = [] ;
#print("starting");
def traverse(start_dir) :
	for dirPath, dirs, files in os.walk(start_dir):
		for singleFile in files:
			if fnmatch.fnmatch(singleFile, "*txt") or fnmatch.fnmatch(singleFile, "*log"):
				absPath = os.path.join(dirPath, singleFile) ;
				of = open(absPath) ;
				f = of.read() ;
				of.close() ;
				mDate = time.ctime(os.path.getmtime(absPath)) ;
				size = os.path.getsize(absPath);
				fileList.append((absPath,f,mDate,size)) ;
		print(fileList) ;
	rawData = open("raw_data.pickle", "wb") ;
	pickle.dump(fileList, rawData) ;
	rawData.close() ;
	
traverse(startDir);
