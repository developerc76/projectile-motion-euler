#!/usr/bin/env python3
import math
import matplotlib.pyplot as plt
import numpy as np


def closest_to_zero(nums):
    li = []
    for num in nums:
        li.append(abs(num))
    for num in nums:
        if abs(num) == min(li):
            return num


def euler(h, g, m, k, vi, angle, dt, endtime, graph, time, dist):
    vy = math.sin(math.radians(angle)) * vi
    vx = math.cos(math.radians(angle)) * vi
    xlist = []
    ylist = []
    timelist = []
    ay = g - k * vx / m
    ax = -k * vx / m

    while time <= endtime:
        if not graph:
            print(
                f"Time (s): {time}; Y-Acceleration (m/s^2): {ay}; Y-Velocity (m/s): {vy}; Height (m): {h}; X-Acceleration (m/s^2): {ax}; X-Velocity (m/s): {vx}; Range (m): {dist}"
            )
        ylist.append(h)
        xlist.append(dist)
        timelist.append(time)
        # Y-Components: Accel (gravity), Height, Velocity
        ay = g - k * vy / m
        h = h + dt * (vy)
        vy = vy + dt * (ay)
        # X-Components: Accel, Height, Velocity
        ax = -k * vx / m
        dist = dist + dt * (vx)
        vx = vx + dt * (ax)
        # Plus Delta Time
        time += dt
        time = round(float(time), 3)
    if graph:
        i = np.array(xlist)
        j = np.array(ylist)
        plt.scatter(i, j)
        plt.show()
    print("-------------GRAPH-SUMMARY----------------")
    minheight = closest_to_zero(ylist)
    indexforminheight = ylist.index(minheight)
    print(f"Max Height: {max(ylist)}")
    print(f"The range and time at the height value closest to 0 at the given dt")
    print(
        f"Height: {minheight}; Time: {timelist[indexforminheight]}; Range: {xlist[indexforminheight]}"
    )


def get_vals():
    h = float(input("Initial height (m): "))
    g = float(input("Absolute Value of Gravity (m/s^2): ")) * (-1)
    m = float(input("Mass (kg): "))
    k = float(input("Drag Coefficient: "))
    vi = float(input("Initial velocity (m/s): "))
    angle = float(input("Launch Angle (degrees): "))
    dt = float(input("Delta Time (s); if 1 then write 1.0: "))
    endtime = float(input("Endtime (s): "))
    graph = input(
        "Would you like a graph? If not, then you will receive standard output (Y/n): "
    )
    time = 0
    dist = 0
    if graph.lower() == "y" or graph.lower() == "n":
        if graph.lower() == "y":
            graph = True
        else:
            graph = False
        return h, g, m, k, vi, angle, dt, endtime, graph, time, dist
    else:
        print("Rerun program and make (Y/n) = Y, y, N, or n")


def main():
    h, g, m, k, vi, angle, dt, endtime, graph, time, dist = get_vals()
    euler(h, g, m, k, vi, angle, dt, endtime, graph, time, dist)


if __name__ == "__main__":
    main()
