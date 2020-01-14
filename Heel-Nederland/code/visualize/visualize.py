import matplotlib.pyplot as plt

# def draw_multiple_points():

# x, y axis value list
x = [2,4,600]
y = [5,7,1007]

# Draw points based on x, y values
plt.scatter(x, y, s=10)

plt.plot(x,y)

# Set x, y label
plt.xlabel("Tester")
plt.ylabel("Test")

# Set chart title
plt.title("Trajecten")

# Read image
img = plt.imread("NLkaart.png")

plt.imshow(img)

# Plot
# ax.imshow(img)
plt.show()
