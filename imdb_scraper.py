#########################################################
# Author: Rajanikant Tenguria
# Start : 4 March 2019
# Last  : 10 March 2019
#########################################################
# Loading...                                      
# ======>                                           28 %
#########################################################

#https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3
# Movie name 		        - Done
# Year 				        - Done
# Genre 			
# Release Date 		        - Done
# Duration 			
# Rating 			
# Reviewer count 	
# Director 			        - Done
# Writer
# User Rev Count
# Critic Rev Count
# Wins				
# Nominations		
# Certificate		
# Language			
# Country			
# Gross 
# Production		
# Sound Mix			
# Color				
# Aspect Ratio
# Cast
# Rating Demographics
# Summary
# Keywords
# Tech spec https://www.imdb.com/title/tt0468569/technical?ref_=tt_dt_spec
# Filming Prod https://www.imdb.com/title/tt0468569/locations?ref_=ttspec_ql_5
# Company credits https://www.imdb.com/title/tt0468569/companycredits?ref_=ttloc_ql_4
# External site https://www.imdb.com/title/tt0468569/externalsites?ref_=ttco_ql_3
# Release dates https://www.imdb.com/title/tt0468569/releaseinfo?ref_=tt_ql_2
# Cast https://www.imdb.com/title/tt0468569/fullcredits?ref_=ttrel_ql_1
# Plot keywords https://www.imdb.com/title/tt0468569/keywords?ref_=ttpl_ql_4
# Parents Guide https://www.imdb.com/title/tt0468569/parentalguide?ref_=tttg_ql_5
# Connections https://www.imdb.com/title/tt0468569/movieconnections?ref_=ttalt_ql_6
# Soundtracks https://www.imdb.com/title/tt0468569/soundtrack?ref_=ttcnn_ql_7
# Awards https://www.imdb.com/title/tt0468569/awards?ref_=ttsnd_ql_op_1
# Ratings https://www.imdb.com/title/tt0468569/ratings?ref_=tturv_ql_4
# Metacritic https://www.imdb.com/title/tt0468569/criticreviews?ref_=ttexrv_ql_6

import requests
from bs4 import BeautifulSoup
from pprint import pprint
from time import sleep
import json
import regex as re
headers = {'headers': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}

url_metac = 'https://www.imdb.com/title/tt3460252/criticreviews?ref_=ttexrv_ql_6'
url = 'https://www.imdb.com/title/tt0075148/'
tspec = '/technical?ref_=tt_dt_spec'
fprod = '/locations?ref_=ttspec_ql_5'
ccred = '/companycredits?ref_=ttloc_ql_4'
esite = '/externalsites?ref_=ttco_ql_3'
rdate = '/releaseinfo?ref_=tt_ql_2'
cast = '/fullcredits?ref_=ttrel_ql_1'
keyw = '/keywords?ref_=ttpl_ql_4'
guide = '/parentalguide?ref_=tttg_ql_5'
conn = '/movieconnections?ref_=ttalt_ql_6'
sound = '/soundtrack?ref_=ttcnn_ql_7'
awa = '/awards?ref_=ttsnd_ql_op_1'
ratg = '/ratings?ref_=tturv_ql_4'
metac = '/criticreviews?ref_=ttexrv_ql_6'
p = 1

page_metac = requests.get(url_metac)
xpage_metac = str(page_metac)
soup_metac = BeautifulSoup(page_metac.text, 'html.parser')
ex = soup_metac.find(class_ = 'metascore_block')
x = re.findall(r'\d+',str(ex))
#print(x[0],x[3])

page_metac = requests.get(url_metac)
xpage_metac = str(page_metac)
soup_metac = BeautifulSoup(page_metac.text, 'html.parser')
ex = soup_metac.find(class_ = 'metascore_block')
x = re.findall(r'\d+',str(ex))
#print(x[0],x[3])

url_tspec = 'https://www.imdb.com/title/tt3460252'+tspec
page_metac = requests.get(url_tspec)
soup_metac = BeautifulSoup(page_metac.text, 'html.parser')
ex = soup_metac.find("label",class_ = 'dataTable labelValueTable')
#print(ex)

url_fprod = 'https://www.imdb.com/title/tt3460252'+fprod
page_metac = requests.get(url_fprod)
soup_metac = BeautifulSoup(page_metac.text, 'html.parser')
ex = soup_metac.find(class_ = 'article listo')
#print(ex)

url_ccred = 'https://www.imdb.com/title/tt3460252'+ccred
page_metac = requests.get(url_ccred)
soup_metac = BeautifulSoup(page_metac.text, 'html.parser')
ex = soup_metac.find(class_ = 'article listo')
#print(ex)

url_esite = 'https://www.imdb.com/title/tt3460252'+esite
page_metac = requests.get(url_esite)
soup_metac = BeautifulSoup(page_metac.text, 'html.parser')
ex = soup_metac.find(class_ = 'article listo')
#print(ex)

url_rdate = 'https://www.imdb.com/title/tt3460252'+rdate
page_rdate = requests.get(url_rdate)
soup_metac = BeautifulSoup(page_rdate.text, 'html.parser')
ex = soup_metac.find(class_ = 'article listo')
#print(ex)

url_cast = 'https://www.imdb.com/title/tt3460252'+cast
page_metac = requests.get(url_cast)
soup_metac = BeautifulSoup(page_metac.text, 'html.parser')
ex = soup_metac.find(class_ = 'article listo')
print(ex)

