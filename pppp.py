import pandas as pd
import numpy as np
from openai.embeddings_utils import get_embedding, cosine_similarity
import openai
import config

openai.api_key = config.OPENAI_API_KEY
query= input("Busqueda: ")
search_term_vector = get_embedding(str(query), engine="text-embedding-ada-002")

df = pd.read_csv(r'/Users/ramirofernandezdeullivarri/Documents/CMQ_prompts_embeddings2.csv', delimiter=',',encoding='utf-8')
#df = df.head(500)
df['embedding_prompts'] = df['embedding_prompts'].apply(eval).apply(np.array)
df["similarities"] = df['embedding_prompts'].apply(lambda x: cosine_similarity(x, search_term_vector))
sorted_by_similarity = df.sort_values("similarities", ascending=False).head(1)

results= [{'outputs_tags': sorted_by_similarity['outputs_tags'].values.tolist(),
          'tags':sorted_by_similarity['tags'].values.tolist(),
          'values':sorted_by_similarity['values'].values.tolist()}]
# results =[{'outputs_tags': sorted_by_similarity['outputs_tags'].values.tolist(),
#                  'tags':sorted_by_similarity['tags'].values.tolist(),
#                  'values':sorted_by_similarity[''].values.tolist()}]
if 'values2' in sorted_by_similarity:
  results.append({'tags2': sorted_by_similarity['tags2'].values.tolist(),
                  'values2': sorted_by_similarity['values2'].values.tolist()})
  
print(results)