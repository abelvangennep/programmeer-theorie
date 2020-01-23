import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# aan deze functie alle history meegeven
# verschil tussen frame/frames
# wat is i in de update

# def animateTSP(history, points):
key_frames_mult = len(history) // 1500

fig, ax = plt.subplots()

line, = plt.plot([], [], lw = 2)

def init():
    # Set x ,y limits
    axes = plt.gca()
    axes.set_xlim(3.25, 7.3)
    axes.set_ylim(50.7, 53.7)

    # Set x, y label
    plt.xlabel("X")
    plt.ylabel("Y")

    # Set chart title
    plt.title("train")

    # Read and show image
    img = plt.imread("NLkaart.png")
    plt.imshow(img, aspect = "auto", extent = [3.25, 7.3, 50.65, 53.7])

    station_coordinates = []
    for station in stations_objects.stations.values():
        station_coordinates.append([station.y, station.x])
        plt.scatter(station.x, station.y, s = 5)
    # x = [points[i][0] for i in history[0]]
    # y = [points[i][0] for i in history[0]]
    # plt.plot(x, y, 'co')

    line.set_data([],[])

    return line,

def update(frames):
    for frame in frames:
        x = [points[i, 0] for i in history[frame] + [history[frame][0]]]
        y = [points[i, 0] for i in history[frame] + [history[frame][0]]]
        line.set_data(x, y)
        return line

ani = FuncAnimation(fig, update, frames = range(0, len(history), key_frames_mult),
            init_func = init, interval = 3, repeat = False)

plt.show()
