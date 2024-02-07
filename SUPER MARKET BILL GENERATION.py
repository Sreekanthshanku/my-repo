# CM SUPER MARKET BILL GENERATE

from datetime import datetime
print("          Welcome          ")
name = input(" Enter your name: ")

# List of items
Lists = '''
rice         Rs 50/kg, 
sugar        Rs 42/kg, 
oil          Rs 110/pkt, 
salt         Rs 20/kg, 
colgate      Rs 10/each, 
maggie       Rs 10/each
'''
# Declaration
price = 0
pricelist = []
totalprice = 0
Finalfinalprice = 0
ilist = []
qlist = []
plist = []

# Rates for items
items = { 'rice':50, 'sugar':20, 'oil':110, 'salt':20, 'colgate':10, 'maggie':10 }
option = int(input(" for all list of items press 1: "))
if option == 1:
    print(Lists)
for i in range (len(items)):
    inp1 = int(input(" if you want to buy press 1 or 2 for exit: "))
    if inp1 == 2:
        break
    if inp1 == 1:
        item = input("Enter your items:")
        quantity = int(input("Enter quantity:"))
        if item in items.keys():
            price = quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print(" Sorry you entered item is not available ")
    else:
        print(" You entered wrong number ")
    inp = input(" Can i bill the items Yes or No : ")
    if inp == 'yes':
        pass
        if finalamount !=0:
                print(75*"-")
                print(25*"=", " CM SUPER MARKET", 25*"=")
                print(25*" ", " YADADRIBHONGIR ")
                print(10*" ")
                print("Name:",name,30*" ","Date:",datetime.now())
                print(75*"-")
                print("sno",10*" ","items",8*" ",'Quantity',12*" ",'price',8*" ")
                for i in range(len(pricelist)):
                        print(i,8*' ',5*' ',ilist[i],10*' ',qlist[i],12*' ',plist[i])
                print(75*"-")
                print(50*" ","TotalAmount:",'Rs','totalprice')
                print("gst amount",50*" ",'Rs','gst')
                print(75*"-")
                print(50*" ","finalAmount:",'Rs','finalamount')
                print(75*"-")
                print(20*" ", " Thanks for visiting " )
                print(75*"-")


