def intToRoman(num: int) -> str:
    # I,V,X,L,C,D,M
    q = num//1000
    b = (num%1000)//100
    s = (num%100)//10
    g = (num%10)
    result = ""
    result = powS("M",q)
    result = result+ pj(b,"M","D","C")
    result = result+ pj(s,"C","L","X")
    result = result+ pj(g,"X","V","I")
    return result

def pj(num,up,half,down):
    result = ""
    if num>=5 and num<9:
        result = half+ powS(down,num-5)
    elif num>0 and num<4:
        result = powS(down,num)
    elif num == 9:
        result = down+up 
    elif num == 4:
        result =  down+half
    return result

def powS(s,n):
    result = ""
    for _ in range(0,n):
        result = result + s
    return result
if __name__ == "__main__":
    print(intToRoman(3900))