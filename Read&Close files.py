'''This is how you can read files and have python close the file automatically'''


with open("./Machine Learning Model.ipynb", "r") as File1:
    file_stuff = File1.read()
    print(file_stuff)

print(File1.closed)
print(file_stuff)