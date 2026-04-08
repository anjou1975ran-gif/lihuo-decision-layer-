from engine.reaction_body_engine_v1 import ReactionBodyEngine

engine = ReactionBodyEngine()

def run_demo():
    while True:
        q = input("\nEnter question (or 'exit'): ")
        if q == "exit":
            break

        result = engine.run(q)

        print("\nResult:")

        status = result.get("status")

        if status == "BLOCKED":
            print("🚫 BLOCKED")
            print("Reason:", result.get("reason", "N/A"))

        elif status == "DEFERRED":
            print("⏳ DEFERRED")
            print("Reason:", result.get("reason", "N/A"))

        else:
            print("✅ ALLOWED")

if __name__ == "__main__":
    run_demo()
