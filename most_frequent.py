def most_frequent():
    str1=input("Please enter a string:")
    d={}
    str1=str1.lower()
    for i in str1:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    newd =  sorted(d.items(), key=lambda kv: kv[1],reverse = True)
    for k,v in newd:
        s=str(v)
        print(k,"=",s.zfill(2))

most_frequent()
