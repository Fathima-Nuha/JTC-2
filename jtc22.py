product=('Expresso','Cappuccino','Latte')
Add_on=('Milk','Cream','Latte')
p_name={'1':'Expresso','2':'Cappuccino','3':'Latte'}
add_on_name={'1':'Milk','2':'Cream','3':'Latte'}

class Menu:
    
    def __init__(self,product,Add_on):
        
        self.product=product
        self.Add_on=Add_on
        
    def __str__(self):
        return f'{self.product} {self.Add_on}'

class Card:
    def __init__(self):
        x=0
        self.menu_all=[]
        self.product=product
        self.add_on=Add_on
        for i in product:
            for j in Add_on:
                self.menu_all.append(Menu(i,j))
                print(f'{x+1}.{self.menu_all[x]}')
                x+=1
            
    def order(self):
        #checking for valid input
        while True:
            
            #taking product order
            products=int(input(f'Enter Product\n1.{self.product[0]}\n2.{product[1]}\n3.{product[2]}\n'))
            
            if products in [1,2,3]:
                break
            else:
                 print("\033[1;3m ENTER EITHER 1 2 OR 3 \033[0m")
                    
        #checking for valid input
        while True:
            
             #taking add_on order
            add_ons=int(input(f'Enter Add_On\n1.{self.add_on[0]}\n2.{Add_on[1]}\n3.{Add_on[2]}\n'))
            if products in [1,2,3]:
                break
            else:
                print("\033[1;3m ENTER EITHER 1 2 OR 3 \033[0m")
        
        #returns product and add_on input value 
        return(products,add_ons)

class Price():
    
    def __init__(self,products,add_ons):
        self.products=products
        self.add_ons=add_ons
        
    def price_items(self):
        
        #checking price along with the product and add_on value returned and returns the price
        
        if self.products==1: #if product is EXPRESSO
            if self.add_ons==1:
                price=60
                return price
            elif self.add_ons==2:
                price=75
                return price
            else:
                price=100
                return price
        
        if self.products==2:    #if product is CAPPUCCINO
            if self.add_ons==1:
                price=80
                return price
            elif self.add_ons==2:
                price=95
                return price
            else:
                price=125
                return price
        
        if self.products==3:  #if product is LATTE
            if self.add_ons==1:
                price=100
                return price
            elif self.add_ons==2:
                price=125
                return price
            else:
                price=150
                return price

# taking the order combining all the functions and classes , final logic!
def orders():
    # list for storing all the order names (coffee name)
    all_order=[]
    
    #list for storing all the price  corresponding to the order
    all_price=[]
    reply='Y'
    order=1
    
    # loop for ordering
    while reply=='Y':
    
    #order number
        print("\033[1;3m ORDER NO:\033[0m ",order)
        order+=1
        
        print("SELECT FROM THE BELOW MENU\n ")
        menu=Card()
        print("----------------")
        
        #input from user stored as products and add_ons
        products,add_ons=menu.order()

        #appending the order names to the all_order list
        all_order.append(Menu(p_name[str(products)],add_on_name[str(add_ons)]))
        
        #instance of Price class
        p=Price(products,add_ons)

        #p.price_items() will return the price of the coffee
        print(f" \033[1;3m Price for {Menu(p_name[str(products)],add_on_name[str(add_ons)])} is {p.price_items()} \033[0m")
        
        #price is appended to price list
        all_price.append(p.price_items())


        while True: 
            
            #asks for ordering more
            reply=input("\n Do you want to order more Y or N \n ")
            if reply in ['Y','N']: #checks if input is valid
                break
            else:
                print(f"\n Enter either \033[1;3m Y \033[0m or \033[1;3m N\033[0m")

    total_price=0
    
    print("\n \033[1;3m YOUR BILL IS\033[0m \n")
    
    for i in range(len(all_order)):
        
        print(f'\033[1;3m {i+1})\033[0m {all_order[i]} {all_price[i]} \n') #shos items ordered along with price
        
        total_price += all_price[i] #adding total price from the list of prices using for loop
        
    print(f"\033[1;3m TOTAL AMOUNT= {total_price} \033[0m ")   

#calling order() for the program
orders()
    
																	 
        
       