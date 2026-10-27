from openai import OpenAI

client = OpenAI(
api_key="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",
)


user_input = input("Enter your message: ")

response = client.responses.create(
    model="o1-pro",
    input=user_input
)

print("Response:")
print(response.output_text)
