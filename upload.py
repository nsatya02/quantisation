from huggingface_hub import login
login('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')
from huggingface_hub import HfApi
api = HfApi()
model_id = "nsatya/SmolLM2-1.7B-Instruct"
api.create_repo(model_id, exist_ok=True, repo_type="model")
api.upload_file(
    path_or_fileobj='/Users/satyanarasala/Desktop/quant/smol1.7B_q4_k_m.gguf',
    path_in_repo="SmolLM2-1.7B-Instruct-Q4_K_M.gguf",
    repo_id=model_id,
)