import re
A = ['234','a2b3c4','abc','#2a$#b%c%561#']
for _ in A:
    new_string = '#' * len(re.sub(r'\D', '', _))
    print("given string:", _ ,"new string : ",new_string)