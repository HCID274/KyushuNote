#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PIC双流不稳定性参数研究实验脚本
自动运行不同n0值的模拟并生成结果图片
"""

import os
import sys
import numpy as np
from pic import run_simulation

def main():
    """
    执行不同n0参数的PIC模拟实验
    """
    print("开始PIC模拟参数研究实验...")
    print("="*50)
    
    # 实验参数设置
    n0_values = [0.5, 1.0, 2.0, 5.0]  # 要测试的电子数密度值
    tEnd = 50  # 模拟结束时间
    
    # 确保输出目录存在
    output_dir = "."  # 当前目录
    
    # 为每个n0值运行模拟
    for i, n0 in enumerate(n0_values):
        print(f"正在运行实验 {i+1}/{len(n0_values)}: n0 = {n0}")
        
        # 设置输出文件名
        output_filename = f"pic_n0_{n0}.png"
        output_path = os.path.join(output_dir, output_filename)
        
        try:
            # 运行模拟
            run_simulation(
                n0=n0,
                tEnd=tEnd,
                output_filename=output_path,
                plotRealTime=False  # 不显示实时绘图，加快执行速度
            )
            print(f"  ✓ 实验完成，结果保存至: {output_filename}")
            
        except Exception as e:
            print(f"  ✗ 实验失败: {str(e)}")
            continue
    
    print("="*50)
    print("所有实验完成！生成的文件：")
    for n0 in n0_values:
        filename = f"pic_n0_{n0}.png"
        if os.path.exists(filename):
            print(f"  - {filename}")
    
    print("\n实验参数总结：")
    print(f"  - 测试的n0值: {n0_values}")
    print(f"  - 模拟时间: {tEnd}")
    print(f"  - 粒子数: 40000")
    print(f"  - 网格数: 400")

if __name__ == "__main__":
    main() 