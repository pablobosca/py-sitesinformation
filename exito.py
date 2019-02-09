import string
import socket
import csv
import requests

url_list = 'exito.txt';
l_urls = list()
f_urls = open(url_list, 'r');
for url in f_urls: # for each url in urls
	if url.strip()=='':
		continue	
	else:
		l_urls.append(url.strip()) #store each line of the file in an array
#check if every line has http first, splitting by http://
names = list()
invalidFile = 0
for url in l_urls:
	if url.lower().find('http://') == -1 and url.lower().find('https://') == -1:
		print (url + " invalid string - No http or https")
		invalidFile = 1
		break
	try:
		names.append(url.lower().split('http://')[1])
	except:
#		print url
		names.append(url.lower().split('https://')[1])

if invalidFile == 1:
	print ("\n\n\t\taborting since there are invalid URLs\n\n\n")
	exit()
#print names
cont = 0
fail = 0
report = list()
row = list()
row.append('Site')
row.append('IP Address')
row.append('Protocol')
report.append(row)
with open('exito_output.csv', 'w') as f:
	writer = csv.writer(f,dialect='excel')
	for name in names:
		domain = name.split('/')[0]
		row = list()
		row.append(domain)
		try:
			row.append(socket.gethostbyname(domain))
			row.append(requests.get('http://' + domain).url.split(':')[0])
			report.append(row)
			print row
		except:
			fail = fail + 1
			row.append("Unresolved")
			report.append(row)
			print row
	writer.writerows(report)
	print report
	cont = cont + 1 



#'forfriends.do.am','195.216.243.40'
#'www.pyabinava.site','104.24.112.136'
#'calmstars.do.am','213.174.157.150'
