AI Social Media Manager Agent
An autonomous AI agent that analyzes historical social media engagement, compresses audience insights into actionable memory, and intelligently decides what to post and when to post for maximum engagement.

This project demonstrates how AI agent architecture (Perception → Memory → Reasoning → Action → Learning) can be applied to social media management to simulate adaptive, data-driven content scheduling.

📌 Problem Statement
Social media managers rely heavily on historical engagement data to decide:

What type of content performs best
What time audience is most active
How to improve engagement over time
However, manually analyzing large content history is inefficient.

This project solves that by building an AI agent that:

Compresses content history into audience insights and autonomously schedules optimized posts.

🧠 AI Agent Architecture
This project follows a true AI Agent model:

Agent Component	Responsibility	File
Perception	Reads past post history	perception.py
Memory	Compresses engagement history into insights	memory.py
Reasoning	Decides next post content & timing	reasoning.py
Action	Schedules the post	action.py
Learning Loop	Updates memory from new engagement	action.py
Agent Brain	Connects all modules	agent.py
🔄 Agent Workflow
Read History → Analyze Engagement → Create Memory Summary
→ Decide Best Post → Schedule Post → Simulate Engagement
→ Update History (Learning)
📂 Project Structure
social-media-manager-agent/
│
├── agent/
│   ├── perception.py
│   ├── memory.py
│   ├── reasoning.py
│   ├── action.py
│   └── agent.py
│
├── data/
│   └── post_history.json
│
├── docs/
├── main.py
├── requirements.txt
└── README.md
⚙️ How It Works
1️⃣ Perception
Reads historical post data including:

Content type
Posting time
Likes and comments
2️⃣ Memory Compression
Calculates total engagement and produces insights like:

“Educational posts around 7:30 PM receive the highest engagement.”

This is compressed audience insight.

3️⃣ Reasoning
Uses memory to decide:

Best content type
Best posting time
Generates next post idea
4️⃣ Action
Schedules the post and simulates engagement.

5️⃣ Learning
New engagement is appended to history, allowing the agent to improve over time.

▶️ Running the Project
Requirements
Python 3.x

Install dependencies:

pip install -r requirements.txt
Run the agent
python main.py
Sample Output
Agent starting...

Memory Summary:
Posts of type 'educational' around '19:30' receive the highest audience engagement.

Agent Decision:
{'content': 'Learn a new AI concept in 5 minutes!', 'time': '19:30', 'type': 'educational'}

Scheduling Post...
Simulated Engagement -> Likes: 134, Comments: 34
Memory updated with new engagement data.

Agent cycle completed.
🌟 Unique Feature
Adaptive Learning Loop
Unlike a simple scheduler, this agent:

Learns from every new post
Updates its memory
Changes future decisions based on engagement trends
This makes the system adaptive and intelligent, not static.

🧪 Working Model Demonstration
When main.py is executed, the agent autonomously performs:

Data analysis
Insight generation
Decision making
Scheduling
Learning from results
This proves a complete working AI agent model.

🛠️ Tech Stack
Python
JSON (data storage)
Modular AI agent architecture
📘 Documentation
Detailed design and architecture explanation is available inside the /docs folder.

🚀 Future Enhancements
Integration with Twitter / LinkedIn APIs
Real-time analytics dashboard
Database storage instead of JSON
LLM-based post generation
🎯 Learning Outcome
This project demonstrates:

Practical implementation of AI agent design
Memory compression techniques
Autonomous reasoning systems
Adaptive learning from historical data
👤 Author
Harsha Vardhan

📜 License
This project is developed for academic and learning purposes.
