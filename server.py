import subprocess

subprocess.call(["uvicorn", "main:app"], shell=True)