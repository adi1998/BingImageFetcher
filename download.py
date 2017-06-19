import json
import os
import urllib
import requests

website_url = "https://www.bing.com"
download_dir="/home/gr33n5h4d0w/Pictures/Wallpaper/bing/"
epoch_time = int(os.popen('date +%s').read())

def fetch_file(url,index):
	global epoch_time
	global download_dir
	name = str(epoch_time) + "_" + str(index)+".jpg"
	testfile = urllib.URLopener()
	print "Starting Download File: "+str(index)
	testfile.retrieve(url, download_dir+name)
	print "Download finished File: "+str(index)
	return
#main function to be ca lled from other script
def download_all_wallpaper():
	req_bing = requests.get(website_url+"/HPImageArchive.aspx", params={'format':'js','idx':'0','n':'100','mkt':'en-US'})

	#parse json
	data = req_bing.json()
	index_max = len(data["images"]) #no of images on server
	
	for i in range(0,index_max):
		base_url = data["images"][i]["urlbase"]
		download_url = website_url+base_url+"_1366x768.jpg"
		print download_url
		fetch_file(download_url,i)
	update_time_in_file()
	return

#functio to write time
def update_time_in_file():
	#update data file with last downloaded time
	file = open('/home/gr33n5h4d0w/automate_things/bing_wallpaper/DataFiles/time.data','w')
	file.write(str(epoch_time))
	file.close()
	return

if __name__ == "__main__":
	download_all_wallpaper()
