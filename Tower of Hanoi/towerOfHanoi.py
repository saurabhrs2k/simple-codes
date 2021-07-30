# Python Solution to popular problem of Tower of Hanoi
# uses recursion

def TowerOfHanoi(n, firstRod, thirdRod, middleRod):
    if n == 1:
        print("Lift Disk 1 from Rod ", firstRod, " and Place it to Rod ", thirdRod)
        return
    TowerOfHanoi(n-1, firstRod, middleRod, thirdRod)
    print("Lift Disk ", n, " from Rod ", firstRod, " to Rod ", thirdRod)
    TowerOfHanoi(n-1, middleRod, thirdRod, firstRod)


# number of disks initially on first rod
disks = 4
TowerOfHanoi(disks, 'A', 'C', 'B')
# A - first rod
# C - third rod
# B - middle rod
