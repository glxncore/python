fruits=['APPLE','ORANGE','GRAPES']
vegetable=['TOMATO','ONION','CARROT']
beverage=['COLA','PEPSI','SPRITE']
print(fruits,'\n',vegetable,'\n',beverage)

fruits.append("BANANA")
print(fruits)

vegetable.insert(1,"POTATO")
print(vegetable)

del beverage[2]
print(beverage)


inventory = [fruits, vegetable, beverage]
print(inventory)
print(fruits[:2])
print(vegetable[-1:])
lengthh=[len(x) for x in fruits]
print(lengthh)
print("water" in beverage)


first_items = (fruits[0], vegetable[0], beverage[0])

print(first_items)