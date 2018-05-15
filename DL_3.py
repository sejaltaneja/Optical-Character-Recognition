from PIL import Image
import pytesseract

temp=''
new=[]

im = Image.open("C:/Users/Sejal Taneja/Desktop/DL_3.jpg")
text = pytesseract.image_to_string(im)
#print(text)

temp=text
list = temp.split('\n')
#print(list)

#filtering the list for my clarity: removing white spaces
for i in list:
    if i=='':
        list.remove(i)


for i in list:
    k=i.split(' ')
    new.append(k)
#Printing the list containing each element that was optically recognised
#print(new, '\n')

#Printing the Output
print("Name", new[1][1], new[1][2])
print("S/D/W of", new[2][1])
print("Address", new[3][1], new[3][2], new[4][1], new[4][2], new[5][4], new[6][4])
print("Date of Birth :", new[6][3])
print("Driving License Number :", new[0][1])