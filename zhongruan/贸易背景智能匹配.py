###########  发票匹配规则  

# 对于承兑业务，
# 发票的购买方，与票面上的出票人一致；发票的销售方，与票面上的收款人一致。
def check_invoice_bill_parties(invoice_buyer: str, bill_drawer: str,
                             invoice_seller: str, bill_payee: str) -> bool:
    """
    检查发票购买方与票面出票人是否一致，发票销售方与票面收款人是否一致
    
    Args:
        invoice_buyer: 发票购买方
        bill_drawer: 票面出票人
        invoice_seller: 发票销售方 
        bill_payee: 票面收款人
        
    Returns:
        bool: 如果发票购买方与出票人一致且发票销售方与收款人一致返回True，否则返回False
    """
    # 检查发票购买方是否与票面出票人一致
    buyer_match = (invoice_buyer == bill_drawer)
    
    # 检查发票销售方是否与票面收款人一致
    seller_match = (invoice_seller == bill_payee)
    
    return buyer_match and seller_match


# 对于贴现业务，
# 发票上的销售方，与贴现申请人一致；发票上的购买方，与贴现申请人直接前手一致
# 一手票除外。
def check_invoice_discount_parties(invoice_seller: str, discount_applicant: str,
                                     invoice_buyer: str, direct_predecessor: str) -> bool:
        """
        检查发票销售方与贴现申请人是否一致，发票购买方与贴现申请人直接前手是否一致
        
        Args:
            invoice_seller: 发票销售方
            discount_applicant: 贴现申请人
            invoice_buyer: 发票购买方
            direct_predecessor: 贴现申请人直接前手
            
        Returns:
            bool: 如果发票销售方与贴现申请人一致且发票购买方与直接前手一致返回True，否则返回False
        """
        # 检查发票销售方是否与贴现申请人一致
        seller_match = (invoice_seller == discount_applicant)
        
        # 检查发票购买方是否与贴现申请人直接前手一致
        buyer_match = (invoice_buyer == direct_predecessor)
        
        return seller_match and buyer_match



# 发票开票日期，早于或等于当前日期。
def check_invoice_date(invoice_date: str) -> bool:
        """
        检查发票开票日期是否早于或等于当前日期
        
        Args:
            invoice_date: 发票开票日期，格式为YYYY-MM-DD
            
        Returns:
            bool: 如果发票日期早于或等于当前日期返回True，否则返回False
        """
        from datetime import datetime
        
        # 将日期字符串转换为datetime对象
        invoice_dt = datetime.strptime(invoice_date, '%Y-%m-%d')
        current_dt = datetime.now()
        
        # 只比较日期部分
        invoice_date = invoice_dt.date()
        current_date = current_dt.date()
        
        return invoice_date <= current_date


###########  合同匹配规则

# 1)对于承兑业务，贸易合同的购买方，与票面上的出票人一致；合同的销售方，与票面上的收款人一致。
def check_contract_bill_parties(
        contract_buyer: str,
        bill_drawer: str, 
        contract_seller: str,
        bill_payee: str
    ) -> bool:
        """
        检查贸易合同的购买方与票面出票人是否一致，合同销售方与票面收款人是否一致
        
        Args:
            contract_buyer: 贸易合同购买方
            bill_drawer: 票面出票人
            contract_seller: 贸易合同销售方
            bill_payee: 票面收款人
            
        Returns:
            bool: 如果合同购买方与票面出票人一致且合同销售方与票面收款人一致返回True，否则返回False
        """
        buyer_match = (contract_buyer == bill_drawer)
        seller_match = (contract_seller == bill_payee)
        
        return buyer_match and seller_match


# 2)对于贴现业务，合同上的销售方，与贴现申请人一致；合同上的购买方，与贴现申请人直接前手（从票据流转信息中可以获取）一致。
def check_contract_discount_parties(contract_seller: str, discount_applicant: str,
                                 contract_buyer: str, direct_predecessor: str) -> bool:
    """
    检查合同销售方与贴现申请人是否一致，合同购买方与贴现申请人直接前手是否一致
    
    Args:
        contract_seller: 合同销售方
        discount_applicant: 贴现申请人
        contract_buyer: 合同购买方
        direct_predecessor: 贴现申请人直接前手
        
    Returns:
        bool: 如果合同销售方与贴现申请人一致且合同购买方与直接前手一致返回True，否则返回False
    """
    # 检查合同销售方是否与贴现申请人一致
    seller_match = (contract_seller == discount_applicant)
    
    # 检查合同购买方是否与贴现申请人直接前手一致
    buyer_match = (contract_buyer == direct_predecessor)
    
    return seller_match and buyer_match


# 5)合同的发生日期/签订日期，早于或等于当前日期。
def check_contract_date(contract_date: str) -> bool:
    """
    检查合同签订日期是否早于或等于当前日期
    
    Args:
        contract_date: 合同签订日期，格式为YYYY-MM-DD
            
    Returns:
        bool: 如果合同日期早于或等于当前日期返回True，否则返回False
    """
    from datetime import datetime
    
    # 将日期字符串转换为datetime对象
    contract_dt = datetime.strptime(contract_date, '%Y-%m-%d')
    current_dt = datetime.now()
    
    # 只比较日期部分
    contract_date = contract_dt.date()
    current_date = current_dt.date()
    
    return contract_date <= current_date



def aggregate_results(result1: str, result2: str,
                      result3: str, result4: str,
                      result5: str, result6: str) -> bool:
    if result1 == 'True' and result2 == 'True' and result3 == 'True' and result4 == 'True' and result5 == 'True' and result6 == 'True':
       return True 
    else:
       return False   



if __name__ == '__main__':
    ###########  发票匹配规则 
    a = check_invoice_bill_parties("ab","ab","ab","ab")
    print(a)

    # 测试用例
    result = check_invoice_discount_parties(
        "销售公司", "销售公司",
        "采购公司", "采购公司"
    )
    print(f"发票与贴现业务各方主体检查结果: {result}")

    # 测试用例
    result = check_invoice_date('2025-01-15')
    print(f"发票日期检查结果: {result}")


    ###########  合同匹配规则
    # 测试用例
    result = check_contract_bill_parties(
        "购买公司", "购买公司",
        "销售公司", "销售公司" 
    )
    print(f"合同与发票各方主体检查结果: {result}")


    final_result = aggregate_results('True', 'True', 'True', 'True', 'True', 'True') 
    print(f"最终检查结果-: {final_result}")















