'''Python 登入驗證與多功能選單練習程式'''

'''使用技術：if／elif／else、for 迴圈、巢狀迴圈、list、input'''

from sys import exit
account="123"
password="456"


acc=input("請輸入你的帳號")
pwd=input("請輸入你的密碼")

if(acc==account) and (pwd==password):
    
    print("登入成功")
    
    op=int(input("請輸入您要執行的程式:0.離開、1.BMI、2.華氏與攝氏換算、3.99乘法表、4.收銀系統、5.撲克牌總和、6.位數加總、7.階乘計算、8.簡易算術運算"))

    if(op==1):
        print("執行BMI程式")
        name=input("請輸入姓名:")

        s1h=float(input("請輸入"+name+"身高cm"))

        s1w=float(input("請輸入"+name+"體重kg"))

        s1h=s1h/100

        bmi=s1w/pow(s1h,2)
        print("hi,"+name+"你的BMI="+str(bmi))
    elif(op==2):
        print("執行華氏轉攝氏")
        c=float(input("請輸入攝氏"))
        f=c*9/5+32
        print("華氏",f,"度")

        f1=float(input("請輸入華氏"))
        c1=(f1-32)*5/9
        print("攝氏",c1,"度")
    elif(op==3):
        print("99乘法表")
        for x in range(1,10):
            for y in range(1,10):
                #print("x=",x)
                #print("y=",y)
                z=x*y
                print(x,"*",y,"=",z)
    elif(op==4):
        print("收銀系統")
        print("請輸入品名")
        name=input()

        num=int(input("請輸入數量")) #3
        price=int(input("請輸入價錢")) #100

        total=num*price

        print("您購買的是",name,"，單價為",price,"元，數量為",num,"個，總價為",total,"元")
        
    elif(op==5):
        print("撲克牌總和")
        quantity = int(input("請輸入欲計算的張數"))
        cards = []
        for i in range(quantity):
            x = input()
            if x == "A":
                x = 1
            elif x == "J":
                x = 11
            elif x == "Q":
                x = 12
            elif x == "K":
                x = 13
            cards.append(int(x))
        print(sum(cards))
        
    elif(op==6):
        print("位數加總")
        n = int(input("請輸入欲位數加總的次數"))
        for i in range(n):
            s = input("請輸入欲計算的數字")
            total = sum(int(x) for x in s)
            print(f"{s} 的位數加總是 {total}")
    elif(op==7):
        print("階乘計算")
        n = int(input("請輸入欲階乘計算的數字"))
        a = 1
        for i in range(1, n + 1):
            a *= i
        print(f"{n} 的階乘計算結果是 {a}")
    elif(op==8):
        print("簡易算術運算")
        a = int(input("請輸入想計算的數字一"))
        b = int(input("請輸入想計算的數字二"))
        op = input("請輸入運算子，如：+(加)、-(減)、*(乘)、/(除)和%(兩者相除的餘數)")
        if op == "+":
            print(a + b)
        elif op == "-":
            print(a - b)
        elif op == "*":
            print(a * b)
        elif op == "/":
            if b == 0:
                print("除數不能為 0")
            else:  
                print(a / b)
        elif op == "%":
            if b == 0:
                print("除數不能為 0")
            else:
                print(a % b)
    elif(op == 0):
        print("程式結束")
        exit()
    else:
        print("輸入錯誤，請輸入 0 到 8。")
            

elif(acc==""):
    print("你的帳號為空")
    exit()
elif(pwd==""):
    print("你的密碼為空")
    exit()
elif(acc!=account):
    print("帳號錯誤")
    exit()
elif(pwd!=password):
    print("密碼錯誤")
    exit()

else:
    exit()
    
'''專案成果：將帳密驗證、數字選單與八項 Python 練習功能整合於同一支程式。'''
'''原始碼：請參閱 104 專案連結中的 GitHub Repository。'''