import os
import random
import glob
import sys
import download
import archive

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
	os.system("PID=$(pgrep -o gnome-session)&&export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)&&gsettings set org.gnome.desktop.background picture-uri file://"+lucky_choice)
	
if __name__ == "__main__":
	try:
		user_name = sys.argv[1]
	except:
		print "Argument missing"
		sys.exit()
	if download.download_all_wallpaper(user_name):
		archive.find_files_to_archive(user_name) #got new wallpapers then archive old
	else:
		change_wallpaper(user_name)	#if not change cureent wallpaper
