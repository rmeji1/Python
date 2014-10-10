from datetime import datetime
import shelve
# ------------------------------------------------------------------------------
# Function that will get input query
def getQuery( ) :
    query=input("query:");
    query = set(query.split()) ;
    return query ;
# ------------------------------------------------------------------------------
def search(shovelFile) :
	query = getQuery() ;
	lists = [] ;
	dict = shelve.open(shovelFile)
	dt1 = datetime.now() ; # --------------------------------------Record start time
	if "or" in query and "and" not in query:
		query.remove("or") ; # ---------------------------- remove or from the query
		# for every word in the query check if the word is a key for dictionary,
		# if so append list to the current list.
		for word in query:
			if word in dict:
				print("Found at", dict[word]) ;
	else:
		if "and" in query:
			query.remove("and") ;
		for word in query:
			if word in dict:
				lists.append(set(dict[word]))
				results = set(lists[0]).intersection(*lists) ;
		for result in results:
			print("Found at", result) ;
	dt2= datetime.now() ;
	dict.close();
	print("Execution time:", dt2.microsecond-dt1.microsecond);
