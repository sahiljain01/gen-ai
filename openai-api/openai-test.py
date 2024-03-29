import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a fixed income trader."},
            {"role": "user", "content": "Explain what an interest rate swap is."},
            ]
        )

print(json.dumps(json.loads(completion.model_dump_json()), indent=4))

