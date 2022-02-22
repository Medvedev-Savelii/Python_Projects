import requests

def download_files(url):
	local_filename = url.split('/')[-1]
	with requests.get(url, stream=True) as r:
		print("Downloading...")
		with open("C:\WEB\Python_project"+local_filename,'wb') as f:
			print("Writing data to file")
			for chunk in r.iter_content(chunk_size=8192):
				f.write(chunk)
	f.close()
	print("Download Complete")
	print("File saved as "+local_filename)


download_files("https://img4.goodfon.ru/wallpaper/nbig/c/e8/akame-ga-kill-ubiitsa-akame-esdeath-general-esdeath-esdes-ge.jpg")
