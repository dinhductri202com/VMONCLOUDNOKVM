import os
print ("Waiting For Install...")
print ("log:")
os.system("apt update -y >/dev/null 2>&1 ")
os.system("if ! command -v qemu-system-x86_64 ; then echo && apt install qemu-system -y >/dev/null 2>&1'  ;else command; fi")
os.system("if ! command -v 7z ; then echo && apt install p7zip-full -y >/dev/null 2>&1'  ;else command; fi")

print wait

