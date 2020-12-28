class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to " +self.name+ " " + self.lastName + "'s cart")


customer1 = Customer()
customer1.name = "Bob"
customer1.lastName = "Baby"
customer1.age = 8
customer1.addCart()

customer2 = Customer()
customer2.name = "Michale"
customer2.lastName = "Jordan"
customer2.age = 30
customer2.addCart()

customer3 = Customer()
customer3.name = "Lebron"
customer3.lastName = "James"
customer3.age = 38
customer3.addCart()

customer4 = Customer()
customer4.name = "Stephen"
customer4.lastName = "Curry"
customer4.age = 27
customer4.addCart()
