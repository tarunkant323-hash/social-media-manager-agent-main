from collections import defaultdict

def compress_memory(posts):
    type_engagement = defaultdict(int)
    time_engagement = defaultdict(int)

    for post in posts:
        engagement = post["likes"] + post["comments"]
        type_engagement[post["type"]] += engagement
        time_engagement[post["time"]] += engagement

    # Find best type and time
    best_type = max(type_engagement, key=type_engagement.get)
    best_time = max(time_engagement, key=time_engagement.get)

    summary = (
        f"Posts of type '{best_type}' around '{best_time}' "
        f"receive the highest audience engagement."
    )

    return summary, best_type, best_time
