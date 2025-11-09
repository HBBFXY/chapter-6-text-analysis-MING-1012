def print_char_frequency(text):
    # 统计字母频率（不区分大小写）
    freq = {}
    for char in text:
        if char.isalpha():  # 只处理字母字符
            char_lower = char.lower()
            freq[char_lower] = freq.get(char_lower, 0) + 1
    
    # 按频率降序排序，频率相同则按字母升序排序
    sorted_chars = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    
    # 提取排序后的字母
    sorted_letters = [char for char, count in sorted_chars]
    
    # 打印结果（每行一个字母）
    for char in sorted_letters:
        print(char)

# 示例用法
input_string = input("请输入字符串: ")
print_char_frequency(input_string)
