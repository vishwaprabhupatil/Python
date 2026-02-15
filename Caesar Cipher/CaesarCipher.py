alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_txt, shift_amt, dir):
    if dir=="encode":
        shift_amt=shift_amt*1
    elif dir=="decode":
        shift_amt=shift_amt*-1
    text=""
    for letter in plain_txt:
        pos=alphabet.index(letter)
        newpos=pos+shift_amt
        new_letter=alphabet[newpos]
        text=text+new_letter
    print(f"The {dir}d text is {text}")    
       
        
direction=input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n")
message=input("Type your message:\n").lower()
shift=int(input("Type the number of shifts: "))
caesar(plain_txt=message, shift_amt=shift,dir=direction)
