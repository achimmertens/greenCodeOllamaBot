# greenCodeOllamaBot
Some Code to chat with an AI

## Modify greenCodeLlama318b.modelfile
Write your promt there and/or give some examples how should work.
After that create a modelfile, based on Ollama and your prompt by writing:
ollama create greenCodeLlama318b --file greenCodeLlama318b.modelfile

## ask_ollama.py
ask_ollama.py is a python "skeleton" script, which takes the file "frage.txt" and pushes it to ollama. It logs the interactions and also the output.
