def get_rooms(s):
    if not s:
        return 0
    rooms = 1
    for i in range(len(s) - 1):
        if s[i][0] <= s[i + 1][0] <= s[i][1] or s[i][0] <= s[i + 1][1] <= s[i][1]:
            rooms += 1
        if s[i][0] > s[i + 1][0] and s[i][1] < s[i + 1][1]:
            rooms += 1
    return rooms
