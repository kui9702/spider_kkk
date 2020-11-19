import os

def exist_file(path):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print(path+'-->存在')