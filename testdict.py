#birthdays = {"Alice": "Apr 1", "Bob": "Dec 12", "Carol": "Mar 4"}

# while True:
#     print('Enter a name: (blank to quit)')
#     name = input()
#     if name == '':
#         break

#     if name in birthdays:
#         print(name, '\'s birthday is ', birthdays[name])
#     else:
#         print('I do not have birthday info for ', name)
#         print('What is their birthday?')
#         birthday = input()
#         birthdays[name] = birthday
#         print('Birthday DB Updated')

# for v in birthdays.values():
#     print(v)
# for k in birthdays.keys():
#     print(k)
# for i in birthdays.items():
#     print(i)

# print('Alice' in birthdays, 'Apr 1' in birthdays)
# for k, v in birthdays.items():
#     print('Key:', k, ' Value: ', v)

#print(birthdays.get('Alice4',0))

stuff = {'rope':1,'gold coin':42}

def displayInventory(inventory):
    print('Inventory:')
    totalItemNum = 0
    for k, v in stuff.items():
        print(v, ' ', k)
        totalItemNum += v
    print('Total number of items: ', totalItemNum)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1

addToInventory(stuff, dragonLoot)
displayInventory(stuff)