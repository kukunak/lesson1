price = 100
discount = 5
price_with_discount = price - price * discount / 100
print (price_with_discount)

def discounted(price, discount):
    price = abs(float(price))
    discount = abs(float(discount))
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    return (price_with_discount)
discounted(100, 50)
discounted(600, -33)
discounted(600, 105)
p = discounted(600, 33)
print(p)

product = {
    "name": "iPhone Xs", 
    "stock": 32, 
    "price": 66000.12,
    "discount": 50
    }
product ['with_discount'] = discounted(product['price'], product['discount'])
print(product)

def discounted(price, discount, max_discount = 50):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('максимальная скидка на может быть больше 99%')
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    return (price_with_discount)

product ['with_discount'] = discounted(product['price'], product['discount'])
print(product) # не выполнено условие
product ['with_discount'] = discounted(product['price'], product['discount'], max_discount=90)
print(product)
discounted(400, 50, max_discount=100) 