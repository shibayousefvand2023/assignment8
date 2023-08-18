


name1 = ('Welcome to Shiba store')
print(name1)

Item_ID = input('Enter Item ID:')
name = input('Enter name Item:')
price = float(input('Enter Item price:'))
amount = int(input('Enter Item amount:'))
search_ID = input('Enter Item ID:')
edit_ID= input('Enter edit_ID:')

goods =[]

def add_Item():
    Item_ID = input('Enter Item ID:')
    name = input('Enter name Item:')
    price = float(input('Enter Item price:'))
    amount = int(input('Enter Item amount:'))

    with open("Task.txt", "a") as file:
        file.write(f'{Item_ID}, {name}, {price}, {amount}\n')
print('Item added seccusfuly.')


def search_Item():
    search_ID = input('Enter Item ID to search:')

    with open("Task.txt", "r") as file:
        for line in file: 
            Item = line.strip().split('.')
            if Item[0] == search_ID:
                print('The desired item was found:')
                print('ID:', Item[0])
                print('name:', Item[1])
                print('price:', Item[2])
                print('amount:', Item[3])
                return
print('The desired item was not found.')

def edit_Item():
    edit_ID= input('Enter item_ID to edit:')
    updated_Items = []

    with open("Task.txt", "r") as file:
        for line in file: 
            Item = line.strip().split('.')
            if Item[0] == edit_ID:
                name = input('Enter new name:')
                price = float(input('Enter new price:'))
                amount = int(input('Enter new amount:'))
                Item = [Item[0], name, price, amount]
                print('Item edited seccusfuly.')
                updated_Items.append(Item)

    with open("Task.txt", "w") as file:
        for Item in updated_Items:
            file.write('.'.join(str(i)for i in Item)+'\n')
            print('The desired item was not found.')

def delete_Item():
    delete_ID = input('Enter Item_ID to delete:')
    deleted = False

    with open("Task.txt", "r") as file:
        lines = file.readlines()

    with open("Task.txt", "w") as file:
        for line in lines:
            Item = line.strip().split('.')
            if Item[0] != delete_ID:
                file.write('\n'+line)
            else:
                deleted = True
    if deleted:
        print('Item deleted seccusfuly.')
    else:
        print('The desired item was not found.')
dic = {}
def show_Items():
    file=open("Task.txt", "r")
    for line in file:
        goods = line.split('.')
        dic = {'ID:':goods[0], 'name:':goods[1], 'price:':goods[2], 'amount:':goods[3]}
        goods.append(dic)
    print('The desired items have been saved:')
    for object in goods:
        print(object)

def exit_app():
    print('Exiting the app ...')
    exit()

while True:
    print('Menu:')
    print('1, add Item')
    print('2, search Item')
    print('3, edit Item')
    print('4, delete Item')
    print('5, show Items')
    print('6, exit')

    user_choice = input('Enter your choice between (1-6):')
    if user_choice== '1':
        add_Item()
    elif user_choice== '2':
        search_Item()
    elif user_choice== '3':
        edit_Item()
    elif user_choice== '4':
        delete_Item()
    elif user_choice== '5':
        show_Items()
    elif user_choice== '6':
        exit_app()
    else:
        print('Wrong selection. please try again.')