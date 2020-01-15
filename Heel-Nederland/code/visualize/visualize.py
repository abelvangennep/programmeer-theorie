import matplotlib.pyplot as plt

# def draw_multiple_points():

axes = plt.gca()
axes.set_ylim(50.7, 53.7)
axes.set_xlim(3.25, 7.3)


# x, y axis value list
y = [52.95527649, 52.37888718, 51.98500061, 50.85027695, 53.21055603, 52.08027649]
x = [4.761111259, 4.900277615, 5.705555439, 5.899166584, 6.564722061, 4.324999809]

# Draw points based on x, y values
plt.scatter(x, y, s=10)

plt.plot(x,y)

# Set x, y label
plt.xlabel("Tester")
plt.ylabel("Test")

# Set chart title
plt.title("Trajecten")

# Read image
img = plt.imread("Nlkaart.png")

plt.imshow(img, aspect = "auto", extent = [3.25, 7.3, 50.65, 53.7])

# Plot
# ax.imshow(img)
plt.show()
