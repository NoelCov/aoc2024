# I have to find which reports are safe 
# a report is safe if all the levels are either all increasing or all decreasing
# any two adjacent levels differ by at least one and at most three

# so we have to go 1 by 1, checking if it's increasing/decreasing and by how much?
# make a flag to check if it's increasing or decreasing, and check if the difference isn't much, check the flag afterwards and count how many are safe

def is_report_safe(report):
    levels = report.split(' ')

    increasing_flag = False
    decreasing_flag = False
    for i in range(1, len(levels) - 1):
        curr, prev = int(levels[i]), int(levels[i - 1])

        if i == len(levels) - 1:
            nxt = 0
        else:
            nxt = int(levels[i + 1])
        
        if 1 < abs(curr - prev) > 3 or 1 < abs(curr - nxt) > 3 or (increasing_flag and curr <= prev) or (decreasing_flag and curr >= prev):
            print("Bad report" + str(levels))
            return False
        
        if curr > prev:
            increasing_flag = True
        elif curr < prev:
            decreasing_flag = True
        else:
            return False
    print(levels)
    print(increasing_flag)
    print(decreasing_flag)
    print(increasing_flag or decreasing_flag)

    print()
    return increasing_flag or decreasing_flag

def process_data():    
    with open('./input.txt', mode='r', encoding='utf-8') as file:
        safe_reports = 0 

        for line in file:           
            line = line.strip()
            if is_report_safe(line):
                safe_reports += 1
        print(safe_reports)



process_data()

# 397 is wrong?
# 421 is wrong?
# 400 wrong?