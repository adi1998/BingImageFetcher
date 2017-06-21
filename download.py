import json
import os
import urllib
import sys
import requests

website_url = "https://www.bing.com"

#function to download file
def fetch_file(url,file_name,user_name):
	download_dir="/home/"+user_name+"/Pictures/Wallpaper/bing/"
	downlaodfile = urllib.URLopener()
	print "Starting Download of File: "+file_name
	downlaodfile.retrieve(url, download_dir+file_name)
	print "Download finished of File: "+file_name
	return

#Check if file already exists
def get_file_download_status(file_name,user_name):
	download_dir="/home/"+user_name+"/Pictures/Wallpaper/bing/"
	file_list = os.listdir(download_dir)
	if file_name in file_list:
		return False
	return True

#main function to be ca lled from other script
def download_all_wallpaper(user_name):
	req_bing = requests.get(website_url+"/HPImageArchive.aspx", params={'format':'js','idx':'0','n':'10','mkt':'en-US'})

	#parse json
	data = req_bing.json()
	index_max = len(data["images"]) #no of images on server
	
	for i in range(0,index_max):
		base_url = data["images"][i]["urlbase"]
		download_url = website_url+base_url+"_1366x768.jpg"
		file_name = download_url.split("/")[-1]
		print download_url
		if get_file_download_status(file_name,user_name):
			fetch_file(download_url,file_name,user_name)
		else:
			print "File already exists: "+file_name
	return

if __name__ == "__main__":
	try:
		user_name = sys.argv[1]
	except:
		print "Argument missing"
		sys.exit()
	download_all_wallpaper(user_name)
