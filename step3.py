with open("recipes.txt") as f:
    text = f.read()

# Split into one chunk per recipe (blank line between recipes)
recipes = [r.strip() for r in text.split("\n\n") if r.strip()]

question = "I have chicken thighs, rice, and spinach, and 30 minutes. What can I make?"

SKIP = {"i", "have", "and", "a", "the", "what", "can", "make",
        "minutes", "with", "to", "of", "in", "on", "or", "for"}

def words(s):
    for ch in ",.?:":
        s = s.replace(ch, " ")
    return set(s.lower().split()) - SKIP

def score(recipe):
    return len(words(question) & words(recipe))

ranked = sorted(recipes, key=score, reverse=True)

for r in ranked[:3]:
    print(r.split("\n")[0], "-> score", score(r))
