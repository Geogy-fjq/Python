#储存库存信息和销售记录的商品的基本信息
def StoreStock():
    StockList=open("Stock","w")
    MarketList=open("Market","w")
    a=0
    while a==0:
        name=str(input("输入商品名称:"))
        price=str(input("输入商品单价:"))
        amount=str(input("输入商品数量:"))
        number=str(input("输入商品编号:"))
        sell=str(0)
        MarketList.write("|名称:|"+name+"|单价:|"+price+"|售出数量:|"+sell+"|\n")
        StockList.write("|名称:|"+name+"|单价:|"+price+"|数量:|"+amount+"|编号:|"+number+"|\n")
        a=eval(input("输入0继续储存商品信息；输入其他数字结束储存："))
    else:
        print("储存完毕.")
    StockList.close()
    MarketList.close()
    print("                       #记录完毕#")
    print()
    print()
    return StockList,MarketList
#收银(输入商品名称和购买数量，显示单价和总价格，储存销售记录和更改库存)
def Market():
    StockList=open("Stock","r+")
    name2=str(input("输入该商品名称:"))
    n=int(input("输入卖出或退换的商品数量（卖出a件输入a;退还a件输入-a）:"))
    for line in StockList:
        c=line.split("|")
        if c[2]==name2:
            print("【",c[1],c[2],c[3],c[4],"】")
            c[4]=int(c[4])
            Total=c[4]*n
            print("【单价是：",c[4],"；总价格是:",Total,"】")
            c[4]=str(c[4])
            c[6]=int(c[6])
            c[6]=c[6]-n
            c[6]=str(c[6])
            line="|".join(c)
            StockList.writelines(line)
    StockList.close()
    MarketList=open("Data/Market","r+")
    for line1 in MarketList:
        d=line1.split("|")
        if d[2]==name2:
            d[6]=int(d[6])
            d[6]=d[6]+n
            d[6]=str(d[6])
            line1="|".join(d)
            MarketList.writelines(line1)     
    MarketList.close()
    return MarketList,StockList
    print("                       #收银完毕#")
    print()
    print()
#查看库存信息(个别和所有两种查看方式)
def SearchStock():
    StockList=open("Data/Stock","r")
    k=eval(input("输入0查看个别商品库存信息；输入1查看所有商品库存信息："))
    if k==0:
        name1=str(input("输入查找的商品名称:"))
        for line in StockList:
            c=line.split("|")
            if c[2]==name1:
                print("【",c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],"】")
    if k==1:
        for line in StockList:
            c=line.split("|")
            print("【",c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],"】")
    StockList.close()
    print("                     #查看库存完毕#")
    print()
    print()
#查看销售记录(个别和所有两种查看方式)
def SearchMarket():
    MarketList=open("Market","r")
    k=eval(input("输入0查看个别商品销售记录；输入1查看所有商品销售记录："))
    if k==0:
        name3=str(input("输入查找的商品名称:"))
        for line1 in MarketList:
            e=line1.split("|")
            if e[2]==name3:
                print("【",e[1],e[2],e[3],e[4],e[5],e[6],"】")
    if k==1:
        for line1 in MarketList:
            e=line1.split("|")
            print("【",e[1],e[2],e[3],e[4],e[5],e[6],"】")
    MarketList.close()
    print("                   #查看销售记录完毕#")
    print()
    print()
#计算总收入
def Income():
    MarketList=open("Market","r")
    income=0
    for line1 in MarketList:
        d=line1.split("|")
        d[4]=int(d[4])
        d[6]=int(d[6])
        income=d[4]*d[6]
        d[4]=str(d[4])
        d[6]=str(d[6])
    print("【总收入:",income,"yuan】")
    MarketList.close()
    print("                     #计算总收入完毕#")
    print()
    print()
#打印菜单
def main():
    print("                      |*&* 菜单 *&*|   ")
    print("                  |储存库存信息------1|")
    print("                  |收银--------------2|")
    print("                  |查看库存信息------3|")
    print("                  |查看销售记录------4|")
    print("                  |查看总收入--------5|")
    print("                  |结束--------------0|")
    Do=eval(input("数字对应功能，请输入你的数字："))
    print()
    print()
    while Do==0 or Do==1 or Do==2 or Do==3 or Do==4 or Do==5:
        if Do==1:
            print("                    【储存库存信息】  ")
            StoreStock()
        elif Do==2:
            print("                      【开始收银】    ")
            Market()
        elif Do==3:
            print("                    【查看库存信息】  ")
            SearchStock()
        elif Do==4:
            print("                    【查看销售记录】  ")
            SearchMarket()
        elif Do==5:
            print("                     【查看总收入】   ")
            Income()
        else:
            print("                      欢迎再次使用！  ")
        print()
        print()
        print("                      |*&* 菜单 *&*|   ")
        print("                  |储存库存信息------1|")
        print("                  |收银--------------2|")
        print("                  |查看库存信息------3|")
        print("                  |查看销售记录------4|")
        print("                  |查看总收入--------5|")
        print("                  |结束--------------0|")
        Do=eval(input("数字对应功能，请输入你的数字："))
main()


