def S1(Time, duration):
    if Time == 0:
        quit()
    if duration < s1:
        print("S1 " + str(Time) + " " + str(duration))
        S1(Time - 1, duration + 1)
    else:
        S2(Time, 0)


def S2(Time, duration):
    if Time == 0:
        quit()
    if duration < s2:
        print("S2 " + str(Time) + " " + str(duration))
        S2(Time - 1, duration + 1)
    else:
        S3(Time, 0)


def S3(Time, duration):
    if Time == 0:
        quit()
    if duration < s3:
        print("S3 " + str(Time) + " " + str(duration))
        S3(Time - 1, duration + 1)
    else:
        S4(Time, 0)


def S4(Time, duration):
    if Time == 0:
        quit()
    if duration < s4:
        print("S4 " + str(Time) + " " + str(duration))
        S4(Time - 1, duration + 1)
    else:
        S5(Time, 0)


def S5(Time, duration):
    if Time == 0:
        quit()
    if duration < s5:
        print("S5 " + str(Time) + " " + str(duration))
        S5(Time - 1, duration + 1)
    else:
        S6(Time, 0)


def S6(Time, duration):
    if Time == 0:
        quit()
    if duration < s6:
        print("S6 " + str(Time) + " " + str(duration))
        S6(Time - 1, duration + 1)
    else:
        S1(Time, 0)


s1 = int(input("ENTER THE DURATION OF S1:"))
s2 = int(input("ENTER THE DURATION OF S2:"))
s3 = int(input("ENTER THE DURATION OF S3:"))
s4 = int(input("ENTER THE DURATION OF S4:"))
s5 = int(input("ENTER THE DURATION OF S5:"))
s6 = int(input("ENTER THE DURATION OF S6:"))
time = int(input("ENTER THE DURATION OF TLC:"))

if __name__ == '__main__':
    S1(time, 0)
