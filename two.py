
lis = ['one','two','three','four']
try:
    with open("file.txt","w") as file:
        for word in lis:
            file.writelines(word+"\n")
except FileExistsError:
    print("FileExistsError found")