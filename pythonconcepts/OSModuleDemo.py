# Explored os Module in Python ~~~
# performed some common tasks with the os module in vs code :

# main.py~~
# import os
# if (not os.path.exists("data")):
#     os.mkdir("data")
# for i in range(0, 100):
#     os.mkdir(f"data/Day{i + 1}")

# oslist.py~~
# import os
# folders = os.listdir("data")
# print(os.getcwd())
# os.chdir("/Users")
# print(os.getcwd())
# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))

# rena.py~~
# import os
# for i in range(0, 100):
#     os.rename(f"data/Tutorial{i + 1}", f"data/Tutorial {i + 1}")