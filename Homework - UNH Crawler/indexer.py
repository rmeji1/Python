import os, pickle, shelve

# ------------------------------------------------------------------------------
# Function that does the preprocessing
def process_data(pickleFile, shovelFile) :
    f = open(pickleFile,"br");
    mylist = pickle.load(f);
    f.close();
    dict = shelve.open(shovelFile)
    for f in mylist: # get each line from the data_list
        contents = f[1] ;
        contents = contents.replace(',', '');
        contents = contents.replace('.','');
        contents = contents.split();
        contents = set(contents);
        for word in contents:           #get each word from the line and add to dict
            if word in dict:
                dict[word].append(f[0]) ;
                print(dict[word], word);
            else:
                dict[word] = [f[0]] ;
                print(dict[word], word);
    dict.close() ;
