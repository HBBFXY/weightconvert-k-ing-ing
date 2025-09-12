user_input = input()
weight = float(user_input[:-2])
unit = user_input[-2:]
if unit == "kg":
     result = weight * 2.2046
     print(f"对应的英制重量为{result:.3f}磅")
elif unit == "pd":
     result = weight / 2.2046
     print(f"对应的公制重量为{result:.2f}公斤")
else:
     print("输入格式错误，请使用'xxkg'或'xxpd'格式（如10kg、10pd）")
