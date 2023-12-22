import matplotlib.pyplot as plt 

x1 = [2,4,5, 10]
y1 = [2,3,6,10]

x2 = [2,4,6,8,10]
y2 = [6,7,8,9,10]

plt.plot(x1, y1, color = "green", linewidth =3,  linestyle = "dashed", marker = "o", markerfacecolor="blue", markersize =12,  label = "Line 1")
plt.plot(x2, y2, label = "Line 2")

#plt.xlim()
# plt.ylim()
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.title("Demo Graph - Two Line")

plt.legend()

plt.show()

