import json

# Provided JSON string
json_str = '''
{
    "output": {
        "choices": [
            {
                "message": {
                    "content": "{\\n    \\"milk_powder_posts_analysis\\": [\\n        {\\n            \\"post_id\\": \\"674b089b0000000002018c8b\\",\\n            \\"type\\": \\"not mentioned\\",\\n            \\"relevance_score\\": 1,\\n            \\"post_type\\": \\"not mentioned\\",\\n            \\"post_topic\\": \\"not mentioned\\",\\n            \\"is_ai\\": 0,\\n            \\"is_ad\\": false,\\n            \\"ad_type\\": \\"not mentioned\\",\\n            \\"sentiment_score\\": 3,\\n            \\"purpose\\": \\"not mentioned\\",\\n            \\"user_role\\": \\"not mentioned\\",\\n            \\"user_segment\\": \\"not mentioned\\",\\n            \\"infant_stage\\": \\"not mentioned\\",\\n            \\"infant_type\\": [],\\n            \\"occasion\\": [],\\n            \\"baby_issue\\": [],\\n            \\"parent_issue\\": [],\\n            \\"product_issue\\": [],\\n            \\"product_choose\\": [],\\n            \\"product_tech_features\\": [],\\n            \\"product_mkt_features\\": [],\\n            \\"mentioned_product\\": [],\\n            \\"ad_insert_method\\": \\"not mentioned\\",\\n            \\"headline_hook\\": \\"not mentioned\\",\\n            \\"tone\\": \\"not mentioned\\",\\n            \\"story_structure\\": \\"not mentioned\\",\\n            \\"effective_ad_methods\\": \\"not mentioned\\",\\n            \\"intro_style\\": \\"not mentioned\\",\\n            \\"body_focus\\": \\"not mentioned\\",\\n            \\"closing_style\\": \\"not mentioned\\",\\n            \\"emerging_keyword\\": [],\\n            \\"latent_demand\\": []\\n        },\\n        {\\n            \\"post_id\\": \\"673aef430000000007032f8c\\",\\n            \\"type\\": \\"求助咨询\\",\\n            \\"relevance_score\\": 4,\\n            \\"post_type\\": \\"求助咨询\\",\\n            \\"post_topic\\": \\"纽贝兰朵羊奶粉的特点及购买信息\\",\\n            \\"is_ai\\": 0,\\n            \\"is_ad\\": false,\\n            \\"ad_type\\": \\"not mentioned\\",\\n            \\"sentiment_score\\": 0,\\\n            \\"purpose\\": \\"增加消费者awareness\\",\\n            \\"user_role\\": \\"妈妈\\",\\n            \\"user_segment\\": \\"成分党\\",\\n            \\"infant_stage\\": \\"12-36月龄（3段）\\",\\n            \\"infant_type\\": [],\\n            \\"occasion\\": [],\\n            \\"baby_issue\\": [],\\n            \\"parent_issue\\": [\\"知识焦虑\\"],\\n            \\"product_issue\\": [],\\n            \\"product_choose\\": [],\\n            \\"product_tech_features\\": [],\\n            \\"product_mkt_features\\": [],\\n            \\"mentioned_product\\": [\\"纽贝兰朵羊奶粉\\"],\\n            \\"ad_insert_method\\": \\"not mentioned\\",\\n            \\"headline_hook\\": \\"not mentioned\\",\\n            \\"tone\\": \\"亲切可信\\",\\n            \\"story_structure\\": \\"问题引入+产品特点+结尾呼吁\\",\\n            \\"effective_ad_methods\\": \\"通过具体细节吸引潜在客户\\",\\n            \\"intro_style\\": \\"提问\\",\\n            \\"body_focus\\": \\"产品对比\\",\\n            \\"closing_style\\": \\"引导用户咨询\\",\\n            \\"emerging_keyword\\": [],\\n            \\"latent_demand\\": [\\"寻找冷门但优质的奶粉\\"]\\n        },\\n        {\\n            \\"post_id\\": \\"6745d71c00000000060152eb\\",\\n            \\"type\\": \\"促销信息\\",\\n            \\"relevance_score\\": 4,\\n            \\"post_type\\": \\"促销信息\\",\\n            \\"post_topic\\": \\"雀巢能恩全护奶粉的推广\\",\\n            \\"is_ai\\": 0,\\n            \\"is_ad\\": true,\\n            \\"ad_type\\": \\"硬广\\",\\n            \\"sentiment_score\\": 5,\\n            \\"purpose\\": \\"种草\\",\\n            \\"user_role\\": \\"品牌方\\",\\n            \\"user_segment\\": \\"国货支持者\\",\\n            \\"infant_stage\\": \\"not mentioned\\",\\n            \\"infant_type\\": [],\\n            \\"occasion\\": [],\\n            \\"baby_issue\\": [],\\n            \\"parent_issue\\": [],\\n            \\"product_issue\\": [],\\n            \\"product_choose\\": [\\"接近母乳\\"],\\n            \\"product_tech_features\\": [\\"HMO\\"],\\n            \\"product_mkt_features\\": [\\"突破性配方\\"],\\n            \\"mentioned_product\\": [\\"Nestle雀巢能恩全护\\"],\\n            \\"ad_insert_method\\": \\"直接推荐\\",\\n            \\"headline_hook\\": \\"请大数据把我推荐给所有宝妈\\",\\n            \\"tone\\": \\"热情洋溢\\",\\n            \\"story_structure\\": \\"产品特点+行动号召\\",\\n            \\"effective_ad_methods\\": \\"通过权威背书和明星成分吸引注意\\",\\n            \\"intro_style\\": \\"场景描绘\\",\\n            \\"body_focus\\": \\"产品技术特性\\",\\n            \\"closing_style\\": \\"行动号召\\",\\n            \\"emerging_keyword\\": [\\"HMO\\"],\\n            \\"latent_demand\\": [\\"对高端奶粉的需求\\"]\\n        }\\n    ]\\n}",
                    "role": "assistant"
                },
                "finish_reason": "stop"
            }
        ]
    },
    "usage": {
        "total_tokens": 3332,
        "output_tokens": 961,
        "input_tokens": 2371,
        "prompt_tokens_details": {
            "cached_tokens": 0
        }
    },
    "request_id": "f9476045-bafc-9228-ba0f-5db6e824849d"
}
'''

# Parse the JSON string
data = json.loads(json_str)

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
