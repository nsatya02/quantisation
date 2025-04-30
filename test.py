import os
import shutil
import subprocess
import streamlit as st
from huggingface_hub import snapshot_download

# Set page config for a nicer UI
st.set_page_config(page_title="Llama.cpp Quantisation", layout="centered")

st.title("Llama.cpp Quantisation Tool")

st.header("Clone and Build llama.cpp")
if st.button("Clone llama.cpp Repository"):
    if not os.path.exists("llama.cpp"):
        with st.spinner("Cloning the repository..."):
            result = subprocess.run(["git", "clone", "https://github.com/ggerganov/llama.cpp"])
        if result.returncode == 0:
            st.success("Repository cloned successfully!")
        else:
            st.error("Error cloning repository.")
    else:
        st.info("Repository already exists.")

if st.button("Build llama.cpp"):
    if os.path.exists("llama.cpp"):
        with st.spinner("Building llama.cpp..."):
            try:
                subprocess.run(["cmake", "-B", "llama.cpp/build"], check=True)
                subprocess.run(["cmake", "--build", "llama.cpp/build", "--config", "Release"], check=True)
                st.success("llama.cpp built successfully!")
            except subprocess.CalledProcessError as e:
                st.error(f"Build failed: {e}")
    else:
        st.error("llama.cpp repository not found. Please clone it first.")

st.header("Download the Model from Hugging Face")
model_name = st.text_input("Model Repository", "HuggingFaceTB/SmolLM2-135M-Instruct")
base_model = st.text_input("Local Directory to Save Model", "./SmolLM2-135M-Instruct/")
if st.button("Download Model"):
    with st.spinner("Downloading model..."):
        try:
            snapshot_download(repo_id=model_name, local_dir=base_model)
            st.success("Model downloaded successfully!")
        except Exception as e:
            st.error(f"Error downloading model: {e}")

st.header("Convert Model to f16 Format")
outfile = st.text_input("Output file for conversion", "./smol_f16.bin")
outtype = st.text_input("Conversion type (e.g., f16)", "f16")
if st.button("Convert Model"):
    conversion_script = os.path.join("llama.cpp", "convert_hf_to_gguf.py")
    if os.path.exists(conversion_script):
        command = ["python3", conversion_script, base_model, "--outfile", outfile, "--outtype", outtype]
        with st.spinner("Converting model..."):
            try:
                subprocess.run(command, check=True)
                st.success("Model converted to gguf format!")
            except subprocess.CalledProcessError as e:
                st.error(f"Conversion failed: {e}")
    else:
        st.error("Conversion script not found in llama.cpp.")

st.header("Quantise the Model")
quantisation = st.selectbox("Select Quantisation Type", options=["q4_k_m", "q4_0", "q5_0"])
outfile_quantised = st.text_input("Output file for quantised model", f"./smol_{quantisation}.gguf")
if st.button("Quantise Model"):
    quantise_executable = os.path.join("llama.cpp", "build", "bin", "llama-quantize")
    if os.path.exists(quantise_executable):
        command = [quantise_executable, outfile, outfile_quantised, quantisation]
        with st.spinner("Quantising model..."):
            try:
                subprocess.run(command, check=True)
                st.success("Model quantised successfully!")
            except subprocess.CalledProcessError as e:
                st.error(f"Quantisation failed: {e}")
    else:
        st.error("Quantisation executable not found. Please build llama.cpp first.")

st.header("Download Quantised Model")
if os.path.exists(outfile_quantised):
    with open(outfile_quantised, "rb") as f:
        quantised_data = f.read()
    st.download_button(
        label="Download Quantised Model",
        data=quantised_data,
        file_name=os.path.basename(outfile_quantised),
        mime="application/octet-stream",
    )
else:
    st.info("Quantised model file not found yet. Run the quantisation step to generate it.")

st.header("Delete Downloaded Model")
if os.path.exists(base_model):
    if st.button("Delete Downloaded Model"):
        try:
            shutil.rmtree(base_model)
            st.success("Downloaded model deleted successfully!")
        except Exception as e:
            st.error(f"Failed to delete downloaded model: {e}")
else:
    st.info("Downloaded model not found or already deleted.")
