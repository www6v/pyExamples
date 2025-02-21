


from datetime import datetime

# 2)合同发生/签订日期，早于或等于发票开票日期，并早于或等于当前日期。
def check_contract_dates(contract_date: str, invoice_date: str) -> bool:
        """
        检查合同日期、发票日期和当前日期的关系
        合同日期 <= 发票日期 
        合同日期 <= 当前日期
        
        Args:
            contract_date: 合同日期，格式 YYYY-MM-DD
            invoice_date: 发票日期，格式 YYYY-MM-DD
        Returns:
            bool: 日期关系是否满足要求
        """
        date_format = "%Y-%m-%d"
        contract_date_obj = datetime.strptime(contract_date, date_format)
        invoice_date_obj = datetime.strptime(invoice_date, date_format)
        current_date = datetime.now()

        # 合同日期 <= 发票日期
        condition1 = contract_date_obj <= invoice_date_obj
        # 合同日期 <= 当前日期
        condition2 = contract_date_obj <= current_date

        return condition1 and condition2


# 3)发票开票日期，早于或等于当前日期。
def check_invoice_date(invoice_date: str) -> bool:
        """
        检查发票开票日期是否早于或等于当前日期
        
        Args:
            invoice_date: 发票日期，格式 YYYY-MM-DD
        Returns:
            bool: 发票日期是否合规
        """
        date_format = "%Y-%m-%d"
        invoice_date_obj = datetime.strptime(invoice_date, date_format)
        current_date = datetime.now()
        
        return invoice_date_obj <= current_date


# 4)发票/合同本次使用金额之和，大于或等于本次业务票面金额之和。
def check_amout(invoice_amount: float, contract_amount:float, receipt_amout: float) -> bool:
    total_amount = invoice_amount + contract_amount
    result = total_amount >= receipt_amout

    return result



# 5)贸易合同的双方名称，与发票的双方的名称匹配。忽略全角/半角的区别（如中文括号和英文括号认为是一致的，大小写认为是一致的）。
def check_party_names(contract_party1: str, contract_party2: str, invoice_party1: str, invoice_party2: str) -> bool:
        """
        检查合同双方名称与发票双方名称是否匹配
        
        Args:
            contract_party1: 合同甲方名称
            contract_party2: 合同乙方名称
            invoice_party1: 发票销售方名称
            invoice_party2: 发票购买方名称
        Returns:
            bool: 双方名称是否匹配
        """
        # 标准化处理名称
        def normalize_name(name: str) -> str:
            # 将全角字符转换为半角
            name = name.replace('（', '(').replace('）', ')')
            name = name.replace('【', '[').replace('】', ']')
            # 转换为小写
            name = name.lower()
            # 移除多余空格
            name = ' '.join(name.split())
            return name
            
        # 标准化所有名称
        c1 = normalize_name(contract_party1)
        c2 = normalize_name(contract_party2)
        i1 = normalize_name(invoice_party1)
        i2 = normalize_name(invoice_party2)
        
        # 检查是否匹配(考虑双方顺序可能相反的情况)
        return (c1 == i1 and c2 == i2) or (c1 == i2 and c2 == i1)



# 6)对于承兑业务，仅对银票承兑才做贸易背景合规检查。
# 要求合同的购买方（甲方）、发票的购买方，与票面上的出票人（银票的出票人必须是贸易的购买方/付款方）三者一致；合同的销售方、发票的销售方，与票面上的收款人三者一致。
def check_acceptance_parties(contract_buyer: str, contract_seller: str,
                               invoice_buyer: str, invoice_seller: str, 
                               bill_drawer: str, bill_payee: str) -> bool:
        """
        检查承兑业务中各方主体的一致性
        
        Args:
            contract_buyer: 合同购买方
            contract_seller: 合同销售方
            invoice_buyer: 发票购买方
            invoice_seller: 发票销售方
            bill_drawer: 票据出票人
            bill_payee: 票据收款人
            
        Returns:
            bool: 各方主体是否匹配一致
        """   
        # 检查购买方是否一致(合同购买方、发票购买方、票据出票人)
        buyers_match = (contract_buyer == invoice_buyer == bill_drawer)
        
        # 检查销售方是否一致(合同销售方、发票销售方、票据收款人)
        sellers_match = (contract_seller == invoice_seller == bill_payee)
        
        return buyers_match and sellers_match


