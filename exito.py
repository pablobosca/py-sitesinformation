import string
import socket
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
for name in names:
	try:
		socket.gethostbyname(name.split('/')[0])
	except:
		print (name.split('/')[0] + " non existant")
