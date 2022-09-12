items = int(input("Number of items :"))
shoppingList = dict()
for i in range(items):
    take_input = input(("Input item and price :"))
    temp = take_input.split(' ')
    shoppingList[temp[0]] = int(temp[1])
sort_list = sorted(shoppingList.items(), key=lambda x: x[1], reverse=False)
for i in sort_list:
    print(i[0], i[1])