from collections import Counter

def print_letters_by_frequency(s):
    # 只保留字母（区分大小写，如需要不区分可以把字母统一小写或大写）
    letters = [char for char in s if char.isalpha()]
    
    # 统计每个字母出现的频率
    frequency = Counter(letters)
    
    # 按频率降序排序，频率一样则按字母升序排序
    sorted_letters = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))
    
    # 仅打印字母，按排序顺序
    for letter, count in sorted_letters:
        print(letter, end=' ')
    print()  # 换行

# 测试
if __name__ == "__main__":
    input_str = input("请输入一个字符串: ")
    print("按字母出现频率降序排列的结果为:")
    print_letters_by_frequency(input_str)
