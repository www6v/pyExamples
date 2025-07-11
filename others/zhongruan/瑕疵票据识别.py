import json

# 1是回头背书票，从记录票据流转信息的列表中，如果发现有相同的当事人，就算是。  
def convert_and_check_parties(invoiceListStr: str) -> dict[str:bool]:
    """
    将字符串转换为列表并调用check_same_parties方法
    
    Args:
        invoiceListStr: 包含票据信息的字符串,格式应为JSON格式
        
    Returns:
        bool: check_same_parties的返回结果
    """
    try:
        # 将字符串解析为Python对象(列表)
        invoices_list = json.loads(invoiceListStr)
        # 调用check_same_parties方法
        return check_same_parties(invoices_list)
    except json.JSONDecodeError:
        print("输入的字符串不是有效的JSON格式")
        return {'result' : False}
    except Exception as e:
        print(f"发生错误: {str(e)}")
        return {'result' : False}


def check_same_parties(invoices: list) -> dict[str:bool]:
    """
    检查多张票据是否具有相同的当事人
    
    Args:
        invoices: 包含票据信息的列表，每个票据信息应包含当事人字段
        
    Returns:
        bool: 如果所有票据的当事人相同返回True，否则返回False
    """
    if not invoices or len(invoices) < 2:
        return {'result' : False}
        
    # 获取第一张票据的当事人信息作为参考
    first_party = invoices[0].get('party', '')
    
    # 检查所有其他票据是否与第一张票据具有相同的当事人
    for invoice in invoices[1:]:
        if invoice.get('party', '') != first_party:
            return {'result' : False}
            
    return {'result' : True}



# 2是不可转让票，票据信息中有这个字段，可以直接判定。   
def check_non_transferable(invoiceListStr):
    """检查票据是否为不可转让票据
    
    Args:
        json_str: JSON格式的票据信息字符串
        
    Returns:
        dict: 包含检查结果的字典,格式为{'result': bool}
    """
    try:
        invoices = json.loads(invoiceListStr)
        if not isinstance(invoices, list) or len(invoices) == 0:
            return {'result1': False}
            
        # 检查每张票据是否都标记为不可转让
        for invoice in invoices:
            if not invoice.get('non_transferable', False):
                return {'result1': False}
                
        return {'result1': True}
        
    except:
        return {'result1': False}



# 3是有限追索票，票据信息中有这个信息，可以直接判定。
def check_limited_recourse(invoiceListStr):
    """检查票据是否为有限追索票据
    
    Args:
        invoiceListStr: JSON格式的票据信息字符串
        
    Returns:
        dict: 包含检查结果的字典,格式为{'result2': bool}
    """
    try:
        invoices = json.loads(invoiceListStr)
        if not isinstance(invoices, list) or len(invoices) == 0:
            return {'result2': False}
            
        # 检查每张票据是否都标记为有限追索
        for invoice in invoices:
            if not invoice.get('limited_recourse', False):
                return {'result2': False}
                
        return {'result2': True}
        
    except:
        return {'result2': False}



###############

def test_convert_and_check_parties():
    """测试convert_and_check_parties函数"""
    # 测试有效的JSON字符串,当事人相同
    json_str1 = '[{"party": "张三"}, {"party": "张三"}]'
    assert convert_and_check_parties(json_str1) == {'result': True}

    # 测试有效的JSON字符串,当事人不同
    json_str2 = '[{"party": "张三"}, {"party": "李四"}]'
    assert convert_and_check_parties(json_str2) == {'result': False}

    # 测试单个票据的情况
    json_str3 = '[{"party": "张三"}]'
    assert convert_and_check_parties(json_str3) == {'result': False}

    # 测试空列表
    json_str4 = '[]'
    assert convert_and_check_parties(json_str4) == {'result': False}

    # 测试无效的JSON字符串
    json_str5 = 'invalid json'
    assert convert_and_check_parties(json_str5) == {'result': False}

    # 测试缺少party字段
    # json_str6 = '[{"name": "张三"}, {"name": "李四"}]'
    # assert convert_and_check_parties(json_str6) == {'result': False}

    print("所有测试用例通过!")






def test_check_non_transferable():
    """测试check_non_transferable函数"""
    # 测试所有票据都不可转让
    json_str1 = '[{"non_transferable": true}, {"non_transferable": true}]'
    assert check_non_transferable(json_str1) == {'result1': True}

    # 测试部分票据可转让
    json_str2 = '[{"non_transferable": true}, {"non_transferable": false}]'
    assert check_non_transferable(json_str2) == {'result1': False}
    
    # 测试单个不可转让票据
    json_str3 = '[{"non_transferable": true}]'
    assert check_non_transferable(json_str3) == {'result1': True}

    # 测试空列表
    json_str4 = '[]'
    assert check_non_transferable(json_str4) == {'result1': False}

    # 测试无效JSON
    json_str5 = 'invalid json'
    assert check_non_transferable(json_str5) == {'result1': False}

    print("所有不可转让票据测试用例通过!")


def test_check_limited_recourse():
    """测试check_limited_recourse函数"""
    # 测试所有票据都是有限追索
    json_str1 = '[{"limited_recourse": true}, {"limited_recourse": true}]'
    assert check_limited_recourse(json_str1) == {'result2': True}

    # 测试部分票据非有限追索
    json_str2 = '[{"limited_recourse": true}, {"limited_recourse": false}]'
    assert check_limited_recourse(json_str2) == {'result2': False}
    
    # 测试单个有限追索票据
    json_str3 = '[{"limited_recourse": true}]'
    assert check_limited_recourse(json_str3) == {'result2': True}

    # 测试空列表
    json_str4 = '[]'
    assert check_limited_recourse(json_str4) == {'result2': False}

    # 测试无效JSON
    json_str5 = 'invalid json'
    assert check_limited_recourse(json_str5) == {'result2': False}

    print("所有有限追索票据测试用例通过!")


def aggregate_results(result: str, result1: str,
                      result2: str) -> dict[str:bool] :
    if result == 'True' and result1 == 'True' and result2 == 'True':
       return { 'final_result' : True}  
    else:
       return { 'final_result' : False}    

if __name__ == '__main__':
  result = test_convert_and_check_parties()
  result1 = test_check_non_transferable()
  result2 = test_check_limited_recourse()
  
  aggregate_results(result, result1, result2)












