import os
import replicate

os.environ["REPLICATE_API_TOKEN"] = "[ENTER API KEY]"


# Prompts
#prompt_input = """[info] 'Here is detailed information about recursion: Recursion is a method where the solution to a problem depends on solutions to smaller instances of the same problem. This technique uses functions that call themselves within their own code.' 
#Now use the information above to answer the question.
#[question] 'How tall is the empire state building?'"""
def generate_response_llama(prompt_input):
    input = {
    "top_p": 1,
    "prompt": prompt_input,
    "temperature": 0.75,
    "system_prompt": "You are an assistand designed ONLY to answer based on the information in the prompt.Please use only the information provided to answer the question. If the answer cannot be found in the information, ONLY reply with this 'I cannot find the answer to your question. Please contact a human representative'. You must use this phrasing with nothing more or less if the information does not contain the answer",
    "max_new_tokens": 800,
    "repetition_penalty": 1
    }
    # Initialize a variable to hold the accumulated responses
    response = ""

    # Stream the responses and concatenate them to the response variable
    for event in replicate.stream(
        "meta/llama-2-70b-chat",
        input=input
    ):
        #print("Received event data:", event.data)  # Print the raw data of the event for debugging
        if event.data.strip() not in ["{}", ""]:
            response += event.data

    # Return the accumulated response as a string
    return response.strip()