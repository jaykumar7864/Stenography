import cv2
import string
import os

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

img = cv2.imread("Snake_python.jpg")

i = img.shape[0]
j = img.shape[1]
print(i, j)

msg = input("Enter secret message:")
password = input("Enter a passcode:")

kl = 0
tln = len(msg)
z = 0

n = 0
m = 0
l = len(msg)

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]] ^ d[password[kl]]
    n = n + 1
    m = m + 1
    m = (m + 1) % 3
    kl = (kl + 1) % len(password)

cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")

print("Data Hiding in image completed successful")

kl = 0
tln = len(msg)
z = 0

n = 0
m = 0

ch = int(input("\nEnter 1 to extract data from image:"))

if ch == 1:
    password1 = input("\nRe-enter password for Decryption msg:")
    decrypt = ""

    if password == password1:
        for i in range(len(msg)):
            decrypt = decrypt + c[img[n, m, z] ^ d[password[kl]]]
            n = n + 1
            m = m + 1
            m = (m + 1) % 3
            kl = (kl + 1) % len(password)

        print("Decryption message:", decrypt)
    else:
        print("password doesn't matched ")
        


