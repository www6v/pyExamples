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
        {"a": 1}, {"b": 2}, {"c": 3},
        {"d": 4}, {"e": 5}, {"f": 6},
        {"g": 7}
    ]
    output_list = merge_every_three_objects_to_one(input_list)
    print(output_list)
    # 
    # 