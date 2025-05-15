# main.py

import os
from dotenv import load_dotenv
from agent.planner import generate_plan
from agent.executor import execute_tasks
from agent.memory import save_results
from agent.reporter import generate_report

# Load environment variables (e.g., OpenAI API key)
load_dotenv()

def main():
    print("🧠 Autonomous Research Agent\n")

    # Step 1: Accept user goal
    goal = input("Enter your research goal: ").strip()
    if not goal:
        print("❌ No goal entered. Exiting.")
        return

    # Step 2: Plan subtasks using GPT
    print("\n📌 Planning subtasks...")
    plan = generate_plan(goal)

    print("\n✅ Subtasks:")
    for i, task in enumerate(plan, 1):
        print(f"{i}. {task}")

    # Step 3: Execute subtasks and collect findings
    print("\n🔁 Executing research tasks...")
    results = execute_tasks(plan)

    # Step 4: Save results to local memory
    save_results(goal, results)

    # Step 5: Save a clean, formatted research report
    generate_report(goal, results)

    print("\n✅ Research complete.")

if __name__ == "__main__":
    main()
