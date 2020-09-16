import math
def add_binary_nums(x, y): 
        max_len = max(len(x), len(y)) 
  
        x = x.zfill(max_len) 
        y = y.zfill(max_len) 
          
        # initialize the result 
        result = '' 
          
        # initialize the carry 
        carry = 0
  
        # Traverse the string 
        for i in range(max_len - 1, -1, -1): 
            r = carry 
            r += 1 if x[i] == '1' else 0
            r += 1 if y[i] == '1' else 0
            result = ('1' if r % 2 == 1 else '0') + result 
            carry = 0 if r < 2 else 1     # Compute the carry. 
          
        if carry !=0 : result = '1' + result 
  
        return result.zfill(max_len)

def complement(sum_bin):
    s1=""
    for i in range(len(sum_bin)):
        s=""
        for j in range(len(sum_bin[i])):
            if sum_bin[i][j]=="0":
                s=s+"1"
            else:
                s=s+"0"
        s1=s1+s
    return add_binary_nums(s1,"1")


def n2b(num):
    return "{0:b}".format(num)

def sign(x):
    s=""
    c=0
    if x<0:
        c=x*-1
    else:
        c=x
    l=n2b(c)
    n=math.floor(len(l)/4)+1
    s=(4*n-len(l))*"0"+l
    if x<0:
        return complement(s)
    return s

def asr(a,q,q0,n1):
    q0=q[len(q)-1]
    s=""
    c=""
    c=c+a[len(a)-1]
    s=s+a[0]*2
    for i in range(len(a)-2):
        s=s+a[i+1]
    for i in range(len(q)-2):
        c=c+q[i]
    c=c+q[len(q)-2]
    return [s,c,q0]

def bTd(binary): 

    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal 

def ba(n,m,m1,a,q,q0):
    q1=q[len(q)-1]
    n1=n
    while n>0:
        #print(q1+q0)
        if (q1+q0)=="01":
            a=add_binary_nums(a,m)
            if len(a)>n1:
                a=a[len(a)-n1:]
            action="A+M"
            print(n,a,q,q0,action)
            
        elif (q1+q0)=="10":
            a=add_binary_nums(a,m1)
            if len(a)>n1:
                a=a[len(a)-n1:]
            action="A-M"
            print(n,a,q,q0,action)
        
        n=n-1
        a,q,q0=asr(a,q,q0,n1)
        #print(a,q,q0)
        action="asr"
        print(n,a,q,q0,action)
        q1=q[len(q)-1]
        
    ans=a+q
    if ans[0]=="1":
        print("negative of")
        ans=complement(ans)
    print("the product is: ",ans)
    print("in decimal:",bTd(int(ans)))


print("Enter the multiplicant:")
m=int(input())
print("Enter the multiplier:")
q=int(input())
#decide answer's polarity
m=sign(m)
q=sign(q)



if len(q)!=len(m):
    if q[0]=="0":
        q="0"*(len(m)-len(q))+q
    else:
        q=("1"*(len(m)-len(q))+q)

m1=complement(m)


n=len(m)
a="0"*n
q0="0"

print("m:",m,"-m:",complement(m),"n: ",n,"q: ",q)

print("n", "A"," "*(n-1),"Q"," "*(n-1),"q0 Action")
print(n,a,q,q0,"initial")
ba(n,m,m1,a,q,q0)