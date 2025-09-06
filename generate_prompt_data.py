#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据整合脚本：将txt文件整合成JSON格式
"""

import os
import json
import re
from pathlib import Path

def extract_placeholders(text):
    """提取文本中的占位符 [XXX]"""
    pattern = r'\[([^\]]+)\]'
    matches = re.findall(pattern, text)
    return matches

def generate_prompt_data():
    """生成提示词数据JSON文件"""
    current_dir = Path(__file__).parent
    image_dir = current_dir / "image_data"
    
    # 扫描图片和对应的txt文件
    prompt_data = {}
    
    # 查找image_data目录下的所有png文件
    if not image_dir.exists():
        print(f"✗ image_data目录不存在: {image_dir}")
        return False
        
    png_files = sorted(image_dir.glob("*.png"))
    
    for png_file in png_files:
        # 获取文件名（不含扩展名）
        file_base = png_file.stem
        
        # 构建数据结构（不再需要txt文件，提示词数据已在JSON中）
        # 这里我们需要从现有的prompt_data.json中读取提示词内容
        prompt_data[file_base] = {
            "image": f"image_data/{png_file.name}",
            "prompt": "",  # 需要从现有数据中获取
            "placeholders": []
        }
        
        print(f"✓ 发现图片文件: {png_file.name}")
    
    # 如果没有找到图片文件，尝试读取现有的prompt_data.json来保持数据
    if not prompt_data:
        existing_data_file = current_dir / "prompt_data.json"
        if existing_data_file.exists():
            try:
                with open(existing_data_file, 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
                    
                # 更新现有数据的图片路径
                for key, data in existing_data.items():
                    # 确保图片路径使用新的image_data目录
                    image_name = os.path.basename(data["image"])
                    data["image"] = f"image_data/{image_name}"
                    
                prompt_data = existing_data
                print(f"✓ 从现有JSON文件读取了 {len(prompt_data)} 个提示词")
            except Exception as e:
                print(f"✗ 读取现有JSON文件失败: {e}")
                return False
    
    # 保存为JSON文件
    output_file = current_dir / "prompt_data.json"
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(prompt_data, f, ensure_ascii=False, indent=2)
        
        print(f"\n✓ 数据整合完成，保存到: {output_file}")
        print(f"✓ 总共处理了 {len(prompt_data)} 个提示词")
        
        # 打印统计信息
        total_placeholders = sum(len(data['placeholders']) for data in prompt_data.values())
        print(f"✓ 总共发现 {total_placeholders} 个占位符")
        
        # 显示占位符详情
        for key, data in prompt_data.items():
            if data['placeholders']:
                print(f"  - {key}: {data['placeholders']}")
        
        return True
        
    except Exception as e:
        print(f"✗ 保存JSON文件失败: {e}")
        return False

if __name__ == "__main__":
    print("开始整合提示词数据...")
    success = generate_prompt_data()
    if success:
        print("\n🎉 数据整合成功！")
    else:
        print("\n❌ 数据整合失败！")
