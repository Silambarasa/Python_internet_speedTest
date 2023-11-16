import speedtest

wifi = speedtest.Speedtest(secure=True)

download_speed = wifi.download()

upload_speed = wifi.upload()
downloading = download_speed/1024
uploading = upload_speed/1024
print(f"downloading = {round(downloading/1024)}Mbps")
print(f"uploading = {round(uploading/1024)}Mbps")
