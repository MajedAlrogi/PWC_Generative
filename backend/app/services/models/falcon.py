import json
import os
import replicate

os.environ["REPLICATE_API_TOKEN"] = "[ENTER API KEY]"

def generate_response_falcon(prompt):
    prescript = "You are a strict chat-bot. your will be given information and a question. you should only answer the question if the answer can be found in the information provided. if the answer is not present in the information you MUST state that you cannot answer the question and ask the user to contact a human representative"
    input={
        "seed": -1,
        "top_p": 0.5,
        "prompt": f"{prescript}\n{prompt}",
        "max_length": 1000,
        "temperature": 0.75,
        "length_penalty": 1,
        "repetition_penalty": 1
    }

    output = replicate.run(
        "joehoover/falcon-40b-instruct:7d58d6bddc53c23fa451c403b2b5373b1e0fa094e4e0d1b98c3d02931aa07173",
        input=input
    )
    return " ".join(output)