from CORE.reaction_body_engine_v1 import ReactionBodyEngine

engine = ReactionBodyEngine()

A = "A reasoning appears valid but lacks full constraints."
B = "Even if incomplete, results are acceptable."

def run(tag, text):
    print(f"\n===== {tag} =====")
    result = engine.run(text)
    print("decision:", result["decision"])
    for b in result.get("branches", []):
        print(" ", b["path"], "|", b["score"], "|", b["status"])

run("RUN1 - A", A)
run("RUN2 - B", B)
run("RUN3 - A", A)
