
IMPORT LIBRARIES => import hashlib  

WE CREATE A CLASS TO GENERATE A HASH

class HASH:
    def generateHash(h): FUNCTION 
        digest = h.hexdigest()   => RETURNS A STRING OBJECT WITH HEXADECIMAL DIGITS
        return digest  => RETURNS STRING OBJECT 
x = 0 
while x < 1:
    print("Choose the option of the algorithm to use:")
    print("1-SHA256")
    print("2-SHA512")
    print("3-Finish the program")
    typeAlgoritm = int(input())  * CHOOSE TYPE ALGORITHM 

    print("Enter the data to be hashed:") * DATA 
    data = input()

    algoritm = "" * TYPE ( 1 OR 2 )
    if typeAlgoritm !=3:

        if typeAlgoritm == 1: 
            algoritm = "sha256"
        elif typeAlgoritm==2:
            algoritm= "sha512"
        database= bytes(data,"utf-8")
        h = hashlib.new(algoritm,database) * takes the data of type algorithm and the text
        hash1= HASH.generateHash(h) * function class
        print()
        print(hash1)
        print()
        x=0
    else:
        x=1
    print("End")
