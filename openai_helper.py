import openai
import config

openai.api_key = config.OPENAI_API_KEY


# role - ['system', 'assistant', 'user']
def get_response(prompt, role='user'):
    # TODO Add temperature as an argument
    generated_text = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": role, "content": prompt}
        ],
        temperature=0.5
    )
    return generated_text['choices'][0]['message']['content']
