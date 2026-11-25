import anthropic

client = anthropic.Anthropic()

with open("recipes.txt") as f:
    text = f.read()

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

top = sorted(recipes, key=score, reverse=True)[:3]
context = "\n\n".join(top)

prompt = f"""Here are the most relevant recipes from my collection:

{context}

Using ONLY the recipes above, answer this question: {question}"""

response = client.messages.create(
    model="claude-sonnet-5-5",
    max_tokens=1500,
    messages=[{"role": "user", "content": prompt}],
)

for block in response.content:
    if block.type == "text":
        print(block.text)
