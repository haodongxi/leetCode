def romanToInt(s: str) -> int:
    i = 0
    sum=0
    while(i<len(s)):
        tempUp = s[i+1] if i+1<len(s) else "O"
        sub_s = s[i]
        if sub_s=="M":
            sum=sum+1000
            i=i+1
        elif sub_s=="D":
            sum=sum+500
            i=i+1
        elif sub_s=="C":
            if tempUp=="D":
                sum=sum+400
                i=i+2
            elif tempUp=="M":
                sum=sum+900
                i=i+2
            else:
                sum=sum+100
                i=i+1
        elif sub_s=="L":
            sum=sum+50
            i=i+1
        elif sub_s=="X":
            if tempUp=="L":
                sum=sum+40
                i=i+2
            elif tempUp=="C":
                sum=sum+90
                i=i+2
            else:
                sum=sum+10
                i=i+1
        elif sub_s=="V":
            sum=sum+5
            i=i+1
        elif sub_s=="I":
            if tempUp=="V":
                sum=sum+4
                i=i+2
            elif tempUp=="X":
                sum=sum+9
                i=i+2
            else:
                sum=sum+1
                i=i+1
        else:
            i= i+1
    return sum

if __name__ == "__main__":
    print(romanToInt("MMMM"))