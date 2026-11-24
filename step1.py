import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-5-5",
    max_tokens=300,
    messages=[
        {"role": "user", "content": "Suggest one quick dinner using chicken and rice."}
    ],
)

print(response.content[0].text)
