import os

print(os.getcwd())
f_path = r"/inbuilt_modules/os_module\\"
# os.mkdir(f_path+"new_folder")
# os.chdir(f_path+"new_folder")
# print(os.getcwd())

# os.rmdir(f_path+"new_file.txt")

f = r"C:\Users\Vidya\PycharmProjects\Python_\files\sample.txt"
# with open(f) as file:
#     pass


# os.popen(f)
# os.rename(f, "example.txt")

print(os.path.exists(f))
print(os.path.getsize(f))