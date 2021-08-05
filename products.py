products = []
while True:
    name = input('請輸入商品名稱:')
    if (name == 'q'):
        break
    price = input('請輸入商品價格：')
    # p = []
    # p.append(name)
    # p.append(price) 複雜
    # p = [name, price] 稍微簡化
    products.append([name, price])
print(products) 