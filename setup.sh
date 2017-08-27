#!/bin/bash

SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

source $SCRIPTPATH/config.data
echo -e "\033[0;36m--------------- ""$name"" ""$version"" ---------------"
echo "$description"
echo "Author: ""$author"
echo "GitHub Repo: ""$github_link"

echo -e "\033[1;33mSetting up at /home/$USER/BingImageFetcher"
echo "Creating required Files"

echo "Creating directory ~/BingImageFetcher"
mkdir -p ~/BingImageFetcher

echo "Creating directory ~/BingImageFetcher/DataFiles"
mkdir -p ~/BingImageFetcher/DataFiles

echo "Creating directory ~/BingImageFetcher/tmp"
mkdir -p ~/BingImageFetcher/tmp

echo "Creating directory ~/Pictures/Wallpaper"
mkdir -p ~/Pictures/Wallpaper

echo "Creating directory ~/Pictures/Wallpaper/bing"
mkdir -p ~/Pictures/Wallpaper/bing

echo "Creating directory ~/Pictures/Wallpaper/bing/archive"
mkdir -p ~/Pictures/Wallpaper/bing/archive

echo -e "\033[0;33mCopying from to $SCRIPTPATH/download.py ~/BingImageFetcher"
cp "$SCRIPTPATH"/download.py ~/BingImageFetcher/download.py

echo "Copying from to $SCRIPTPATH/mainscript.py ~/BingImageFetcher"
cp "$SCRIPTPATH"/mainscript.py ~/BingImageFetcher/mainscript.py

echo "Copying from to $SCRIPTPATH/archive.py ~/BingImageFetcher"
cp "$SCRIPTPATH"/archive.py ~/BingImageFetcher/archive.py

echo "Copying from to $SCRIPTPATH/setup.sh ~/BingImageFetcher"
cp "$SCRIPTPATH"/setup.sh ~/BingImageFetcher/setup.sh

echo "Copying from to $SCRIPTPATH/config.data ~/BingImageFetcher"
cp "$SCRIPTPATH"/config.data ~/BingImageFetcher/config.data
echo "Copying completed"

echo -e "\033[1;37mSetting up Cron Job"

crontab -l >~/BingImageFetcher/tmp/cronjob
echo "#BingImageFetcher script **don't edit next line**">>~/BingImageFetcher/tmp/cronjob
echo "*/30 * * * * python /home/$USER/BingImageFetcher/mainscript.py $USER">>~/BingImageFetcher/tmp/cronjob

crontab ~/BingImageFetcher/tmp/cronjob
echo "Setup Complete"
echo -e "\033[0;31mRemoving temporary files"
rm -r ~/BingImageFetcher/tmp
echo -e "You may delete this files\033[0m"

#author gr33n5h4d0w
