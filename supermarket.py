supermarket = {}
cart = []


def add_product():
    name = input("Enter the product name: ")
    price = int(input("Enter the price: "))
    quantity = int(input("Enter stock: "))
    supermarket[name] = {'price' : price, 'quantity' : quantity}


def view_product():
    for name in supermarket:
        print("Name: ", name)
        for key in supermarket[name]:
            print(key,":", supermarket[name][key])
        print("\n")

def addToCart():
    pass

def checkout():
    pass

while True:
    print("\n1. Add Products \n2. View Product \n3. Add to cart \n4. Checkout")

    choice = int(input("\nEnter your choice: "))
    print("\n")

    if choice == 1:
        add_product()
    elif choice == 2:
        view_product()
    elif choice == 3:
        addToCart()
    elif choice == 4:
        checkout()
    else:
        print("invalid choice")
        