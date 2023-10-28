# Downloading files from GitHub on the Command Line

## Linux
```
wget raw.githubusercontent.com/KishanKokal/elca/main/filename.py
```
Clear terminal history
```
history -c && history -w
```

## Windows
Note: Open PowerShell
```
Invoke-WebRequest -Uri raw.githubusercontent.com/KishanKokal/elca/main/filename.py -OutFile filename.py
```