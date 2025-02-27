

def test():
    print('')


if __name__ == '__main__':
    test()



def upload_and_verify_image(image_path: str, verify_url: str) -> dict:
    """
    上传图片并进行验真
    
    Args:
        image_path: 图片文件路径
        verify_url: 验真服务的URL地址
        
    Returns:
        dict: 包含图片信息和验真结果的字典
    """
    import os
    import requests
    from pathlib import Path
    
    # 获取图片信息
    image_file = Path(image_path)
    
    # 检查文件是否存在
    if not image_file.exists():
        return {"error": "文件不存在"}
        
    image_info = {
        "name": image_file.name,
        "size": os.path.getsize(image_path),
        "type": image_file.suffix[1:] # 去掉前面的点号
    }
    
    # 准备上传文件
    try:
        files = {
            'image': (image_info['name'], open(image_path, 'rb'), f'image/{image_info["type"]}')
        }
        
        # 发送验真请求
        response = requests.post(verify_url, files=files)
        
        # 检查响应状态
        if response.status_code == 200:
            verify_result = response.json()
            return {
                **image_info,
                "verify_result": verify_result
            }
        else:
            return {
                **image_info,
                "error": f"验真请求失败: {response.status_code}"
            }
            
    except Exception as e:
        return {
            **image_info,
            "error": f"处理过程出错: {str(e)}"
        }
    finally:
        files['image'][1].close()



# 使用示例
if __name__ == '__main__':
    image_path = "invoice.jpg"
    verify_url = "http://example.com/verify"
    result = upload_and_verify_image(image_path, verify_url)
    print("图片信息和验真结果:", result)