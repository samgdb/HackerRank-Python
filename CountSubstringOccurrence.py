def count_substring(string, sub_string):
    if (1<=(len(string))<=200):
        count=0
        ls,lss = len(string),len(sub_string)
        for i in range(0,ls-lss+1):
            if string[i:i+lss] == sub_string:
                count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
