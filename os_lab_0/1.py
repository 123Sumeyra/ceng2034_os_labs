import os
os.system("ls -l")


dosyalar =os.listdir()
for dosya in dosyalar:
    if dosya.endswith(".txt"):
        print(dosya)
