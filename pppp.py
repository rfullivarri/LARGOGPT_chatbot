import pandas as pd
import numpy as np
from openai.embeddings_utils import get_embedding, cosine_similarity
import openai
import config
import class_n_search

openai.api_key = config.OPENAI_API_KEY
query= input("Busqueda: ")
search_term_vector = get_embedding(str(query), engine="text-embedding-ada-002")

df = pd.read_csv(r'/Users/ramirofernandezdeullivarri/Documents/CMQ_prompts_embeddings2.csv', delimiter=',',encoding='utf-8')
#df = df.head(500)
df['embedding_prompts'] = df['embedding_prompts'].apply(eval).apply(np.array)
df["similarities"] = df['embedding_prompts'].apply(lambda x: cosine_similarity(x, search_term_vector))
sorted_by_similarity = df.sort_values("similarities", ascending=False).head(1)
print(sorted_by_similarity)


# # results= [{'outputs_tags': sorted_by_similarity['outputs_tags'].values.tolist()},{
# #           'tags':sorted_by_similarity['tags'].values.tolist(),
# #           'values':sorted_by_similarity['values'].values.tolist()}]

#if 'values2' in sorted_by_similarity and not sorted_by_similarity['values2'].empty:
if sorted_by_similarity['values2'].isnull().any():
    results = ({'outputs_tags': sorted_by_similarity['outputs_tags'].values.tolist()},
                   {'tag':sorted_by_similarity['tags'].values.tolist(),
                   'value':sorted_by_similarity['values'].values.tolist()})
else:
    results = ({'outputs_tags': sorted_by_similarity['outputs_tags'].values.tolist()},
               {'tag':[sorted_by_similarity['tags'].values.tolist(), sorted_by_similarity['tags2'].values.tolist()],
                'value':[sorted_by_similarity['values'].values.tolist(), sorted_by_similarity['values2'].values.tolist()]
                 })

  
print(results, "\n")  

#print(class_n_search.search_P(str(results[0]).replace("[","").replace("]",""), str(results[1]).replace("[","").replace("]","")))
  
#print(df)