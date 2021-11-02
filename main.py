from gnewsclient import gnewsclient
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
from tqdm import tqdm
import json
import pandas as pd
import threading

def search_news(lang,loc,topicc,no_of_results):
	# search for news articles
	client = gnewsclient.NewsClient(language=lang,
	                                location=loc,
	                                topic=topicc,
	                                max_results=no_of_results)
	 
	news_list = client.get_news()
	return(news_list)

def extract_text(url):
	# given the url of a news article extract all textual content from it 
	text = ""
	try:

		req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		html = urlopen(req).read()
		soup = BeautifulSoup(html, features="html.parser")

		# kill all script and style elements
		for script in soup(["script", "style"]):
		    script.extract()    # rip it out

		# get text
		text = soup.get_text()

		# break into lines and remove leading and trailing space on each
		lines = (line.strip() for line in text.splitlines())
		# break multi-headlines into a line each
		chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
		# drop blank lines
		text = '\n'.join(chunk for chunk in chunks if chunk)
	except Exception as e: 
		i = 0
	return(text)

def extract_bunch(li,start,end,folder,checkpoint_duration,thread_id):
	# extract text from a set of articles
	# this is called by each thread
	dic = {}
	for i in tqdm(range(start,end)):

		row = li[i]
		if(row[4]=='en'):
			row.append(extract_text(row[3]))
			dic[i] = row
		if i%checkpoint_duration==0:
			start_str = str(start)
			checkpoint = str(i)
			with open(folder + "\\"+str(thread_id)+"_output.json", "w",encoding = "UTF-16") as outfile:
				json.dump(dic, outfile)
	with open(folder + "\\"+str(thread_id)+"_output.json", "w",encoding = "UTF-16") as outfile:
		json.dump(dic, outfile)
	return



# input csv file
input_csv = 'news.csv'

df = pd.read_csv(input_csv)
li = df.values.tolist()
nli = []
for r in li:
	if r[4] =='en':
		nli.append(r)
li = nli
ind = 0
dic = {}


# path to output folder
output_folder = "output\\"

# total number of threads

no_of_threads = 10

# limit the number of articles to search by setting tasks = lets say 100
# 100 can be any number < total headlines
tasks = len(li)

per_thread = tasks//no_of_threads

# checkpoint duration, set the number after which checkpoints are made, 100 is a good number
checkpoint_duration = 100






threads = []
for i in range(0,no_of_threads):
	ti = threading.Thread(target=extract_bunch, args=(li,i*per_thread,min((i+1)*per_thread,tasks),output_folder,checkpoint_duration,i))
	ti.start()
	threads.append(ti)
for thread in threads:
	thread.join()

