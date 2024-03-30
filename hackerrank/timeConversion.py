def timeConversion(s):
    time_split = s[:-2].split(":")
    am_pm = s[-2:]

    if am_pm == "PM" and time_split[0] != "12":
        time_split[0] = str(int(time_split[0]) + 12)
    elif am_pm == "AM" and time_split[0] == "12":
        time_split[0] = "00"

    military_time = ":".join(time_split)
    return military_time

if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)
