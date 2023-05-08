from modules import script_callbacks, shared

def on_ui_settings():
    shared.opts.add_option("eps_enable_save_raw_prompt_to_pnginfo", shared.OptionInfo(False, "将原提示保存在pngninfo中", section=("easy_prompt_studio", "EasyPromptStudio")))
    shared.opts.add_option("eps_use_old_template_feature", shared.OptionInfo(False, "使用旧的随机功能实现(为了与sdweb-eagle-pnginfo兼容)", section=("easy_prompt_studio", "EasyPromptStudio")))

script_callbacks.on_ui_settings(on_ui_settings)