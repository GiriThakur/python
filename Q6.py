num= int(input("Enter three digit number"))
digit =[ ]
while num>0:
    digit.append(num%10)
    num=int(num/10)
sum=digit[0] **3 + digit[1] **3 + digit[2] **3
print(sum)
    
