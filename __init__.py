"""
Banana Prompt Node - 独立的ComfyUI扩展
完全独立于原Local Image Gallery项目
"""

from .banana_prompt_node import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

# 设置Web目录指向js文件夹
WEB_DIRECTORY = "./js"

# 导出必要的映射
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']

print("🍌 Banana Prompt Node loaded successfully!")
