import requests
import os
import json

from readFile import read_file_to_string  

strDict = {
  "result": "{\"posts\": [{\"text\": \"胖宝宝睡大觉回头发现喵喵居然侧躺着，肥脸太可爱了，肥诺诺的[害羞R][害羞R][害羞R][害羞R][害羞R][害羞R][害羞R]\", \"post_id\": \"674b089b0000000002018c8b\"}, {\"text\": \"纽贝兰朵羊奶粉哪里好啊??六年母婴一共没卖过几箱这个奶 因为很多妈妈追求大众品牌 其实冷门的奶粉配方也很好的[耶R][耶R]粉2段的 有 16:34 新日期吗 16:41 可爱母婴 纽贝兰朵 纽 是的 17:49 辽宁 书院： 3 纽贝兰朵羊奶粉二段一箱 净含量：00220 净含量：80 万羊奶粉（12-36月龄，3段） 一-1月龄，2 请收款 微信转账\", \"post_id\": \"673aef430000000007032f8c\"}, {\"text\": \"请大数据把我推荐给所有宝妈！宝宝喂养其实很简单推荐给所有宝妈！ 宝宝喂养其实很简单 NAN INFINIPRO.能恩圣罐 BREAKTHROUGHFORMULA Nestle雀巢能恩全护， 6HMO婴/儿配方奶粉\", \"post_id\": \"6745d71c00000000060152eb\"}]}"
}


def send_post_request(url: str, json_body: dict, headers: dict = None, params: dict = None)  -> requests.Response:
    """
    Send an HTTP POST request with a JSON body, custom headers, and query parameters.

    Args:
        url (str): The URL to send the request to.
        json_body (dict): The JSON body of the request.
        headers (dict, optional): Custom HTTP headers. Defaults to None.
        params (dict, optional): Query parameters. Defaults to None.

    Returns:
        requests.Response: The response from the server.
    """
    try:
        response = requests.post(
            url,
            json=json_body,  # Automatically sets Content-Type to application/json
            headers=headers,
            params=params,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        raise






def prepare(strDict, prompt, qwenToken):
    data = strDict['result']

    # URL to send the request to
    url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"

    model = 'qwen-plus' # qwen-turbo   

    json_body = {
        "model": model,
        "input": {
            "messages": [{
                    "role": "system",
                    "content":  prompt
                },
                {
                    "role": "user",
                    "content": data
                }
            ]
        },
        "parameters": {
            "result_format": "message",
            "top_p": 0.8,
            "temperature": 0.7
        }
    }


    headers = {
        "Authorization": "Bearer " + qwenToken,
        "Content-Type": "application/json",
        "Custom-Header": "CustomValue",
    }

    params = {
        "run_id": "1",
        "url": url,
        "model": model,
        "data_id": "1",
        "prompt": "",
        "data": "",
        "start_request_time": "",
    }
    
    return url,json_body,headers,params


# def prepare(strDict, prompt, qwenToken):
#     data = strDict

#     # file_path = "/Users/wei.wang/workspace/pyExamples/web/http/danone_post.tpl"
#     # prompt = read_file_to_string(file_path)
#     # prompt = os.getenv('prompt') 

#     # URL to send the request to
#     url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"

#     model = 'qwen-turbo'

#     json_body = {
#         "model": model,
#         "input": {
#             "messages": [{
#                     "role": "system",
#                     "content":  prompt
#                 },
#                 {
#                     "role": "user",
#                     "content": data
#                 }
#             ]
#         },
#         "parameters": {
#             "result_format": "message",
#             "top_p": 0.8,
#             "temperature": 0.7
#         }
#     }


#     # Example headers
#     headers = {
#         "Authorization": "Bearer " + qwenToken,
#         "Content-Type": "application/json",
#         "Custom-Header": "CustomValue",
#     }

#     params = {
#         "run_id": "1",
#         "url": "", #### 
#         "model": model,
#         "data_id": "1",
#         "prompt": "",
#         "data": "",
#         "start_request_time": "",
#     }
    
#     return url,json_body,headers,params


# if __name__ == "__main__":
#     url, json_body, headers, params = prepare(strDict)

#     # Send the request
#     response = send_post_request(url, json_body, headers, params)
    
#     print(f"Response status code: {response.status_code}")
#     print(f"Response body: {response.json()}")


# def main(strDict: str, prompt:str, qwenToken:str) -> dict:
if __name__ == "__main__":

    file_path = "/Users/wei.wang/workspace/pyExamples/web/http/danone_post.tpl"
    prompt = read_file_to_string(file_path)

    qwenToken = os.getenv('qwenToken') 

    url, json_body, headers, params = prepare(strDict, prompt, qwenToken) 
    print(url)
    print(json_body) 
    print(headers)
    print(params)

    response = send_post_request(url, json_body, headers, params)

    print(f"Response status code: {response.status_code}")
    print(f"Response body: {response.json()}")


    # json_str = str(response.json())

    # # Parse the JSON string
    # data = json.loads(json_str)


    data = response.json()

    # Extract the required fields
    validated_success_data = {
        "input_tokens": data["usage"]["input_tokens"],
        "output_tokens": data["usage"]["output_tokens"],
        "total_tokens": data["usage"]["total_tokens"],
        "request_id": data["request_id"],
        "finish_reason": data["output"]["choices"][0]["finish_reason"],
        "content": json.loads(data["output"]["choices"][0]["message"]["content"])
    }

    # Print the result
    print(validated_success_data)

    # {
    #     "result": response.status_code + response.json(),
    # }
    
    # print(f"Response body: {str(response.json())}")