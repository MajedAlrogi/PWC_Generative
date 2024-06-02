from openai import OpenAI
import os
from dotenv import load_dotenv


# currently researching https://platform.openai.com/docs/guides/prompt-engineering to make better prompts

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')

# Initialize the client with the API key
client = OpenAI(api_key=api_key)

# Example prompt
#prompt = """[info] 'Here is detailed information about recursion: Recursion is a method where the solution to a problem depends on solutions to smaller instances of the same problem. This technique uses functions that call themselves within their own code.' 
#Now use the information above to answer the question.
#[question] 'How tall is the empire state building?'"""

# Generating response
#print(generate_response(prompt))

#uses gpt-3.5-turbo
def generate_response(prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Please use only the information provided to answer the question. If the answer cannot be found, ask the user to contact a human representative"},
                  {"role": "user", "content": prompt}]
    )
    #print(completion.choices)
    response = completion.choices[0].message.content
    return response
#uses gpt-4o [Cheaper]
def generate_response_v4(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "Please use only the information provided to answer the question. If the answer cannot be found, ask the user to contact a human representative"},
                  {"role": "user", "content": prompt}]
    )
    #print(completion.choices)
    response = completion.choices[0].message.content
    return response


# Example prompt
#prompt = """[Question] 'How tall is the empire state building?
#[Answers] 1. ans 2.ans 3. ans 4.ans
def judge_answer(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "You are a silent judge. you will be given a question and a numbered list of answers. your job is to strictly output the words of the answer the best answers the question"},
                  {"role": "user", "content": prompt}]
    )
    #print(completion.choices)
    response = completion.choices[0].message.content
    return response