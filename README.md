# Downloading files from GitHub on the Command Line

## Linux
Step-1: Fetch the original link from the tinyurl

The original url looks like: https://raw.githubusercontent.com/UserName/...

Note: Do not enter the file extension
```
wget raw.githubusercontent.com/KishanKokal/elca/main/ai/filename.py
```

## Windows
Note-1: Open PowerShell
Note-2: Do not add file extension in the url
```
Invoke-WebRequest -Uri raw.githubusercontent.com/KishanKokal/elca/main/ai/filename.py -OutFile filename.py
```