'''
Author: LQ
Date: 2023-05-08 20:50:16
LastEditors: LQ
LastEditTime: 2023-05-08 21:26:39
FilePath: \stable-diffusion-webui-easy-prompt-studio\scripts\settings.py
Description:

Copyright (c) 2023 by LQ, All Rights Reserved.
'''
from modules import script_callbacks, shared

def on_ui_settings():
    shared.opts.add_option("eps_enable_save_raw_prompt_to_png_info", shared.OptionInfo(False, "将原提示保存在png info中", section=("easy_prompt_studio", "EasyPromptStudio")))
    shared.opts.add_option("eps_is_using_old_template_feature", shared.OptionInfo(False, "使用旧的随机功能实现(为了与sdweb-eagle-pnginfo兼容)", section=("easy_prompt_studio", "EasyPromptStudio")))

script_callbacks.on_ui_settings(on_ui_settings)
