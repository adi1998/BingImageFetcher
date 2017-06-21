import os
import random
import glob
import sys

def get_new_wallpapers(user_name):
	os.system("python /home/"+user_name+"/BingImageFetcher/download.py "+user_name)
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
	get_new_wallpapers(user_name)
	change_wallpaper(user_name)
