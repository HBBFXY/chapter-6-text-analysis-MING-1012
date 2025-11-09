def analyze_char_frequency(text):
    # 创建一个字典用于统计字符频率
    frequency = {}
    
    # 遍历字符串中的每个字符并计数
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    # 按频率降序排序，频率相同时按字符升序排列
    sorted_chars = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))
    
    # 打印结果
    for char, count in sorted_chars:
        print(f"字符 '{char}': 出现 {count} 次")

# 获取用户输入
user_input = input("请输入一个字符串: ")

# 调用函数进行分析
analyze_char_frequency(user_input)
