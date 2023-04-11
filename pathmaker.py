import os
dirname = os.path.dirname(__file__)
try:
    os.makedirs("./dirA/dirB")
except FileExistsError:
    print("File already exists") 