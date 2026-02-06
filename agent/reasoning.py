def decide_next_post(best_type, best_time):
    if best_type == "educational":
        content = "Learn a new AI concept in 5 minutes!"
    elif best_type == "motivational":
        content = "Start your day with positive energy and focus!"
    elif best_type == "challenge":
        content = "Today's coding challenge: Solve this problem!"
    else:
        content = "Stay tuned for amazing content!"

    decision = {
        "content": content,
        "time": best_time,
        "type": best_type
    }

    return decision
