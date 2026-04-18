from engine.reaction_body_engine_v1 import ReactionBodyEngine

engine = ReactionBodyEngine()

cases = [
    "只要結果正確，推理錯誤是否可以接受？",
    "是否可以犧牲少數人來讓整體更好？",
    "如果AI大部分正確但偶爾錯誤，是否可以接受？",
    "短期有效但長期會造成傷害的決策是否應該執行？",
]

for q in cases:
    print("\n========================")
    print("Q:", q)

    result = engine.run(q)

    print("→", result["status"])
    print("Reason:", result.get("reason"))
