import binascii
from pathlib import Path
magic_dict={}

def magic_num(filepath):
    with open(filepath,'rb') as f:
        hex_string = binascii.hexlify(f.read(16)).decode('ascii')
    return hex_string

with open('magic_dictionary.txt','r') as f:
    for row in f:
        part=row.split()
        magic_dict[part[0]]=part[1]

def check(op_hex_string):
    with open('magic_dictionary.txt','r') as f:
        for row in f:
            part=row.split()
            if(op_hex_string.startswith(part[0])):
                if(Path(filepath).suffix.removeprefix('.').lower() != magic_dict[part[0]]):
                    print('(FLAG ON )  Filetype doesNOT match with the given extension.\n')
                   

                else:
                    print('Filetype matches with the given extension.\n')
                return magic_dict[part[0]]


print('\n')
print('--------------------------------------------------------------------------------------------')
print('\n')

filepath=input("Enter filepath: ")
print('\n')
print('--------------------------------------------------------------------------------------------')

print('\n')

print(f'Detected filetype : {check(magic_num(filepath))}')
print(f'file extension  : {Path(filepath).suffix.removeprefix('.').lower()}')
print('\n')

print(f'Raw Hex(16 bytes): {magic_num(filepath)}.....')

print('\n')
print('--------------------------------------------------------------------------------------------')

print('\n')






