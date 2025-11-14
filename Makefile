

run:
	uv run python main.py

# is very slow, hence git clone approach below
pull:
	hf download meta-llama/Llama-3.1-8B-Instruct

# replace <huggingface-user-name> and <ACCESS_TOKEN> with your own
clonemodel:
	git clone https://<huggingface-user-name>:<ACCESS_TOKEN>@huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct

scan:
	uv run python scan.py

shell:
	uv run python

setconfig:
	uv run modelscan create-settings-file -l modelscan_config.json