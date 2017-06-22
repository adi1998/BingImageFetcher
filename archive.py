import os
import sys

def function_move(file_name,user_name):
	main_file = "/home/"+user_name+"/Pictures/Wallpaper/bing/"+file_name
	archive_file = "/home/"+user_name+"/Pictures/Wallpaper/bing/archive/"+file_name
	command = "mv "+main_file+" "+archive_file
	os.system(command)
	return

def find_files_to_archive(user_name):
	main_dir = "/home/"+user_name+"/Pictures/Wallpaper/bing/"
	file_list = os.listdir(main_dir)
	file_list.remove('archive') #List all image files
	
	current_epoch = int(os.popen('date +%s').read()) #current epoch time
	for i in file_list:
		time = os.path.getmtime(main_dir+i)
		time_difference = current_epoch - time
		if time_difference/(60.0*60.0*24.0*40.0)>=1: #if older than 40 days
			function_move(i,user_name)
			print "File archived: "+i
		else:
			print "File is new: "+i
	return

if __name__ == "__main__":
	try:
		user_name = sys.argv[1]
	except:
		print "Argument missing"
		sys.exit()
	find_files_to_archive(user_name)
