from os import write


with open('referat.txt','r',encoding='utf-8') as f:
    content = f.read()
    print(len(content))
    print(len(content.split()))

with open('referat2.txt','w',encoding='utf-8') as a: 
    
    b=content.replace('.','!')
    a.write(b)
    print(b)