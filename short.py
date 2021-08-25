import os

arr = os.listdir("archives")
myFile = open("list.txt", "w");

# Sort the array before looping
arr.sort();

for x in arr:
    myFile.write(f"* [{x}](/archives/{x}?raw=true)\n")
    #print(f"/archives/{x}")

myFile.close();
