import gdown
url = input("Provide your Google Drive Link: ")
prefix = ["https://", "http://"]
gdown.download_folder(url, quiet=False, use_cookies=False)