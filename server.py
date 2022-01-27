import subprocess

subprocess.call(["poetry", "shell"], shell=True)
subprocess.call(["uvicorn", "main:app"], shell=True)