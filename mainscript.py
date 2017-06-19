import os
import random
import glob
def check_if_day_passed():
	#Read when was wallpapers last downloaded
	current_epoch_time = int(os.popen('date +%s').read())
	file = open('/home/gr33n5h4d0w/automate_things/bing_wallpaper/DataFiles/time.data','r')
	last_download_time_passed = int(file.read()) - current_epoch_time
	file.close()

	if last_download_time_passed/86400.0>=1 :
		#transfer old wallpaper to archive
		os.system("mv /home/gr33n5h4d0w/Pictures/Wallpaper/bing/* /home/gr33n5h4d0w/Pictures/Wallpaper/bing/archive")
		
		os.system("python /home/gr33n5h4d0w/automate_things/bing_wallpaper/download.py")
		print "New wallpapers downloaded"
	else:
		print "Not a day passed yet"
	return

def get_image_path():
	#get all image list
	image_list = glob.glob("/home/gr33n5h4d0w/Pictures/Wallpaper/bing/*.jpg")

	#Read index from file
	try:
		file = open('/home/gr33n5h4d0w/automate_things/bing_wallpaper/DataFiles/LastWallpaper.data','r')
		index_last = int(file.read())
		file.close()
	except:
		index_last = random.randint(0,len(image_list))

	index_max = len(image_list) - 1
	next_index = index_last + 1
	if index_max==0:
		return None
	elif next_index>index_max:
		next_index=0

	#write index to file
	file = open('/home/gr33n5h4d0w/automate_things/bing_wallpaper/DataFiles/LastWallpaper.data','w')
	file.write(str(next_index))
	file.close()

	return image_list[next_index]

def change_wallpaper():
	#image to be set
	lucky_choice = get_image_path()
	print lucky_choice
	#this time that gui export dispaly is added in cron
	os.system("gsettings set org.gnome.desktop.background picture-uri file://"+lucky_choice)
	os.system("echo 'asdfg'>>/home/gr33n5h4d0w/wow.txt")
	
if __name__ == "__main__":
	check_if_day_passed()
	change_wallpaper()
