import os,sys

name = sys.argv[1]
os.system("adb shell screencap -p /sdcard/%s.png" %name)
os.system("adb pull /sdcard/%s.png E:\screen-3.8.1" %name)

