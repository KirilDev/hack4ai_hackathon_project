import sys
import gdown

class GoogleDownload:
    def download_google_drive_folder(url: str) -> None:
        """
        Downloads a folder from a Google Drive link.

        Parameters:
        url (str): The Google Drive link to the folder to be downloaded.
        """
    try:
        gdown.download_folder(url, quiet=False, use_cookies=False)
    except Exception as e:
        print(f"An error occurred while downloading the Google Drive folder: {e}")

    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: script.py <Google Drive Link>")
            sys.exit(1)
    
    google_drive_link = sys.argv[1]
    download_google_drive_folder(google_drive_link)

