def swap_case(s):
    if (0<len(s)<=1000):
        str=''
        for i in s:
            if (i==i.upper()):
                str+=i.lower()
            elif(i==' '):
                pass
            else:
                str+=i.upper()
    return str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
