class Ingredient:
    def __init__(self,name,shelfLife,doesExpire,quantity,quantityUnit):
        self.doesExpire = doesExpire
        self.name = name
        self.shelfLife = shelfLife
        self.quantity = quantity
        self.quantityUnit = quantityUnit
