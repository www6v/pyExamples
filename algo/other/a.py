import json
def merge_every_five_objects_to_json(input_list):
    result = []
    for i in range(0, len(input_list), 5):
        group = input_list[i:i+5]
        content = [
            {"post_id": obj["post_id"], "text": obj["cleaned_content"]}
            for obj in group
        ]
        merged = {
            "post_ids": ",".join(str(obj["post_id"]) for obj in group),
            "posts": json.dumps(content, ensure_ascii=False)  # 将内容转换为 JSON 字符串
        }
        result.append(merged)
    return result

if __name__ == "__main__":
    input_list = [
        {"post_id": 1, "cleaned_content": "在麓镇圣诞集市，一天就卖空的玫瑰酒！谁懂啊真的很受欢迎 每天都能收到大家问见月白玫瑰酒什么时候补货 因为酿造周期的问题，大家等待了一段时间 现在！最新批次的玫瑰酒还有回来了！大家可以尽情享受微醺时刻了～ 一如既往地0添加！配料表比我脸都干净！ 玫瑰花和玫瑰茄再加上酒米发酵，带来无与伦比的玫瑰香甜！喝下玫瑰的芬芳～ 开瓶瞬间就能嗅到玫瑰的香气，就像在窗边留下一朵沾满露水的玫瑰花！发酵之后的米香完美的融入玫瑰的味道，回味还有一丝草木的清香！ 柔和，顺滑，自然，香甜 玫瑰香在嘴里持续回味～ 但是只有6度！非常适合微醺一下！而且喝法多样，可以冰镇直饮，可以煮酒！也可以加气泡水等等各种方式饮用！ #见月白米酒#今夜来一杯微醺酒#喝酒日常#新年礼物#适合过年喝的酒#适合女生喝的酒#断货王"},
        {"post_id": 2, "cleaned_content": "#零食推荐 #好吃到停不下来 #大人小孩都爱吃 #陈皮#陈皮红豆沙 这款五年新会陈皮搭配的水洗沙工艺，嘴巴轻轻一抿就化了。软糯香甜好爱，配料表只有饮用水、红豆、冰糖、莲子、陈皮。微甜不腻，更有陈皮的味道中和红豆软糯，莲子香甜。陈皮清香，味道层次丰富，入口爽滑细腻，滋补又养生！"},
        {"post_id": 3, "cleaned_content": "内容3"},
        {"post_id": 4, "cleaned_content": "内容4"},
        {"post_id": 5, "cleaned_content": "内容5"},
        {"post_id": 6, "cleaned_content": "内容6"},
        {"post_id": 7, "cleaned_content": "内容7"},
        {"post_id": 8, "cleaned_content": "内容8"},
        {"post_id": 9, "cleaned_content": "内容9"},
        {"post_id": 10, "cleaned_content": "内容10"},
        {"post_id": 11, "cleaned_content": "内容11"}
    ]
        

    # l = input_list[0]['result']  

    output_list = merge_every_five_objects_to_json(input_list)    

    print(output_list)


# def main(arg1: list) -> dict:
#     l = arg1[0]['result']  

#     output_list = merge_every_five_objects_to_json(l)    

#     return {
#         "result": output_list,
#     }
