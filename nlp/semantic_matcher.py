# nlp/semantic_matcher.py

from sentence_transformers import SentenceTransformer, util
import torch

# Load model once when the file is imported
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Define goal labels and semantic descriptions
FLAVOUR_GOALS = {
    "increase florality": "Enhance floral notes",
    "increase body": "Thicker, heavier cup",
    "syrupy body": "Sticky, dense, syrup-like texture",
    "reduce bitterness": "Less bitter, smoother taste",
    "highlight acidity": "Bright, sparkling, acidic profile",
    "increase sweetness": "More sugary, honey-like sweetness",
    "enhance clarity": "Clean, clear-tasting profile",
    "mellow profile": "Gentle, soft cup, no extremes",
    "highlight fruit notes": "Fruity, juicy tones",
    "balance cup": "No extremes, harmonious taste"
}

goal_keys = list(FLAVOUR_GOALS.keys())
goal_descriptions = list(FLAVOUR_GOALS.values())

# Precompute goal embeddings
goal_embeddings = model.encode(goal_descriptions, convert_to_tensor=True)

def match_flavour_goal(user_input: str) -> str:
    user_embedding = model.encode(user_input, convert_to_tensor=True)
    similarity_scores = util.pytorch_cos_sim(user_embedding, goal_embeddings)
    best_idx = int(torch.argmax(similarity_scores))
    return goal_keys[best_idx]
