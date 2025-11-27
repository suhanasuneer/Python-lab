list1=[]
with open('text.txt','r') as file1:
    for line1 in file1:
        list1.append(line1.split())
print(list1)
