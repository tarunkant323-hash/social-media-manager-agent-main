from agent.agent import SocialMediaManagerAgent

def main():
    agent = SocialMediaManagerAgent("data/post_history.json")
    agent.run()

if __name__ == "__main__":
    main()
