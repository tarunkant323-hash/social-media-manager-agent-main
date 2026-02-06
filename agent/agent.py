from agent.perception import read_post_history
from agent.memory import compress_memory
from agent.reasoning import decide_next_post
from agent.action import schedule_post


class SocialMediaManagerAgent:

    def __init__(self, data_path):
        self.data_path = data_path

    def run(self):
        print("Agent starting...\n")

        # Perception
        posts = read_post_history(self.data_path)

        # Memory Compression
        summary, best_type, best_time = compress_memory(posts)
        print("Memory Summary:")
        print(summary)

        # Reasoning
        decision = decide_next_post(best_type, best_time)
        print("\nAgent Decision:")
        print(decision)

        # Action
        schedule_post(decision, self.data_path)


        print("\nAgent cycle completed.")
