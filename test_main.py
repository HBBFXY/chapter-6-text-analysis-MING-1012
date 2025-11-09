def analyze_characters(s):
    # 创建一个字典用于统计字符出现次数
    char_count = {}
    
    # 遍历字符串中的每个字符
    for char in s:
        # 只统计字母字符（忽略数字、符号和空格等）
        if char.isalpha():
            # 转换为小写以实现大小写不敏感的统计（如A和a视为同一字符）
            lower_char = char.lower()
            char_count[lower_char] = char_count.get(lower_char, 0) + 1
    
    # 按出现频率降序排序，如果频率相同则按字母顺序排序
    sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
    
    # 打印结果
    print("字符出现频率（降序）：")
    for char, count in sorted_chars:
        print(f"{char}: {count}次")

# 获取用户输入
user_input = input("请输入一个字符串：")

# 调用函数进行分析
analyze_characters(user_input)
