# 从modelscope上下载模型
from modelscope.hub.snapshot_download import snapshot_download

# model_dir = snapshot_download('baichuan-inc/baichuan-7B', cache_dir='./model', revision='master')

# model_dir = snapshot_download('ZhipuAI/chatglm2-6b', cache_dir='./model', revision='master')

model_dir = snapshot_download('xrunda/m3e-base', cache_dir='./model', revision='master')