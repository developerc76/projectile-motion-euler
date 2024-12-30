#!/usr/bin/env python3
import main_matplotlib
import math
from prettytable import PrettyTable


def closest_to_zero(nums):
    li = []
    for num in nums:
        li.append(abs(num))
    for num in nums:
        if abs(num) == min(li):
            return num


def printMethodAdvanced(h, g, m, k, vi, angle, dt, endtime, graph, time, dist):
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

    t = PrettyTable(
        [
            "Time (s)",
            "Y-Acceleration (m/s/s)",
            "Y-Velocity (m/s)",
            "Height (m)",
            "X-Acceleration (m/s/s)",
            "X-Velocity (m/s)",
            "Range (m)",
        ]
    )

    while time <= endtime:
        t.add_row([time, ay, vy, h, ax, vx, dist])
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
    print(t)
    print("-------------MOTION-SUMMARY----------------")
    minheight = closest_to_zero(ylist)
    indexforminheight = ylist.index(minheight)
    print(f"Max Height: {max(ylist)}")
    print(f"The range and time at the height value closest to 0 at the given dt")
    print(
        f"Height: {minheight}; Time: {timelist[indexforminheight]}; Range: {xlist[indexforminheight]}"
    )


def main():
    h, g, m, k, vi, angle, dt, endtime, graph, time, dist = main_matplotlib.get_vals()
    printMethodAdvanced(h, g, m, k, vi, angle, dt, endtime, graph, time, dist)


if __name__ == "__main__":
    main()
