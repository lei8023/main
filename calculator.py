#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简易 Python 计算器
支持：加减乘除、幂运算、取余、开方
"""

import math

def calculate(a: float, op: str, b: float = None) -> float:
    """执行计算"""
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ValueError("错误：除数不能为零")
        return a / b
    elif op == '**' or op == '^':
        return a ** b
    elif op == '%':
        if b == 0:
            raise ValueError("错误：除数不能为零")
        return a % b
    elif op == 'sqrt':
        if a < 0:
            raise ValueError("错误：不能对负数开平方")
        return math.sqrt(a)
    else:
        raise ValueError(f"不支持的操作符: {op}")

def main():
    print("=" * 40)
    print("        简易 Python 计算器")
    print("=" * 40)
    print("支持的操作：")
    print("  +  -  *  /  **(幂)  %(取余)  sqrt(开方)")
    print("输入 q 或 quit 退出\n")

    while True:
        try:
            user_input = input("请输入表达式 (例如 3 + 5 或 sqrt 16)：").strip()

            if user_input.lower() in ('q', 'quit', 'exit'):
                print("再见！")
                break

            if not user_input:
                continue

            parts = user_input.split()

            # 处理开方：sqrt 16
            if parts[0].lower() == 'sqrt' and len(parts) == 2:
                a = float(parts[1])
                result = calculate(a, 'sqrt')
                print(f"结果: √{a} = {result}\n")
                continue

            # 普通二元运算：3 + 5
            if len(parts) != 3:
                print("格式错误！请使用：数字 操作符 数字  或  sqrt 数字\n")
                continue

            a = float(parts[0])
            op = parts[1]
            b = float(parts[2])

            result = calculate(a, op, b)
            print(f"结果: {a} {op} {b} = {result}\n")

        except ValueError as e:
            print(f"{e}\n")
        except Exception as e:
            print(f"发生错误: {e}\n")

if __name__ == "__main__":
    main()
