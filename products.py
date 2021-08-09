#讀取檔案
#strip 刪除/n
#split 分隔指定字串
#continue 繼續(還在迴圈不過跳到下一迴)
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
    for line in f:
        if '商品，價格' in line:
            continue
        name, price = line.strip().split(',')
        products.append([name, price])
print(products)

# 讓使用者輸入
while True:
    name = input('請輸入商品名稱:')
    if (name == 'q'):
        break
    price = input('請輸入商品價格：')
    price = int(price)
    # p = []
    # p.append(name)
    # p.append(price) 複雜
    # p = [name, price] 稍微簡化
    products.append([name, price]) # 最簡化
print(products) 

# 印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品, 價格, \n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')