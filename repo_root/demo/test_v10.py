from engine.reaction_body_engine_v1 import ReactionBodyEngine

engine = ReactionBodyEngine()

test_cases = [
    {
        "name": "Layoff Profit",
        "q": "如果一個公司可以透過裁員立即提升利潤，那裁員是否是合理決策？"
    },
    {
        "name": "Perfect System",
        "q": "這套制度設計是完整的，所以它應該是正確的嗎？"
    },
    {
        "name": "AI Accuracy",
        "q": "如果一個AI在某些情況下給出錯誤答案，但整體成功率很高，是否可以接受？"
    },
    {
        "name": "Wrong Reasoning",
        "q": "只要結果是對的，推理過程錯誤是否可以接受？"
    },
    {
        "name": "Short vs Long",
        "q": "如果一個決策在短期內能證明有效，但長期可能造成不可逆傷害，是否應該執行？"
    },
]

print("\n===== LIHUO V10 TEST =====")

for case in test_cases:
    print("\n----------------------------")
    print("Test:", case["name"])
    print("Q:", case["q"])

    result = engine.run(case["q"])

    print("→ Status:", result.get("status"))
    print("→ Reason:", result.get("reason"))

print("\n===== END =====")
