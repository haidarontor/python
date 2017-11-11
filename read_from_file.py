file_open=open("filename.txt","r")

content=file_open.read()

print content
file_open.close()


file_open=open("filename.txt","r")

content=file_open.read(50)

print content
file_open.close()

file_open=open("filename.txt","r")

content=file_open.readlines()

print content
file_open.close()


file_open=open("filename.txt","r")

for file in file_open:
    print file
file_open.close()