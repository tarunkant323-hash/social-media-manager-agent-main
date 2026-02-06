import random
import json

def schedule_post(decision, data_path):
    print("\nScheduling Post...")
    print(f"Content : {decision['content']}")
    print(f"Type    : {decision['type']}")
    print(f"Time    : {decision['time']}")
    print("Post scheduled successfully!")

    # Simulate engagement
    likes = random.randint(30, 200)
    comments = random.randint(5, 50)

    print(f"Simulated Engagement -> Likes: {likes}, Comments: {comments}")

    # Append to history (learning)
    new_post = {
        "content": decision["content"],
        "type": decision["type"],
        "time": decision["time"],
        "likes": likes,
        "comments": comments
    }

    with open(data_path, 'r+') as file:
        data = json.load(file)
        data.append(new_post)
        file.seek(0)
        json.dump(data, file, indent=2)

    print("Memory updated with new engagement data.")
