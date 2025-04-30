# # To Download the model:
# from huggingface_hub import snapshot_download
# model_name = "HuggingFaceTB/SmolLM2-135M-Instruct"
# base_model = "./SmolLM2-135M-Instruct/"
# snapshot_download(repo_id=model_name, local_dir=base_model, local_dir_use_symlinks=False)

# To Download the model:
# from huggingface_hub import snapshot_download
# model_name = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
# base_model = "./DeepSeek-R1-Distill-Qwen-1.5B/"
# snapshot_download(repo_id=model_name, local_dir=base_model, local_dir_use_symlinks=False)

from huggingface_hub import snapshot_download
model_name = "meta-llama/Llama-3.2-1B"
base_model = "./llama3.2/"
snapshot_download(token="",repo_id=model_name, local_dir=base_model, local_dir_use_symlinks=False)