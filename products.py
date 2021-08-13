#讀取檔案
#strip 刪除/n
#split 分隔指定字串
#continue 繼續(還在迴圈不過跳到下一迴)

import os #operating system
#讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品, 價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products

# 讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱:')
        if (name == 'q'):
            break
        price = input('請輸入商品價格：')
        # p = []
        # p.append(name)
        # p.append(price) 複雜
        # p = [name, price] 稍微簡化
        products.append([name, price]) # 最簡化
    print(products)
    return products

# 印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])

# 寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品, 價格, \n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')

def main():
    filename = 'products.csv'
    if os.path.isfile(filename): #檢查檔案在不在
        print('yeah! 找到檔案了!')
        products = read_file(filename)
    else:
        print('找不到檔案')

main()
products = read_file('products.csv')
products = user_input(products)
print_products(products)
write_file('products.csv', products)


