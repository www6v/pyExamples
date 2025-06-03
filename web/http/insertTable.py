import pymysql

# 创建数据库连接
db = pymysql.connect(
    host="rm-uf6h6n62xt2qw5jvkjo.mysql.rds.aliyuncs.com",
    user="admin_apple",
    password="UOIwjVe7rPMcULqMCkg0H",
    database="apple"
)

cursor = db.cursor()

sql = "insert into validated_success_data(run_id,openai_id,prompt_tokens,completion_tokens,total_tokens,model,created,content,finish_reason,data_id,prompt, source_response,start_request_time,end_request_time) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
values = ("run_id-1", 'openai_id-1', 300, 300, 500, 'qwenPlus', '2024-11-21 19:57:19' ,'mock content', 'stop', 'data_id-1', 'mock-prompt', 'mock-source_response', '2024-11-21 19:57:19', '2024-11-21 19:57:19')
cursor.execute(sql, values)


db.commit()

print(cursor.rowcount, "条记录插入成功")



# 插入数据
# sql = "INSERT INTO users (name, age) VALUES (%s, %s)"
# values = ("张三", 25)
# cursor.execute(sql, values)
