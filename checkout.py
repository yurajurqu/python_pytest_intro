class Checkout:
    class Discount:
        def __init__(self,nbrItems,price):
            self.nbrItems = nbrItems
            self.price = price
    def __init__(self):
        self.prices = {}
        self.items = {}
        self.discounts = {}
    def addItemPrice(self, item, price):
        self.prices[item] = price
    def addItem(self, item):
        if item not in self.prices:
            raise Exception('Bad item')
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculateItemTotal(self, item, cnt):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if cnt >= discount.nbrItems:
                total += self.calculateItemDiscountedTotal(item,cnt,discount)
            else:                    
                total += self.prices[item] * cnt
        else:                    
            total += self.prices[item] * cnt
        return total

    def calculateTotal(self):
        total = 0
        for item, cnt in self.items.items():
            total += self.calculateItemTotal(item,cnt)
        return total
    def addDiscount(self,item,nbrOfItems,price):
        discount = self.Discount(nbrOfItems, price)
        self.discounts[item] = discount
        
    def calculateItemDiscountedTotal(self, item, cnt, discount):
        nbrOfDiscounts = cnt // discount.nbrItems
        remaining = cnt % discount.nbrItems
        return nbrOfDiscounts * discount.price + remaining * self.prices[item]
        