'''
list=[{"张三":1,"李四":2,"王五":3},
      {"张三":4,"李四":5,"王五":6},
      {"张三":7,"李四":8,"王五":9}
      ]
for item in list:
    lst=item["张三"]
    print(lst)
'''
radius = 25 # 圆的半径是25
area = 3.1415 * radius * radius # 输入计算圆面积的公式
print(area)
print("面积是：{:.2f}".format(area)) # 只输出两位小数