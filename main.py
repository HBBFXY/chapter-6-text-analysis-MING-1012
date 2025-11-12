# -*- coding: utf-8 -*-
# 在此文件处编辑代码
def analyze_text(text):
    """
    分析文本中字符频率并按频率降序排列
    
    参数:
    text - 输入的字符串
    
    返回:
    list - 按字符频率降序排列的字符列表
    """
    # 创建字典统计字符频率
    char_freq = {}
    
    # 遍历文本中的每个字符
    for char in text:
        # 只统计字母字符（包括中文字符）
        if char.isalpha():
            # 将字符转换为小写以实现不区分大小写
            char_lower = char.lower()
            # 更新字符频率计数
            if char_lower in char_freq:
                char_freq[char_lower] += 1
            else:
                char_freq[char_lower] = 1
    
    # 按频率降序排序字符
    # 使用sorted函数，按频率值（字典的值）排序，reverse=True表示降序
    sorted_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)
    
    # 提取排序后的字符列表（只返回字符，不包含频率值）
    result = [char for char, freq in sorted_chars]
    
    return result


# 主程序，已完整
if __name__ == "__main__":
    print("文本字符频率分析器")
    print("====================")
    print("请输入一段文本（输入空行结束）：")
    
    # 读取多行输入
    lines = []
    while True:
        try:
            line = input()
            if line == "":
                break
            lines.append(line)
        except EOFError:
            break
    
    # 合并输入文本
    text = "\n".join(lines)
    
    if not text.strip():
        print("未输入有效文本！")
    else:
        # 分析文本
        sorted_chars = analyze_text(text)
        
        # 打印结果
        print("\n字符频率降序排列:")
        print(", ".join(sorted_chars))
        
        # 提示用户比较不同语言
        print("\n提示: 尝试输入中英文文章片段，比较不同语言之间字符频率的差别")
