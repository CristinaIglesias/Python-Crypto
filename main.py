import hashlib  

class HASH:
    def generateHash(h):
        digest = h.hexdigest()
        return digest
x = 0
while x < 1:
    print("Choose the option of the algorithm to use:")
    print("1-SHA256")
    print("2-SHA512")
    print("3-Finish the program")
    typeAlgoritm = int(input())

    print("Enter the data to be hashed:")
    data= input()

    algoritm = ""
    if typeAlgoritm !=3:

        if typeAlgoritm == 1: 
            algoritm = "sha256"
        elif typeAlgoritm==2:
            algoritm= "sha512"
        database= bytes(data,"utf-8")
        h = hashlib.new(algoritm,database)
        hash1= HASH.generateHash(h)
        print()
        print(hash1)
        print()
        x=0
    else:
        x=1
    print("End")
