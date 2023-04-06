with ThreadPoolExecutor(max_workers=500) as e:
  e.map(download, images)