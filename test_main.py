# 评分文件，不要修改
import sys
import importlib.util
import subprocess
import os

def load_student_function():
    """加载学生函数"""
    try:
        # 动态导入学生模块
        spec = importlib.util.spec_from_file_location("student_module", "main.py")
        student_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(student_module)
        return student_module.has_duplicates, None
    except ImportError:
        return None, "❌ 错误: 找不到main.py文件"
    except AttributeError:
        return None, "❌ 错误: main.py中没有定义has_duplicates函数"
    except SyntaxError as e:
        return None, f"❌ 语法错误: {e}"
    except Exception as e:
        return None, f"❌ 加载学生模块时出错: {e}"

def test_function(has_duplicates):
    """测试重复元素检测功能"""
    test_cases = [
        ([], False),           # 空列表
        ([1], False),          # 单元素
        ([1, 2, 3], False),    # 无重复
        ([1, 2, 1], True),     # 有重复
        (["a", "b", "a"], True),  # 字符串重复
        ([1.0, 2.0, 1.0], True),  # 浮点数重复
        ([True, False], False),  # 布尔值无重复
        ([None, None], True)   # None值重复
    ]
    
    passed = 0
    total = len(test_cases)
    
    print("\n=== 函数功能测试 ===")
    for test_input, expected in test_cases:
        try:
            result = has_duplicates(test_input)
            if result == expected:
                passed += 1
                print(f"✅ 通过: {test_input} -> {expected}")
            else:
                print(f"⚠️ 失败: {test_input}")
                print(f"   预期: {expected}, 实际: {result}")
        except Exception as e:
            print(f"❌ 异常: {test_input}")
            print(f"   错误: {e}")
    
    score = int((passed / total) * 70)  # 函数测试占70分
    print(f"\n函数测试得分: {score}/70 (通过 {passed}/{total} 个测试)")
    return score

def test_main_program():
    """测试学生的主程序输出"""
    try:
        # 使用子进程运行学生的主程序并捕获输出
        result = subprocess.run(
            [sys.executable, "main.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        output = result.stdout
        
        # 检查是否有输出
        if not output.strip():
            print("❌ 主程序没有输出")
            return 0
        
        print("\n=== 主程序输出 ===")
        print(output)
        
        # 宽松检查
        score = 30  # 基础分30分
        if "有重复元素" in output and "没有重复元素" in output:
            print("✅ 主程序包含测试结果")
        else:
            print("⚠️ 主程序缺少部分测试结果")
            score = 20  # 部分得分
        
        print(f"主程序测试得分: {score}/30")
        return score
    except Exception as e:
        print(f"❌ 主程序运行出错: {e}")
        return 0

def main():
    """主测试函数"""
    print("=" * 50)
    print("重复元素判定作业自动评分")
    print("=" * 50)
    
    # 加载学生函数
    has_duplicates, error = load_student_function()
    if error:
        print(error)
        sys.exit(1)
    
    # 测试函数功能
    func_score = test_function(has_duplicates)
    
    # 测试主程序输出
    main_score = test_main_program()
    
    # 计算总分
    total_score = func_score + main_score
    print("\n" + "=" * 50)
    print(f"最终得分: {total_score}/100")
    print("=" * 50)
    
    # 退出码（0表示通过，1表示失败）
    if total_score >= 60:
        print("🎉 评分通过!")
        sys.exit(0)
    else:
        print("💥 评分未通过")
        sys.exit(1)

if __name__ == "__main__":
    main()
