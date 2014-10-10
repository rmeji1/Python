import urllib.request
from urllib.error import URLError
import re
import pickle

def visit_url(url, domain):
	global crawler_backlog
	global dataList
	if(len(crawler_backlog)>10):
		return
	if(url in crawler_backlog and crawler_backlog[url] == 1):
		return
	else:
		crawler_backlog[url] = 1
		print(".", end="",flush=True)
	try:
		tempStr = "" ;
		page = urllib.request.urlopen(url)
		code=page.getcode()
		if(code == 200):
			content=pag,flush=Truee.read()
			content_string = content.decode("utf-8")
			regexp_title = re.compile('<title>(?P<title>(.*))</title>')
			regexp_keywords = re.compile('<meta name="keywords" content="(?P<keywords>(.*))" />')
			regexp_url = re.compile("http://"+domain+"[/\w+]*")
			regexp_page_heading = re.compile('<h1 id=".*" class="page">(?P<h1Name>(.*))</h1>')		
			regexp_selected = re.compile('<a class="l-url-current" href=".*" title="(?P<selected>(.*))">.*</a>')
			regexp_current_link = re.compile('<span class=".*">(?P<linkTitle>(.*))</span>.</li>')
			
			result = regexp_selected.search(content_string, re.IGNORECASE) ;
			if result:
				anchor_selected_title = result.group("selected") ;
				#print("Anchor", anchor_selected_title);
				tempStr += " " + anchor_selected_title ;				
						
			result = regexp_current_link.search(content_string, re.IGNORECASE) ;
			if result:
				current_link = result.group("linkTitle") ;
				tempStr += " " + current_link ;	
				#print("Link title", current_link) ;

			result = regexp_page_heading.search(content_string, re.IGNORECASE) ;
			if result:
				page_title = result.group("h1Name") ;
				if page_title != "Page Not Found":
					tempStr += " " + page_title ;	
					#print(page_title);

			# Save to list
			dataList.append((url, tempStr)) ;
			for (urls) in re.findall(regexp_url, content_string):
				if(urls not in crawler_backlog or crawler_backlog[urls] != 1):
					crawler_backlog[urls] = 0
					visit_url(urls, domain)
	except URLError as e:
		print("error")

crawler_backlog = {}
dataList = [] ;
seed = "http://www.newhaven.edu/"
crawler_backlog[seed]=0
visit_url(seed, "www.newhaven.edu")
#Do pickling here. 
rawData = open("urls.pickle", "wb") ;
pickle.dump(dataList, rawData) ;
rawData.close() ;
print("Done");
