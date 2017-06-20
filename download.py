import json
import os
import urllib
import sys
import requests

website_url = "https://www.bing.com"
epoch_time = int(os.popen('date +%s').read())

def fetch_file(url,index,user_name):
	global epoch_time
	download_dir="/home/"+user_name+"/Pictures/Wallpaper/bing/"
	name = str(epoch_time) + ".jpg"
	testfile = urllib.URLopener()
	print "Starting Download File: "+str(index)
	testfile.retrieve(url, download_dir+name)
	print "Download finished File: "+str(index)
	return
#main function to be ca lled from other script
def download_all_wallpaper(user_name):
	req_bing = requests.get(website_url+"/HPImageArchive.aspx", params={'format':'js','idx':'0','n':'1','mkt':'en-US'})

	#parse json
	data = req_bing.json()
	index_max = len(data["images"]) #no of images on server
	
	for i in range(0,index_max):
		base_url = data["images"][i]["urlbase"]
		download_url = website_url+base_url+"_1366x768.jpg"
		print download_url
		fetch_file(download_url,i,user_name)
	update_time_in_file(user_name)
	return

#function to write time
def update_time_in_file(user_name):
	#update data file with last downloaded time
	file = open('/home/'+user_name+'/BingImageFetcher/DataFiles/time.data','w')
	file.write(str(epoch_time))
	file.close()
	return

if __name__ == "__main__":
	try:
		user_name = sys.argv[1]
	except:
		print "Argument missing"
		sys.exit()
	download_all_wallpaper(user_name)
