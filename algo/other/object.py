def merge_every_three_elements(input_list):
    result = []
    for i in range(0, len(input_list), 3):
        # 取当前三个元素，并用逗号连接
        merged = ",".join(input_list[i:i+3])
        result.append(merged)
    return result

# # 示例用法
# input_list = ["a", "b", "c", "d", "e", "f", "g"]
# output_list = merge_every_three_elements(input_list)
# print(output_list)  # 输出: ['a,b,c', 'd,e,f', 'g'] 

def merge_every_three_objects(input_list):
    result = []
    for i in range(0, len(input_list), 3):
        # 取当前三个元素，组成一个子列表
        merged = input_list[i:i+3]
        result.append(merged)
    return result


def merge_every_three_objects_to_one(input_list):
    result = []
    for i in range(0, len(input_list), 3):
        # 取当前三个元素
        group = input_list[i:i+3]
        # 合并为一个新对象（这里以字典为例）
        merged = {}
        for obj in group:
            merged.update(obj)
        result.append(merged)
    return result


def merge_every_three_objects_with_attributes(input_list):
    result = []
    for i in range(0, len(input_list), 3):
        group = input_list[i:i+3]
        merged = {
            "post_ids": ",".join(str(obj["post_id"]) for obj in group),
            "cleaned_contents": merge_attr(group)
        }
        result.append(merged)
    return result

def merge_attr(group):    
    return ",".join( "post_id:" + str(obj["post_id"]) + "," + "text:" + str(obj["cleaned_content"]) for obj in group   )


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
            "posts": json.dumps(content)  # 将内容转换为 JSON 字符串
        }
        result.append(merged)
    return result


if __name__ == "__main__":
    input_list = ["a", "b", "c", "d", "e", "f", "g"]
    output_list = merge_every_three_elements(input_list)
    print(output_list)  


    ids = output_list[0]
    idList = ids.split(',') 
    if(len(idList) > 0):
      id = idList[0]
    else:
      id = ''


    input_list = [{"a": 1}, {"b": 2}, {"c": 3}, {"d": 4}, {"e": 5}, {"f": 6}, {"g": 7}]
    output_list = merge_every_three_objects(input_list)
    print(output_list)


    # abc = ""
    t = [{'post_id': '1'}, {'post_id': "2"}, {'post_id': "3"}]       
    l = [t[i]['post_id'] for i in range(0, len(t))]   
    result = ",".join(l)

    print(result)   



    input_list = [
        {"post_id": 1}, {"post_id": 2}, {"post_id": 3},
        {"d": 4}, {"e": 5}, {"f": 6},
        {"g": 7}
    ]
    output_list = merge_every_three_objects_to_one(input_list)
    print(output_list)
    # 


    input_list = [
        {"post_id": 1, "cleaned_content": "content1"},
        {"post_id": 2, "cleaned_content": "content2"},
        {"post_id": 3, "cleaned_content": "content3"},
        {"post_id": 4, "cleaned_content": "content4"},
        {"post_id": 5, "cleaned_content": "content5"},
        {"post_id": 6, "cleaned_content": "content6"},
        {"post_id": 7, "cleaned_content": "content7"}
    ]
    output_list = merge_every_three_objects_with_attributes(input_list)
    print(output_list)

    print("--------------------------------")

    input_list = [
        {"post_id": 1, "cleaned_content": "content1"},
        {"post_id": 2, "cleaned_content": "content2"},
        {"post_id": 3, "cleaned_content": "content3"},
        {"post_id": 4, "cleaned_content": "content4"},
        {"post_id": 5, "cleaned_content": "content5"},
        {"post_id": 6, "cleaned_content": "content6"},
        {"post_id": 7, "cleaned_content": "content7"}
    ]
    output_list = merge_every_five_objects_to_json(input_list)
    print(output_list)   