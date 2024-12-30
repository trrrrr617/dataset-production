from get_answer_wenxinapi import answer_generate
import json
import random
from get_answer_localmodel import generate

prices = list(range(1000, 10001, 500))     # Max and Min prices


def get_nodes(request):   # 1as color, 2as company，3as KeyNeed
    getting_nodes = []
    with open(request, 'r', encoding="utf-8") as f:
        data = json.load(f)
    for objects in data:
        getting_nodes.append(objects)
    return getting_nodes


nodes_KeyNeed = get_nodes("basic_KeyNeed.json")
nodes_Color = get_nodes("basic_Color.json")
nodes_Company = get_nodes("basic_Company.json")

# there must be '111' in every string belongs to this file inorder to exchange the real price
# with open("basic_HighPrice.json", 'r', encoding="utf-8") as file_HighPrice:
#    data_HighPrice = json.load(file_HighPrice)
# with open("basic_LowPrice.json", 'r', encoding="utf-8") as file_LowPrice:
#    data_LowPrice = json.load(file_LowPrice)
for x in range(100):         # n times to run, in case error happen
    main_dic = []
    for j in range(5):             # to every simple
        example = {}
        history = ""
        emotion = random.choice(["开心", "平静", "焦虑", "急切"])
        money = random.choice(["较差", "尚可", "很好"])

        # to confirm low&high prices
        price_low = random.choice(prices)-500
        price_high = random.choice(prices)+500
        if price_low > price_high:
            a = price_low
            price_low = price_high
            price_high = a

        # confirm the order of five dimensions
        order = [1, 2, 3, 4, 5]
        random.shuffle(order)

        for i in range(5):
            history1 = history
            random_key = ""
            if_company = "但不要刻意提及厂家"
            if order[i] == 4:
                example[("question_angle"+str(i))] = "LowPrice"
                example[("entity" + str(i))] = str(price_low)
                history += "、最低价"
                random_key = "最低价"+str(price_low)
                # example[("question"+str(i))] = str(random.choice(list(data_LowPrice))).replace("111",str(price_low))
                # continue
            if order[i] == 5:
                example[("question_angle"+str(i))] = "HighPrice"
                history += "、最高价"
                example[("entity" + str(i))] = str(price_high)
                random_key = "最高价"+str(price_high)
                # example[("question"+str(i))] = str(random.choice(list(data_HighPrice))).replace("111",str(price_high))
                # continue
            if order[i] == 1:
                random_key = random.choice(nodes_KeyNeed)
                example[("question_angle"+str(i))] = "KeyNeed"
                history += "、特殊需求"
                example[("entity" + str(i))] = random_key
            if order[i] == 2:
                random_key = random.choice(nodes_Color)
                example[("question_angle"+str(i))] = "Color"
                history += "、颜色"
                example[("entity" + str(i))] = random_key
            if order[i] == 3:
                random_key = random.choice(nodes_Company)
                example[("question_angle"+str(i))] = "Company"
                history += "、生产公司"
                if_company = ""
                example[("entity" + str(i))] = random_key
            question = "请基于"+emotion+"情感提出一个关于你需要选配空调的诉求，表现出提出诉求的人经济条件"+money+"不要直接写出经济条件，诉求的目的是使得空调有以下属性："
            question = question+random_key
            question = question+("。注意！这个属性是最关键、最需要你在提问中表达出来的信息！目前已经有过关于"+history1+"的对话："
                                 "。请保持语义的连接顺畅，展开思路，写一个与众不同的提问。同时，我希望其中不要参杂表情包等内容，大约40字以内即可，请"
                                 "使用一些口语化的词进行生成！而不是过于追求华丽、优美、对仗。注意不要写的跟宣传口号那样！要写的更像用户正常的提问诉求"+if_company)

            answer = generate(question).replace('\"', '')
            example[("question"+str(i))] = answer
            print("完成第"+str(j+x*5)+"个数据中第"+str(i)+"个问题")
        main_dic.append(example)
    with open("final_data.json", 'r', encoding="utf-8") as final_data:
        data = json.load(final_data)
    data.append(main_dic)
    with open("final_data.json", 'w', encoding="utf-8") as final_data:
        json.dump(data, final_data, indent=4, ensure_ascii=False)


