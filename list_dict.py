#списки 
phones = ["iPhone XS", "Samsung GalaxyS10", "XiaomiMi8", "iPhone XS"]
print (phones)
print (len (phones))
phones.append ("Acer x")
print (phones)
print (phones.count("Acer x"))
print (phones.count("acer x"))
print (phones[0])
print (phones[3])
print (phones[1:3])
print (phones[1:])
print (phones[:2])
print (phones[:-1])
print (phones[::-1])
print (phones.index("Acer x"))
print (phones[1])
phones.sort()  #работает только для данных одноготипа, сначала сортирует заглавные после строчные
print (phones)
print ("Acer x" in phones) # проверяет нахождение в списке элемента и выводит True или False
del phones[3]
print (phones)
phones.remove ("Acer x")
print (phones)
#словари
product = {
    "name": "iPhone Xs", 
    "stock": "32", 
    "price": "66000.12"
    }
print (product)
print (len(product))
product["stock"] = 26
print (product)
product ["memory"] = 64
print (product)
print (product["name"])
print (product.get("name")) 
print (product.get("NAME")) # не останавливает программу из-зи ошибки,вернет None
print (product.get("discount", 0))
del product ["memory"] #удалить элемент
print (product)
product ["recomend"] = phones
print (product)
print (product ["recomend"] [1])
product ["recomend"].append ("Nokia 3310")
print (product)
top = [
    {'name': 'iPhone Xs Plus', 'stock': 26, 'price': '66000.12', 'recomend': ['Samsung GalaxyS10', 'XiaomiMi8', 'iPhone XS', 'Nokia 3310']}, 
    {'name': 'Samsung GalaxyS10', 'stock': 6, 'price': '60000.2'}, 
    {'name': 'XiaomiMi8', 'stock': 13, 'price': '35231.772'},
    ]
print (top)
print (top[0])
print (top[0]['price'])
top[0]['price'] = float(top[0]['price']) + float(top[1]['price'])
print (top[0]['price'])
print (top)
print (top[0]['recomend'][0:2])
print(type(top))
print(type(product))
print(type(top[1]))




