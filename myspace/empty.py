
import json


def abc(post_id:str, occasion:str, needs:str, where:str, who:str, topic_relevance:str):    
  s = '{ "post_id": "' + post_id + '", "occasion": "'+ occasion + '", "needs":  "' + needs + '", "where":  "' + where + '",  "who": "' + who + '", "topic_relevance": "' + topic_relevance + '"}'
  json_obj = json.loads(s)
  print(json_obj)


def ttt(post_id:str, cleaned_content:str):  
  s = '{"posts": [{ "post_id": "' + post_id + '", "text": "'+ cleaned_content + '"}]}'
  json_obj = json.loads(s)
  print(json_obj)

if __name__ == "__main__":
  ttt("p", "o")