class DeliveryFood:
    def __init__(self,name1,phone1,address1, *items1):
        self.name = name1
        self.phone = phone1
        self.address = address1
        self.items = items1

    def cust_details(self, name, phone, address):
        print("Customer Name        :",name)
        print("Customer Phone       :",phone)
        print("Customer Address     :",address)

    def cust_order(self, *items):
        print("Customer Order       :",items)

    def cust_bill(self, *items):
        billamt = 0
        for idx in items:
            if idx == "dosa":
                billamt = billamt + 150
            if idx == "vada":
                billamt = billamt + 50
            if idx == "idli":
                billamt = billamt + 75
        print("Customer Bill Amount : Rs.",billamt,"/-")
        return billamt

arul = DeliveryFood("Anand","9841312855","Pazhavanthangal",('dosa','vada','idli'))
arul.cust_details("Anand","9841312855","Pazhavanthangal")
arul.cust_order('dosa','vada','idli')
arul.cust_bill('dosa','vada','idli')
