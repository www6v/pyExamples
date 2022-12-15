import json
import pandas as pd

if __name__ == '__main__':
    with open('abc.json','r') as f:
       data = json.loads(f.read())
    df_nested_list = pd.json_normalize(data, record_path =['students'])		# 指定输出 student 项目下的内容
    print(df_nested_list)







