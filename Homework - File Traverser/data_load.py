#UPS 1z577140YW42419485

from datetime import datetime
import time
from quotes import data_list
# ------------------------------------------------------------------------------
# Function that does the preprocessing
def getDict() :
    dict = {} ;
    for i,line in enumerate(data_list): # get each line from the data_list
        line = line.replace(',', '');
        line = line.replace('.','');
        line = line.split() ;
        line = set(line) ;
        for word in line:           #get each word from the line and add to dict
            if word in dict:
                dict[word].append(i) ;
            else:
                dict[word] = [i] ;
    #print(dict) ;
    return dict ;
# ------------------------------------------------------------------------------
# Function that will get input query
def getQuery( ) :
    query=input("query:");
    query = set(query.split()) ;
    return query ;

# ------------------------------------------------------------------------------
# Start of application
dict = getDict() ; # -------------------------------------------Do preprocessing
query = getQuery() ;
lists = [] ;
dt1 = datetime.now() ; # --------------------------------------Record start time
if "or" in query and "and" not in query:
    query.remove("or") ; # ---------------------------- remove or from the query
    # for every word in the query check if the word is a key for dictionary,
    # if so append list to the current list.
    for word in query:
        if word in dict:
            print(dict[word]);
            lists = lists + dict[word] ;
    for index in set(lists) :
        print("Found at", index, data_list[index]) ;
else:
    if "and" in query:
        query.remove("and") ;
    for word in query:
        if word in dict:
            lists.append(set(dict[word]))
    results = set(lists[0]).intersection(*lists) ;
    for result in results:
        print("Found at", result, data_list[result]) ;

dt2= datetime.now() ;
#print("Execution time", (time.time() - starttime) * 1000, "microseconds" ) ;
print("Execution time:", dt2.microsecond-dt1.microsecond);
