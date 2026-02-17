logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_txt, shift_amt, dir):
    if dir=="encode":
        shift_amt=shift_amt*1
    elif dir=="decode":
        shift_amt=shift_amt*-1
    text=""
    for char in plain_txt:
        if char in alphabet:
            pos=alphabet.index(char)
            newpos=pos+shift_amt
            new_letter=alphabet[newpos]
            text=text+new_letter
        else:
            text=text+char
    print(f"The {dir}d text is {text}")    
       
        




end=False
while end==False:
    direction=input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n")
    message=input("Type your message:\n").lower()
    shift=int(input("Type the number of shifts: "))
    shift=shift%26
    caesar(plain_txt=message, shift_amt=shift,dir=direction)    
    choice=input("Do you want to continue? (Y/N)\n").lower()
    if choice=="y":
        end=True
    elif choice=="n":
        end=False
        print("\n")
    
        