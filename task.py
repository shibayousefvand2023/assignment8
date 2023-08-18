products =[]

def read_data():
    f = open("task1.txt", "r")
    for l in f:
        dic = {}
        # print(l)
        result = l.split(",")
        dic = {'id':result[0], 'name':result[1], 'price':result[2], 'count':result[3]}
        print(dic)
        # print(result[4])
        products.append(dic)


def show_manu():
    print('1_ add')
    print('2_delete')
    print('3_search')
    print('4_buy')
    print('5_edit')
    print('6_exit')
    print('7_show_menu')

def add():
    id= input('Enter id:')
    name=input('Enter name:')
    price=input('Enter price:')
    count=input('Enter count:')

dic = {'id':id, 'name':name, 'price':price, 'count': count}
products.append(dic)
print(products)
def search():
    key= input('Enter your key:')
    for product in products:
        if key == product['id'] or key == products['name']:
            print(product)
            break
    else:
        print('not found')


def delete():
    pass
def buy():
    pass
def edit():
    pass
def exit():
    pass
def show_product():
    print("id'/t name /t price /t count")
    for product in products:
        print(product['id'], '/t', product['name'], '/t')
        print(f{product['id'], '/t'})

read_data()
show_manu()
user_choice = int(input('Enter your choice:'))
if user_choice== 1:
    add()
elif user_choice== 2:
    delete()
elif user_choice== 3:
    search()
elif user_choice== 4:
    buy()
elif user_choice== 5:
    edit()
elif user_choice== 6:
    exit()
elif user_choice== 7:
    show_manu()





# print(product)