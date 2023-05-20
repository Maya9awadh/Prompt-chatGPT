# -*- coding: utf-8 -*-
"""

@author: mayaa
"""

import openai

openai.api_key='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'

model="text-davinci-003"
prompt=input("Ask a question: ")

while prompt !='stop':
    completion=openai.Completion.create(engine=model,prompt=prompt,max_tokens=1024,n=1,stop=None,temperature=0.6)
    response=completion.choices[0].text
    print(response)
    prompt=input("Ask a question: ")
