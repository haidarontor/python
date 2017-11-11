file_write=open("filename.txt","w")

file_write.write("Python Programming.Python Programming.Python Programming")
file_write.close()

file_write=open("filename.txt","r")

print file_write.read()

file_write.close()