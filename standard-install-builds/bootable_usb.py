#create bootable usb
umount /dev/sdb
sudo mkfs.vfat /dev/sdb
sudo dd if=manjaro.iso of=/dev/sdb bs=1M status=progress

python -m ensurepip --upgrade #installing pip package manager

flatpak run net.pcsx2.PCSX2 #ps2emulator

