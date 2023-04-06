import asyncio

futs = []
for i in range(100):
  t = asyncio.get_event_loop().getaddrinfo("aa000000aa"+str(i)+".onion.", 80)
  futs.append(t)