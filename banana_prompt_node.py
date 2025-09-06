# -*- coding: utf-8 -*-
# bjubBdXgED: HHixnTVX50
# Generated obfuscated code
import base64 as vHUGyr3KHI
import random as CjlPT7D4tN
import string as S9cnqpMbEP

# Obfuscation variables
KoZSibhhdK = lambda x: x
RWWCDxtPyn = 633
C0QiwtCinT = "gfZUsJ8phJ"

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Banana Prompt Node - 独立的提示词选择节点
"""

import server
from aiohttp import web
import os
import json
import torch
import numpy as np
from PIL import Image
import urllib.parse
import io
import re

# 获取当前目录
nSjkr7lV7W = os.path.dirname(os.path.abspath(__file__))
ikIhs4bfrm = os.path.join(nSjkr7lV7W, "prompt_data.json")
r4YYhzVOwm = os.path.join(nSjkr7lV7W, "selection.json")

def RHtNxO8t8N():
    """加载提示词数据"""
    if not os.path.exists(ikIhs4bfrm):
        return {}
    try:
        with open(ikIhs4bfrm, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"BananaPrompt: Error loading prompt data: {e}")
        return {}

# uTmtt7BTup: QaTnJjDxUF
def URqLahUcwH():
    """加载选择状态"""
    if not os.path.exists(r4YYhzVOwm):
        return {}
    try:
        with open(r4YYhzVOwm, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"BananaPrompt: Error loading selection: {e}")
        return {}

def Z8nJMH6u5X(data):
    """保存选择状态"""
    try:
        with open(r4YYhzVOwm, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"BananaPrompt: Error saving selection: {e}")

def m90kWgn8c6(prompt_text, placeholders_dict):
    """替换提示词中的占位符"""
    if not placeholders_dict:
        return prompt_text
    
    result = prompt_text
    for placeholder, value in placeholders_dict.items():
        if value.strip():  # 只替换非空值
            pattern = r'\[' + re.escape(placeholder) + r'\]'
            result = re.sub(pattern, value, result)
    
    return result

class BananaPromptNode:
    """Banana Prompt 节点类"""
    
    @classmethod
    def IS_CHANGED(cls, **kwargs):
        # 检查选择文件的修改时间
        if os.path.exists(r4YYhzVOwm):
            return os.path.getmtime(r4YYhzVOwm)
        return float("inf")

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "hidden": { "unique_id": "UNIQUE_ID" },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "get_selected_prompt"
    CATEGORY = "🍌Banana Prompt"

    def get_selected_prompt(self, unique_id):
        """获取选中的提示词"""
        selection_data = URqLahUcwH()
        node_data = selection_data.get(str(unique_id), {})
        
        selected_key = node_data.get("selected_key")
        placeholders = node_data.get("placeholders", {})
        
        if not selected_key:
            return ("",)  # 没有选择任何图片
        
        prompt_data = RHtNxO8t8N()
        if selected_key not in prompt_data:
            return ("",)  # 选择的图片数据不存在
        
        original_prompt = prompt_data[selected_key]["prompt"]
        
        # 替换占位符
        final_prompt = m90kWgn8c6(original_prompt, placeholders)
        
        return (final_prompt,)

# 获取ComfyUI服务器实例
try:
    prompt_server = server.PromptServer.instance
    print("BananaPrompt: ComfyUI服务器实例获取成功")
except Exception as e:
    print(f"BananaPrompt: 获取服务器实例失败: {e}")
    prompt_server = None

# 注册API路由
if prompt_server is not None:
    print("BananaPrompt: 开始注册API路由...")

# b4txgCo8f2: vd1aFNFl7J
@prompt_server.routes.get("/banana_prompt/get_prompt_data")
async def dmlGgprIsb(request):
    """获取提示词数据API"""
    try:
        prompt_data = RHtNxO8t8N()
        return web.json_response({"status": "ok", "data": prompt_data})
    except Exception as e:
        return web.json_response({"status": "error", "message": str(e)}, status=500)

@prompt_server.routes.post("/banana_prompt/set_selection")
async def s9NNAvOUtg(request):
    """设置选择的图片和占位符值"""
    try:
        data = await request.json()
        node_id = str(data.get("node_id"))
        selected_key = data.get("selected_key")
        placeholders = data.get("placeholders", {})
        
        if not node_id:
            return web.json_response({"status": "error", "message": "Missing node_id"}, status=400)
        
        selection_data = URqLahUcwH()
        
        selection_data[node_id] = {
            "selected_key": selected_key,
            "placeholders": placeholders
        }
        
        Z8nJMH6u5X(selection_data)
        
        return web.json_response({"status": "ok"})
    except Exception as e:
        return web.json_response({"status": "error", "message": str(e)}, status=500)

@prompt_server.routes.post("/banana_prompt/get_selection")
async def pMrv8FU3rU(request):
    """获取节点的选择状态"""
    try:
        data = await request.json()
        node_id = str(data.get("node_id"))
        
        if not node_id:
            return web.json_response({"status": "error", "message": "Missing node_id"}, status=400)
        
        selection_data = URqLahUcwH()
        node_data = selection_data.get(node_id, {})
        
        return web.json_response({"status": "ok", "data": node_data})
    except Exception as e:
        return web.json_response({"status": "error", "message": str(e)}, status=500)

@prompt_server.routes.get("/banana_prompt/get_available_images")
async def kOguEx0mT7(request):
    """获取image_data目录下可用的图片列表"""
    try:
        image_dir = os.path.join(nSjkr7lV7W, "image_data")
        if not os.path.exists(image_dir):
            return web.json_response([])
        
        # 获取所有PNG文件
        available_images = []
        for filename in os.listdir(image_dir):
            if filename.lower().endswith('.png'):
                filepath = os.path.join(image_dir, filename)
                if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
                    available_images.append(filename)
        
        # 按文件名排序
        available_images.sort()
        
        print(f"BananaPrompt: Found {len(available_images)} images: {available_images}")
        return web.json_response(available_images)
    except Exception as e:
        print(f"BananaPrompt: Error getting available images: {e}")
        return web.json_response({"status": "error", "message": str(e)}, status=500)

@prompt_server.routes.post("/banana_prompt/add_prompt")
async def QarYTiQb4I(request):
    """添加新的提示词"""
    try:
        data = await request.json()
        
        # 验证必需字段
        required_fields = ['image_filename', 'prompt', 'title', 'describe']
        for field in required_fields:
            if not data.get(field, '').strip():
                return web.json_response({"status": "error", "message": f"Missing {field}"}, status=400)
        
        image_filename = data['image_filename']
        
# zffgrmZ57D: TMDMQLgj9F
        # 验证图片文件是否存在
        image_path = os.path.join(nSjkr7lV7W, "image_data", image_filename)
        if not os.path.exists(image_path):
            return web.json_response({"status": "error", "message": f"Image file {image_filename} not found"}, status=400)
        
        # 验证是否为PNG文件
        if not image_filename.lower().endswith('.png'):
            return web.json_response({"status": "error", "message": "Only PNG files are supported"}, status=400)
        
        # 读取现有数据
        prompt_data = RHtNxO8t8N()
        
        # 检查图片是否已被使用
        for key, existing_data in prompt_data.items():
            if existing_data.get('image', '').endswith(image_filename):
                return web.json_response({"status": "error", "message": f"Image {image_filename} is already used by prompt {key}"}, status=400)
        
        # 生成新的key（找到最大的数字key +1）
        existing_keys = [int(k) for k in prompt_data.keys() if k.isdigit()]
        new_key = str(max(existing_keys, default=0) + 1)
        print(f"BananaPrompt: Generated new key: {new_key}")
        
        # 解析占位符
        placeholders = data.get('placeholders', [])
        if isinstance(placeholders, str):
            try:
                placeholders = json.loads(placeholders)
            except:
                placeholders = []
        elif not isinstance(placeholders, list):
            placeholders = []
        
        # 添加新数据
        prompt_data[new_key] = {
            "image": f"image_data/{image_filename}",
            "prompt": data['prompt'],
            "placeholders": placeholders,
            "Favorite": "false",
            "title": data['title'],
            "describe": data['describe']
        }
        
        # 保存回JSON文件
        try:
            with open(ikIhs4bfrm, 'w', encoding='utf-8') as f:
                json.dump(prompt_data, f, ensure_ascii=False, indent=2)
            print(f"BananaPrompt: Updated prompt_data.json with new key: {new_key}")
        except Exception as e:
            print(f"BananaPrompt: Error saving JSON: {e}")
            return web.json_response({"status": "error", "message": f"Failed to save data: {str(e)}"}, status=500)
        
        return web.json_response({"status": "ok", "new_key": new_key})
        
    except Exception as e:
        print(f"BananaPrompt: Error adding prompt: {e}")
        import traceback
        traceback.print_exc()
        return web.json_response({"status": "error", "message": str(e)}, status=500)

@prompt_server.routes.post("/banana_prompt/toggle_favorite")
async def jQRjorEDCs(request):
    """更新收藏状态"""
    try:
        data = await request.json()
        key = str(data.get("key"))
        favorite = data.get("favorite")
        
        if not key or favorite not in ["true", "false"]:
            return web.json_response({"status": "error", "message": "Invalid parameters"}, status=400)
        
        # 读取现有数据
        prompt_data = RHtNxO8t8N()
        
        if key not in prompt_data:
            return web.json_response({"status": "error", "message": "Key not found"}, status=404)
        
        # 更新收藏状态
        prompt_data[key]["Favorite"] = favorite
        
        # 保存回JSON文件
        try:
            with open(ikIhs4bfrm, 'w', encoding='utf-8') as f:
                json.dump(prompt_data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            return web.json_response({"status": "error", "message": f"Failed to save: {str(e)}"}, status=500)
        
        return web.json_response({"status": "ok"})
    except Exception as e:
        return web.json_response({"status": "error", "message": str(e)}, status=500)

@prompt_server.routes.get("/banana_prompt/thumbnail")
async def f79qmsKI4c(request):
    """生成缩略图API"""
    filepath = request.query.get('filepath')
    if not filepath or ".." in filepath:
        return web.Response(status=400)
    
    filepath = urllib.parse.unquote(filepath)
    
    # 如果是相对路径，转换为绝对路径
    if not os.path.isabs(filepath):
        filepath = os.path.join(nSjkr7lV7W, filepath)
    
# ZGemzvqvyG: uSAZHEusF0
    # 安全检查：确保文件在banana_prompt目录内
    if not filepath.startswith(nSjkr7lV7W):
        return web.Response(status=403)
    
    if not os.path.exists(filepath):
        return web.Response(status=404)
    
    try:
        img = Image.open(filepath)
        has_alpha = img.mode == 'RGBA' or (img.mode == 'P' and 'transparency' in img.info)
        img = img.convert("RGBA") if has_alpha else img.convert("RGB")
        img.thumbnail([320, 320], Image.LANCZOS)
        buffer = io.BytesIO()
        format_type, content_type = ('PNG', 'image/png') if has_alpha else ('JPEG', 'image/jpeg')
        img.save(buffer, format=format_type, quality=90 if format_type == 'JPEG' else None)
        buffer.seek(0)
        return web.Response(body=buffer.read(), content_type=content_type)
    except Exception as e:
        print(f"BananaPrompt: Error generating thumbnail for {filepath}: {e}")
        return web.Response(status=500)

# 节点类映射
NODE_CLASS_MAPPINGS = {
    "BananaPromptNode": BananaPromptNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BananaPromptNode": "🍌 Banana Prompt Selector",
}

# 确认路由注册
# h1vyugBSen: x3gk6tKURF
if prompt_server is not None:
    print("BananaPrompt: 所有API路由注册完成")
    # 列出已注册的banana_prompt路由
    banana_routes = [str(route) for route in prompt_server.routes if 'banana_prompt' in str(route)]
    print(f"BananaPrompt: 已注册 {len(banana_routes)} 个路由")
else:
    print("BananaPrompt: 警告 - 无法注册API路由，ComfyUI服务器实例不可用")
