from google import genai

client = genai.Client(api_key='AIzaSyCJ9H_KCORPVgJ27e44qbzKwmCQmtC5InQ')

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)
