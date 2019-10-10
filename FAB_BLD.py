import os

path = "C:/Users/CDGarcia/Desktop"

os.chdir(path)

gribs = os.listdir("testgrib")
print(gribs)

print(os.getcwd())

if not os.path.exists(os.path.basename("gribs")):
    os.makedirs(os.path.dirname("gribs"))
with open(path, "w") as f:
    f.write("filename")
#%%
    
import os 
path = "C:/CHRIS/testfolder/testgrib" 
gribs = os.listdir(path) 
grib = gribs 
os.chdir(path) 
print (os.getcwd())
for folder in grib: 
    os.makedirs(os.path.join(path, folder + '.subdata'))
#%%
    
import os, shutil

for i in files:
  os.mkdir(os.path.join(dir_name , i.split(".")[0]))
  shutil.copy(os.path.join(dir_name , i), os.path.join(dir_name , i.split(".")[0]))
#%%
import glob, os, shutil
#%%
folder = r'C:\Users\aesnj\OneDrive\Desktop\MIT_'

for file_path in glob.glob(os.path.join(folder, '*.*')):
    new_dir = file_path.rsplit('.', 1)[0]
    try:
        os.mkdir(os.path.join(folder, new_dir))
    except WindowsError:
        # Handle the case where the target dir already exist.
        pass
    shutil.move(file_path, os.path.join(new_dir, os.path.basename(file_path)))  
  