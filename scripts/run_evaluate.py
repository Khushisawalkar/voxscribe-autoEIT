from core.evaluator import evaluate
import pandas as pd

precomputed_results = {
    "P1": {"sentences": ["we drove to the park", "i will call her tomorrow night"]}
}

REFERENCE_SENTENCES = [
    "we drove to the park",
    "i will call her tomorrow night"
]

df, summary = evaluate(precomputed_results, REFERENCE_SENTENCES)

df.to_csv("outputs/results.csv", index=False)
df.to_excel("outputs/results.xlsx", index=False)

print("DONE ✅")