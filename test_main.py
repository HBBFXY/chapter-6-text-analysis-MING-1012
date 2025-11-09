def analyze_text():
    # 获取用户输入的字符串
    text = input("请输入要分析的文本: ")
    
    # 创建字典存储字符频率
    char_frequency = {}
    
    # 遍历字符串中的每个字符，统计频率
    for char in text:
        # 忽略空字符（可选，根据需求调整）
        if char.strip() == "":
            continue
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    
    # 按频率降序排序，如果频率相同则按字符升序排序
    sorted_chars = sorted(char_frequency.items(), 
                         key=lambda x: (-x[1], x[0]))
    
    # 打印结果
    print("\n字符出现频率（降序）：")
    for char, count in sorted_chars:
        print(f"字符 '{char}'：出现 {count} 次")

# 运行程序
if __name__ == "__main__":
    analyze_text()
