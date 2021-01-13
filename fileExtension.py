filename = input("Input the Filename: ")
file_extn = filename.split(".")
ext={"py":"python","txt":"txt","java":"java","c":"c"}
print("The extension of the file is : " + ext[file_extn[-1]])
