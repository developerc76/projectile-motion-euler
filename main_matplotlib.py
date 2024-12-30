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
    xacclist = []
    yacclist = []
    vxlist = []
    vylist = []

    timelist = []
    ay = g - k * vx / m
    ax = -k * vx / m

    while time <= endtime:
        ylist.append(h)
        xlist.append(dist)
        timelist.append(time)
        xacclist.append(ax)
        yacclist.append(ay)
        vxlist.append(vx)
        vylist.append(vy)
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
        q = 10
        r = 10
        while not 0 <= q <= 7 or not 0 <= r <= 7:
            q = int(
                input(
                    "X-Axis: \n1 = Range; 2 = Height; 3 = X-Acceleration; 4 = Y-Acceleration; 5 = X-Velocity; 6 = Y-Velocity; 7 = Time\n"
                )
            )
            r = int(
                input(
                    "Y-Axis: \n1 = Range; 2 = Height; 3 = X-Acceleration; 4 = Y-Acceleration; 5 = X-Velocity; 6 = Y-Velocity; 7 = Time\n"
                )
            )
        match (q):
            case 1:
                q = xlist
                xlab = "Range (m)"
            case 2:
                q = ylist
                xlab = "Height (m)"
            case 3:
                q = xacclist
                xlab = "X-Acceleration (m/s/s)"
            case 4:
                q = yacclist
                xlab = "Y-Acceleration (m/s/s)"
            case 5:
                q = vxlist
                xlab = "X-Velocity (m/s)"
            case 6:
                q = vylist
                xlab = "Y-Velocity (m/s)"
            case 7:
                q = timelist
                xlab = "Time (s)"

        match (r):
            case 1:
                r = xlist
                ylab = "Range (m)"
            case 2:
                r = ylist
                ylab = "Height (m)"
            case 3:
                r = xacclist
                ylab = "X-Acceleration (m/s/s)"
            case 4:
                r = yacclist
                ylab = "Y-Acceleration (m/s/s)"
            case 5:
                r = vxlist
                ylab = "X-Velocity (m/s)"
            case 6:
                r = vylist
                ylab = "Y-Velocity (m/s)"
            case 7:
                r = timelist
                ylab = "Time (s)"

        i = np.array(q)
        j = np.array(r)
        plt.xlabel(xlab)
        plt.ylabel(ylab)
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
        "Would you like a graph? If not, then you will receive only a summary of the graph (Y/n): "
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
