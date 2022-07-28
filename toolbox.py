#create bootable usb
umount /dev/sdb
sudo mkfs.vfat /dev/sdb
sudo dd if=manjaro.iso of=/dev/sdb bs=1M status=progress

python -m ensurepip --upgrade #installing pip package manager

flatpak run net.pcsx2.PCSX2 #ps2emulator

#view remote git
git remote -v

#change https git repo to ssh
git remote set-url origin git@github.com:nondominant/purple-elephant.git

#adding ssh key to the ssh-agent process 
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

curl -s http://host.net/url.html | sed -rn '/magnet/{s/.*(magnet:[^"]*).*/\1/g;p}' #scrape magnet links using curl

sed -n '3{p;q}' file #print out single line of a file specified by number (in this case line 3)

find . -type f -name *.html -print0 | xargs -0 sed -i '' -e "s/$existing/$replacement/g" #find and replace in all files in all directories

http-server [path] [options] #nodejs server, install using "npm install --global http-server"

npx babel script.js --out-file script-compiled.js #manually compile babeljs file

gcc -g main.c #compile c file with debugging info 

gdb a.out #debug binary output of gcc

xset r rate 500 80 #sets key repeat rate, 500 millisecond start delay, 80 strokes a second

#python script to create blank png
from PIL import Image
img = Image.new('RGB', (32,32), color='white')
img.save('empty.png')
quit()

curl -H "$(cat headers.txt)" "$(cat url.txt)"
curl -H @headers.txt "$(cat url.txt)"
#using @header.txt is better the other way doesn't override headers it sends
#duplicates, which can be bad


#add an ssh key to a vultr server
ssh-copy-id -i ~/.ssh/id_ed25519 root@66.42.32.91

#generate ssh key
ssh-keygen -t ed25519 -C "email@gmail.com"

#creating user on remote server
adduser sandworm

#add user to sudo group
usermod -aG sudo sandworm

#switch users
su - sandworm

#maria db setup requires gpg key repo (debian)
sudo apt -y install curl software-properties-common gnupg2

#connect to remote database
mysql -u u206225039_peter -h test-deployment.live -P 3306 -D u206225039_database -p

#use tar to stream files over ssh " - "'s must be included
tar -cf - file.a file.b file.c | ssh root@192.0.0.128 tar -xvf -

#see open port info
sudo lsof -i -P -n | grep LISTEN
#see open port info
sudo netstat -tulpn | grep LISTEN
#see open port info
sudo ss -tulpn | grep LISTEN
#see open port info
sudo lsof -i:22 ## see a specific port such as 22 ##
#see open port info
sudo nmap -sTU -O IP-address-Here


#clean and restart docker container
docker-compose down
docker rm -f $(docker ps -a -q)
docker volume rm $(docker volume ls -q)
docker-compose up -d # -d specifies detached 


vim -T dumb -N -u NONE --noplugin -es -n -c "set nomore" -S "commands.vim" "filespec"
#Here's a summary of the used arguments:
-T dumb        # Avoids errors in case the terminal detection goes wrong.
-N -u NONE     # Do not load vimrc and plugins, alternatively:
--noplugin     # Do not load plugins.
-n             # No swapfile.
-es            # Ex mode + silent batch mode -s-ex
               #   Attention: Must be given in that order!
-S ...         # Source script.
-c 'set nomore'# Suppress the more-prompt when the screen is filled
               #   with messages or output to avoid blocking.


#start virtual machine manager
virt-manager

#install elm
npm i -g elm
cd /usr/lib
sudo ln -s libncurses++w.so.6 libtinfo.so.5
