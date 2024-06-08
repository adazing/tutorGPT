from openai import OpenAI
import keys
client = OpenAI(api_key=keys.gpt_key)

MODEL = "gpt-3.5-turbo"


completion = client.chat.completions.create(
    model = MODEL,
  messages=[
    {"role": "system", "content": "You are a helpful assistant that generates 20 multiple choice questions based on a users' notes. Format must be a list that can be formatted in python, with tuples  "},
    {"role": "user", "content": "Hello! Could you solve 20 x 5?"}
  ]
                                            )