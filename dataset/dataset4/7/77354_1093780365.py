resp = requests.get(uri, stream=True)
decompressed = gzip.GzipFile(fileobj=resp.raw)
boto3.client('s3').upload_fileobj(decompressed, Bucket=bucket, Key=key)