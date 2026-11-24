import anthropic

client = anthropic.Anthropic()

with open("recipes.txt") as f:
    recipes = f.read()

question = "I have chicken thighs, rice, and spinach, and 30 minutes. What can I make?"

prompt = f"""Here are my recipes:

{recipes}

Using ONLY the recipes above, answer this question: {question}"""

response = client.messages.create(
    model="claude-sonnet-5-5",
    max_tokens=1500,
    messages=[{"role": "user", "content": prompt}],
)

for block in response.content:
    if block.type == "text":
        print(block.text)
