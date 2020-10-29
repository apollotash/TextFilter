import os
import platform


file_path = os.path.dirname(__file__) + "/textBeforeFilter.txt"
with open(file_path, "r") as data_file:
    data = data_file.readlines()

new_data = []
for i in data:
    if ("İndirimli" not in i) and ("Burslu" not in i) and ("Ücretli" not in i):
            new_data.append(i+"\n")
    else:
        pass

new_file_path = os.path.dirname(__file__)+"/textAfterFilter.txt"
with open (new_file_path, "w") as new_data_file:
        new_data_file.writelines(new_data)

if platform.system() == "Linux":
    os.system("xdg-open " + new_file_path)
elif platform.system() == "Windows":
        os.system("start " + new_file_path) #for windows
elif platform.system() == "Darwin":
        os.system("open " + new_file_path)  #for Mac
else:
    print("Please try your code on another machine.!")
