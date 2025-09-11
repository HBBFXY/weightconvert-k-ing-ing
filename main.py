def kg_to_pound(kg):
    """千克转磅：1千克 = 2.2046磅"""
    return kg * 2.2046

def pound_to_kg(pound):
    """磅转千克：1千克 = 2.2046磅"""
    return pound / 2.2046

print("=== 重量转换程序 ===")
print("请输入重量数值及单位（单位仅支持 kg 或 pd，示例：10kg、10pd）：")
user_input = input().strip().lower()
unit = user_input[-2:]
try:
    value = float(user_input[:-2])
    if unit == "kg":
        result = kg_to_pound(value)
        print(f"{value:.0f}kg = {result:.3f}pd")
    elif unit == "pd":
        result = pound_to_kg(value)
        print(f"{value:.0f}pd = {result:.3f}kg")
    else:
        print("单位错误！仅支持 kg（公斤）或 pd（磅）")
except:
    print("输入格式错误！请按示例格式输入（如 10kg、10pd）")
