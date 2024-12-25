import json
import random

main_dic = []
prices = list(range(1000, 10001, 500))

with open("basic_KeyNeed.json", 'r', encoding="utf-8") as file_KeyNeed:
    data_KeyNeed = json.load(file_KeyNeed)
with open("basic_Color.json", 'r', encoding="utf-8") as file_Color:
    data_Color = json.load(file_Color)
with open("basic_Company.json", 'r', encoding="utf-8") as file_Company:
    data_Company = json.load(file_Company)
with open("basic_HighPrice.json", 'r', encoding="utf-8") as file_HighPrice:  # 这个文件中必须存在“111”以替换成实际价格
    data_HighPrice = json.load(file_HighPrice)
with open("basic_LowPrice.json", 'r', encoding="utf-8") as file_LowPrice:
    data_LowPrice = json.load(file_LowPrice)
for j in range(500):
    example = {}
    price_low = random.choice(prices)
    price_high = random.choice(prices)
    if price_low > price_high:
        a = price_low
        price_low = price_high
        price_high = a

    order = [1, 2, 3, 4, 5]
    random.shuffle(order)
    for i in range(5):
        if order[i] == 1:
            random_key = random.choice(list(data_KeyNeed.keys()))
            example[("question"+str(i))] = random.choice(data_KeyNeed[random_key]).replace('\"', '')
            example[("question_angle"+str(i))] = "需求"
            example[("entity" + str(i))] = random_key
        if order[i] == 2:
            random_key = random.choice(list(data_Color.keys()))
            example[("question"+str(i))] = random.choice(data_Color[random_key]).replace('\"', '')
            example[("question_angle"+str(i))] = "颜色"
            example[("entity" + str(i))] = random_key
        if order[i] == 3:
            random_key = random.choice(list(data_Company.keys()))  # 这里选择了用哪个目标词
            example[("question"+str(i))] = random.choice(data_Company[random_key]).replace('\"', '')
            example[("question_angle"+str(i))] = "厂家"
            example[("entity" + str(i))] = random_key
        if order[i] == 4:
            example[("question"+str(i))] = str(random.choice(list(data_LowPrice))).replace("111",str(price_low))
            example[("question_angle"+str(i))] = "最低价格"
            example[("entity" + str(i))] = str(price_low)
        if order[i] == 5:
            example[("question"+str(i))] = str(random.choice(list(data_HighPrice))).replace("111",str(price_high))
            example[("question_angle"+str(i))] = "最高价格"
            example[("entity" + str(i))] = str(price_high)

    main_dic.append(example)
with open("final_data.json",'w',encoding="utf-8") as final_data:
    json.dump(main_dic, final_data, indent=4, ensure_ascii=False)
