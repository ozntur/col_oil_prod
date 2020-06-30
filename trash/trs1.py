import requests
import io
import zipfile

def download_extract_zip(url):
    """
    Download a ZIP file and extract its contents in memory
    yields (filename, file-like object) pairs
    """
    response = requests.get(url)
    with zipfile.ZipFile(io.BytesIO(response.content)) as thezip:
        for zipinfo in thezip.infolist():
            with thezip.open(zipinfo) as thefile:
                yield zipinfo.filename, thefile


url = 'https://cogcc.state.co.us/documents/data/downloads/gis/WELLS_SHP.ZIP'

download_extract_zip(url)

print(thefile)