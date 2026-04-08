# HOW TO TEST LIHUO DECISION LAYER

## Requirements

* Python 3.10+
* Any local LLM (optional)

---

## Step 1 — Clone

```bash
git clone https://github.com/YOUR_USERNAME/lihuo-decision-layer.git
cd lihuo-decision-layer
```

---

## Step 2 — Run Demo

```bash
python demo/demo_cli.py
```

---

## Step 3 — Try Questions

Example:

* Is it acceptable if reasoning is wrong but the result is correct?
* Is layoffs justified if profit increases?
* If an AI is mostly correct but sometimes wrong, is it acceptable?

---

## Expected Behavior

The system will NOT generate answers.

Instead it will return:

* 🚫 BLOCKED
* ⏳ DEFERRED
* ✅ ALLOWED

---

## Key Idea

This system does not answer questions.

It decides:

> Whether an answer should be allowed to exist.

---

## Optional — Integrate with your LLM

You can place this layer between:

User → LLM

Modify:

```python
result = engine.run(user_input)
```

If BLOCKED → do not call LLM
If ALLOWED → pass to LLM

---

## Notes

* No training required
* No API key needed
* Fully local
