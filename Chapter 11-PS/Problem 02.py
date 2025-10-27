class Animals:
    pass
class pets(Animals):
    pass
class dogs(pets):
    @staticmethod
    def berk():
       print ("bow bow!")
        

d = dogs()
d.berk()        