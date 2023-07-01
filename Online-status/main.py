def online_count(statuses):
    count = 0
    for status in statuses.values():
        if status == "online":
            count += 1
    return count

