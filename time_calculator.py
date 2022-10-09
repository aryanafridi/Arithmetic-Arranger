def add_time(time, duration, day=None):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    time_format = {"am": 0, "pm": 12}
    form = lambda x, y: 0 if x else time_format[y]
    t, a = time.split(" ")
    time = [(int(t.split(":")[x]) + int(duration.split(":")[x]) + form(x, a.lower())) for x in range(2)]
    time = [time[0]+int(time[1] / 60), time[1] % 60]
    final_time = [time[0] % 12, time[1], list(time_format.keys())[int(time[0] % 24 / 12)].upper(),  int(time[0] / 24)]
    final_day = "" if day is None else f", {days[(days.index(day.capitalize()) + final_time[3]) % 7]}"
    after_days = "" if final_time[3] == 0 else " (next day)" if final_time[3] == 1 else f" ({final_time[3]} days later)"
    return f"{12 if final_time[0]==0 else final_time[0]}:{final_time[1]:0>2} {final_time[2]}{final_day}{after_days}"


if __name__ == '__main__':
    add_time("3:00 PM", "3:10")
    add_time("11:30 AM", "2:32", "Monday")
    add_time("11:43 AM", "00:20")
    add_time("10:10 PM", "3:30")
    add_time("11:43 PM", "24:20", "tueSday")
    add_time("6:30 PM", "205:12")
