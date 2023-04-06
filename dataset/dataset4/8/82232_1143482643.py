import time

print(time.strftime("%Y-%m-%d %H:%M:%S %z", time.gmtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S %z", time.localtime()))

# outputs
# 2022-06-01 11:22:12 +0800
# 2022-06-01 19:22:12 +0800