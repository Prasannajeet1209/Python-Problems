b=(input("Enter Name "))
a =(int(input("Enter salary")))
if a>75000:
    da=int((a*30)/100)
    ta=int((a*20)/100)
    hrs=int((a*10)/100)
    a=a+da+ta+hrs
    print("Total salary is equal to",a)
elif 60000<a<75000 :
    da=int((a*20)/100)
    ta=int((a*10)/100)
    hrs=int((a*5)/100) 
    a=a+da+ta+hrs
    print("Total salary is equal to",                                                                                                                                                                                 a)
elif 50000<a<60000 :
     da=int((a*15)/100)
     ta=int((a*5)/100)
     hrs=int((a*4)/100)
     a=a+da+ta+hrs
     print("Total salary is equal to",a) 
elif 40000<a<50000 :
    da=int((a*10)/100)
    ta=int((a*5)/100)
    hrs=int((a*2)/100)
    a=a+da+ta+hrs
    print("Total salary is equal to",a) 