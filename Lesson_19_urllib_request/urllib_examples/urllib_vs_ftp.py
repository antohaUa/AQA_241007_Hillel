import urllib.request

ftp_url = "ftp://ftp.example.com/file.txt"
response = urllib.request.urlopen(ftp_url)
content = response.read()

with open("local_file.txt", "wb") as file:
    file.write(content)