# 7)对于贴现业务，
# 合同上的销售方、发票上的销售方，与贴现申请人三者一致；
# 合同上的购买方、发票上的购买方，与贴现申请人直接前手（从票据流转信息中可以获取）三者一致（没有前手的票不判断）。
def check_discounting_parties(contract_seller: str, contract_buyer: str,
                            invoice_seller: str, invoice_buyer: str,
                            discount_applicant: str, direct_predecessor: str) -> bool:
    """
    检查贴现业务中各方主体的一致性
    
    Args:
        contract_seller: 合同销售方
        contract_buyer: 合同购买方
        invoice_seller: 发票销售方
        invoice_buyer: 发票购买方
        discount_applicant: 贴现申请人
        direct_predecessor: 贴现申请人直接前手
        
    Returns:
        bool: 各方主体是否匹配一致
    """
    # 检查销售方是否一致(合同销售方、发票销售方、贴现申请人)
    sellers_match = (contract_seller == invoice_seller == discount_applicant)
    
    # 检查购买方是否一致(合同购买方、发票购买方、贴现申请人直接前手)
    buyers_match = (contract_buyer == invoice_buyer == direct_predecessor)
    
    return sellers_match and buyers_match


def aggregate_results(result1: str, result2: str,
                      result3: str, result4: str,
                      result5: str, result6: str, result7: str) -> bool:
    # 所有检查结果进行与操作
    # final_result = result1 and result2 and result3 and result4 and result5 and result6 and result7

    if result1 == 'True' and result2 == 'True' and result3 == 'True' and result4 == 'True' and result5 == 'True' and result6 == 'True' and result7 == 'True':
       return True 
    else:
       return False   

    #return final_result



# 1)合同总金额大于或等于发票总金额。
def check_contract_invoice_amount(contract_amount: float, invoice_amount: float) -> bool:
        """
        检查合同总金额是否大于或等于发票总金额
        
        Args:
            contract_amount: 合同总金额
            invoice_amount: 发票总金额
            
        Returns:
            bool: 如果合同金额大于等于发票金额返回True，否则返回False
        """
        return contract_amount >= invoice_amount




# def main(arg1: int, arg2: int) -> bool:
#     return {
#         arg1 > arg2,
#     }    



if __name__ == '__main__':
    # a = main(1, 2)


    a = check_contract_invoice_amount(1, 2)
    print(f"kkk: {a}")


    # 测试用例
    result = check_contract_dates("2026-01-03", "2026-01-02")

    print(f"合同日期检查结果: {result}")

    # r = check_contract_dates("2022-01-03", "2022-01-02")
    # print(r)

    # 测试用例
    r1 = check_invoice_date("2023-01-02")
    print(f"发票日期检查结果: {r1}")



    r2 = check_amout(1, 6, 5)
    print(f"金额检查结果: {r2}")  # 检查发票和合同金额之和是否大于等于业务金额


    r3 = check_party_names("甲方", "(乙方)", "（乙方）", "甲方")
    r4 = check_party_names("甲方", "乙方", "甲方", "乙方")
    print(f"双方名称检查结果: {r3}")
    print(f"双方名称检查结果: {r4}")



    # 测试用例
    r5 = check_acceptance_parties(
        "测试公司", "供应商A", 
        "测试公司", "供应商A",
        "测试公司", "供应商A"
    )
    print(f"承兑业务各方主体检查结果: {r5}")


    # 测试贴现业务各方主体检查
    r6 = check_discounting_parties(
        "销售公司", "采购公司",
        "销售公司", "采购公司",
        "销售公司", "采购公司"
    )
    print(f"贴现业务各方主体检查结果: {r6}")


    final_result = aggregate_results(
        True, True, True, True, True, True, True
    )

    print(f"最终检查结果: {final_result}")





def main(result1: str, result2: str,
                      result3: str, result4: str,
                      result5: str, result6: str, result7: str) -> bool:
    # 所有检查结果进行与操作
    # final_result = result1 and result2 and result3 and result4 and result5 and result6 and result7

    if result1 == 'True' and result2 == 'True' and result3 == 'True' and result4 == 'True' and result5 == 'True' and result6 == 'True' and result7 == 'True'):
       return {"final_result" : str(True) }  
    else:
       return {"final_result" : str(False)}   
 








    








