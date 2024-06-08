import os
import random_patching.Config as cf
import random_patching.code_commit_statistic_analysis as ccsa

from tqdm import tqdm, trange

os.environ["http_proxy"]="127.0.0.1:7890"
os.environ["https_proxy"]="127.0.0.1:7890"

import openai
openai.api_key = cf.api_key

# list models
models = openai.Model.list()

# print the first model's id
# print(models.data[0].id)


commit_sec_list, non_commit_sec_list, non_sec_list = ccsa.rev_back_dataset()
for i in tqdm(range(len(commit_sec_list)), desc='Processing'):
    item = commit_sec_list[i]
    print("----- URL of IR:{} -----\n".format(item['Issue_Url']))
    print(">> Issue Title: {}\n >> Issue Body: {}".format(item['Issue_Title'], item['Issue_Body']))
    content = cf.content.format(5, item['Issue_Title'], item['Issue_Body'])

    # create a chat completion
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": content}])

    # print the chat completion
    print(">> Recommend Codes and Patches:\n {}".format(chat_completion.choices[0].message.content))