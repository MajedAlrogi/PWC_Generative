
from .models import chatGPT
from .models import Llama
from .models import falcon

def generate_prompt(user_prompt, pages_of_text):
    prompt = "[INFORMATION]: "

    for page in pages_of_text:
        prompt = prompt + f"{page}\n"
    prompt = prompt + f"Now use the information above to answer the question \n[QUESTION]: {user_prompt}\n"
    return prompt

def clip_for_model(user_prompt,pages, ctx):
    prescript = "[INFORMATION]: "
    pages_combined = '\n'.join(pages) 
    postscript = f"Now use the information above to answer the question \n[QUESTION]: {user_prompt}\n"
    
    if len(f'{prescript}{pages_combined}\n{postscript}') > ctx:
        delta = ctx - len(prescript) + len(postscript) 
        new_pages = pages_combined[:delta]
        return f'{prescript}{new_pages}\n{postscript}'
    else: 
        return f'{prescript}{pages_combined}\n{postscript}'
        

def generate_selection(quest, answers):
    prompt = "".join("Question: ")
    prompt = prompt + quest
    prompt = prompt + "\n"
    i = 1
    for answer in answers:
        if answer:
            prompt = prompt + f"Answer {i}: {answer}\n"
            i+=1
    return prompt

def obtain_final_answer(user_prompt, pages):
    combine = lambda x: clip_for_model(user_prompt, pages, x)

    ans = []
    ans.append(chatGPT.generate_response(combine(16385)))
    ans.append(chatGPT.generate_response_v4(combine(128000)))
    ans.append(Llama.generate_response_llama(combine(4096)))
    #ans.append(falcon.generate_response_falcon(combine(1728)))

    selection = generate_selection(user_prompt,ans)

    final_ans = chatGPT.judge_answer(selection)

    return final_ans

