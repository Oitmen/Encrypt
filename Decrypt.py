import os
import glob

def decrypt(filename, key):
    file = open(filename, "rb").read()
    key = open(key, "rb").read()
    decrypt = bytes(a ^ b for (a, b) in zip(file, key))
    with open(filename, "wb") as decrypt_out:
        decrypt_out.write(decrypt)


allpng = glob.glob(r"\Your Pfad\*.*")
keyl = glob.glob(r"\Your Pfad\*.*.key")


l = len(allpng)
l = l-1
x = 0

while l >= x :

    a = int(x/2)
    png = allpng[x]
    key = keyl[a]

    if png == key:

        x = x +1
    else:
        
        pngs = png+".key"

        decrypt(png, pngs)


        os.remove(pngs)

        x = x +1