url_keyw = 'https://www.imdb.com/title/tt3460252'+keyw
page_metac = requests.get(url_keyw)
soup_metac = BeautifulSoup(page_metac.text, 'html.parser')
ex = soup_metac.find(class_ = 'article listo')
print(ex)

url_guide = 'https://www.imdb.com/title/tt3460252'+guide
page_metac = requests.get(url_guide)
soup_metac = BeautifulSoup(page_metac.text, 'html.parser')
ex = soup_metac.find(class_ = 'article listo')
print(ex)

page = requests.get(url)
xpage = str(page)
soup = BeautifulSoup(page.text, 'html.parser')

lname = soup.find('title')
#lgenre = soup.find(class_='subtext')
ldirector = soup.find(class_='credit_summary_item')
awards_list = soup.find(class_='article highlighted')
lrating = soup.find(class_='ratingValue')
ldate = soup.find(class_='title_wrapper')
director_list = soup.find(class_='credit_summary_item')



sawl = str(awards_list).split()
sawl = ' '.join(sawl)
rank = 0
oscars = 0
wins = 0
nominations = 0

#print(sawl)

if sawl.find('Oscar') != -1:
	posc = sawl.find('Oscar')
	oscars = re.findall(r'\d+',sawl[posc-8:posc])

if sawl.find('Top Rated Movie') != -1:
	prank = sawl.find('Top Rated Movie')
	rank = re.findall(r'\d+',sawl[prank:prank+30])
	
if sawl.find('awards-blurb') != -1:
	pwin = sawl.find('awards-blurb')
	#print(sawl[pwin-100:pwin+120])
	both = re.findall(r'\d+',sawl[pwin-100:pwin+120])
	if len(both) == 2:
		wins = both[0]
		nominations = both[1]
	else:
		wins = 0
		nominations = both[0]
"""
if sawl.find('nomination') != -1:
	pnom = sawl.find('nomination')
	nominations = re.findall(r'\d+',sawl[pnom-8:pnom])"""

#print(rank,oscars, wins, nominations)
q = soup.findAll('b',"awards-blurb", class_="article highlighted")
#print(q)
			
"""
for i in awards_list:
	print(i)
	print('---------')
		
p = str(soup.find('script', {'type':'application/ld+json'}))
intp = p.find('duration')+14
ldur = p[intp:intp+4]
x = re.findall(r'\d+', ldur)
dur = 60*int(x[0])+int(x[1])
"""

lll = (soup.findAll("h4", class_="inline"))


genre = []
sound = []
production = []
certificate = []
writer = []
country = []
language = []
color = []
duration = []

for h4 in lll:
	for text in h4:
		x = h4.find_next_siblings()
		for txt in x:
			#print(text,txt.contents)
			if text == 'Genres:':
				if len(str(txt.contents))>5:
					genre.append(str(txt.contents)[3:-2])
			if text == 'Sound Mix:':
				if len(str(txt.contents))>5:
					sound.append(str(txt.contents)[2:-2])
			if text == 'Production Co:':
				if len(str(txt.contents))>5:
					production.append(str(txt.contents)[2:-2])
				#production = production[:2]
			if text == 'Certificate:':
				if len(str(txt.contents))<11:
					certificate.append(str(txt.contents)[2:-2])
				#certificate = certificate[:1]
			if text == 'Writers:':
				if len(str(txt.contents))>5:
					writer.append(str(txt.contents)[2:-2])
				#writer = writer[:1]
			if text == 'Country:':
				if len(str(txt.contents))>5:
					country.append(str(txt.contents)[2:-2])
				#country = country[0]
			if text == 'Language:':
				#print(str(txt.contents),len(str(txt.contents)))
				if len(str(txt.contents))>5:
					language.append(str(txt.contents)[2:-2])
				#language = language[0]
			if text == 'Color:':
				if len(str(txt.contents))>5:
					color.append(str(txt.contents)[2:-2])
				#color = color[0]
			if text == 'Runtime:':
				if len(str(txt.contents))>5:
					duration.append(str(txt.contents)[2:-2])
				#color = color[0]
#print(duration)
			
"""
for h4 in lll:
    for text in h4:
        print(text,h4.find_next_siblings())
"""
# Pull text from all instances of <a> tag within BodyText div
#genre = lgenre.find_all('a')
director = ldirector.find_all('a')
date = ldate.find_all('a')
#awards = awards_list.find_all('a')

# Create for loop to print out all artists' names

for i in director:
    tdirector = i.contents[0]

for i in date:
    rdate = i.contents[0]

"""print (awards_list)
if awards_list != None:
	tawards = awards_list.contents[0].split()
	if len(tawards)>2:
		wins = tawards[0]
		nominations = tawards[3]
	
	else:
		wins = 0
		nominations = tawards[0]
"""

name = str(lname.contents)[2:-16]
year = str(lname.contents)[-14:-10]
xrating = str(re.findall(r'"(.*?)"',str(lrating.contents))[0])
rating = xrating.split()[0]
rev_cnt = xrating.split()[3]
day = rdate.strip().split()[0]
month = rdate.strip().split()[1]
year = rdate.strip().split()[2]

"""
print (name)
print (rank)
print (oscars)
print (wins)
print (nominations)
print (rating)
print (rev_cnt)
print (day)
print (month)
print (year)
print (genre)
print (sound)
print (production)
print (certificate)
print (writer)
print (country)
print (language)
print (color)
print(duration)

"""
