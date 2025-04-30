Quantisation using llama.cpp

* First clone the git repo “git clone https://github.com/ggerganov/llama.cpp”
      Then in terminal enter this command “cd llama.cpp”
* Then after that enter the below command in terminal “cmake -B build
	cmake --build build --config Release” .

* Download the model which you want to quantise from hugging face using snap_download code.

* To convert the model into f16.bin format by below command.
* “python3 ./llama.cpp/convert_hf_to_gguf.py ./SmolLM2-135M-Instruct --outfile ./smol_f16.bin --outtype f16”

* To convert the model into gguf abd 4 bit quant format using the llama-quantise in llama.cpp by below command.
*  “./llama.cpp/build/bin/llama-quantize ./smol_f16.bin  ./smol_q4_k_m.gguf  q4_k_m”
