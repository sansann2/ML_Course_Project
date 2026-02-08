import torch

from pathlib import Path


def check():
    files:[
        "Meta-Llama-3.1-8B-Instruct-Q8_0.gguf",
        "public.txt",
        "private.txt",
    ]
    for f in files:
        if not Path(f).exists():
            print(f"File {f} not found.")
            return False
        
def main():
    check()


if __name__ == "__main__":
    main()