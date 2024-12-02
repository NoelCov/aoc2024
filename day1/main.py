# Okay. If we make two lists and order them in ascending order we have what we need.
# Once we have that, we measure the distance between each point and get the total distance using that.


left = []
right = []
with open('./input.txt', mode='r', encoding='utf-8') as file:
    for line in file:
        left_val, right_val = line.strip().split("   ")
        left.append(left_val)
        right.append(right_val)
      
    # left.sort()
    # right.sort()

    # total_distance = 0
    # for i in range(len(left)):
    #     total_distance += abs(int(left[i]) - int(right[i]))
    # print(total_distance)
    result = 0
    for item in left:
        counter = 0
        for val in right:
            if val == item:
                counter += 1
        result += int(item) * counter
    print(result)
# 478 is wrong?
# 2000468

# Now I have to check how many times each number in the left list appears in the right list
# Make a set with unique numbers in the left.
# Then make a list that stores the frequencies?