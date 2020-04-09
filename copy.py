import os
import shutil
import random
now = os.getcwd() #получение текущей рабочей директории
old_path = input("Скажите какую папку вы собираетесь сдублировать?")

new_path = old_path + str(random.randint(0,1000))

os.makedirs(new_path)

directory_files = os.listdir(old_path ) # directory_path
for name in directory_files:
    print(name)
    shutil.copy2(old_path + "/" + name, new_path + "/" + name)

