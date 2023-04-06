import matplotlib.pyplot as plt
f = plt.figure(figsize=(10,5),dpi=300)
ax1 = f.add_axes([0,0,0.5,1])
ax2 = f.add_axes([0.5,0,0.5,1])
ax1.pie([180,180],center=(0.5,0.5),radius=0.5,frame=False)
ax2.pie([180,180],center=(0.5,0.5),radius=0.5,frame=True)
plt.show()