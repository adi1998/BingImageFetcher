import os
import random
import glob
import sys

def check_if_day_passed(user_name):
	#Read when was wallpapers last downloaded
	current_epoch_time = int(os.popen('date +%s').read())
	file = open('/home/'+user_name+'/BingImageFetcher/DataFiles/time.data','r')
	last_download_time_passed = current_epoch_time - int(file.read())
	file.close()

	if last_download_time_passed/86400.0>=1:
		os.system("python /home/"+user_name+"/BingImageFetcher/download.py "+user_name)
		print "New wallpaper downloaded"
	else:
		print "Not a day passed yet"
	return

def get_image_path(user_name):
	#get all image list
	image_list = glob.glob("/home/"+user_name+"/Pictures/Wallpaper/bing/*.jpg")
	if len(image_list)==0:
		return str(None)
	return random.choice(image_list)

def change_wallpaper(user_name):
	#image to be set
	lucky_choice = get_image_path(user_name)
	print lucky_choice
	#Export Display added in cronscript.sh
	os.system("gsettings set org.gnome.desktop.background picture-uri file://"+lucky_choice)
	
if __name__ == "__main__":
	try:
		user_name = sys.argv[1]
	except:
		print "Argument missing"
		sys.exit()
	check_if_day_passed(user_name)
	change_wallpaper(user_name)
