# Downloading files from GitHub on the Command Line

## Linux
Step-1: Fetch the original link from the tinyurl

The original url looks like: https://raw.githubusercontent.com/UserName/...

Note: Do not enter the file extension
```
wget tinyurl.com/elca<filename>
```
Step-2: Copy the url from the response and paste the <URL> in the following command
```
wget <URL>
```

## Windows
Note-1: Open PowerShell
Note-2: Do not add file extension in the url
```
Invoke-WebRequest -Uri tinyurl.com/elca<filename> -OutFile <filename>.py
```