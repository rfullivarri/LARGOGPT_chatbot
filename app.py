from flask import Flask, request, render_template
import openai
from openai.embeddings_utils import get_embedding, cosine_similarity
import pandas as pd
import numpy as np
import config
from class_n_search import search_P

app = Flask(__name__)

openai.api_key = config.OPENAI_API_KEY

@app.route('/static/<path:filename>')
def serve_static(filename):
  return app.send_static_file(filename)

@app.route('/')
def search_form():
  return render_template('search_form.html')


@app.route('/search')
def search():
    # Get the search query from the URL query string
    query = request.args.get('query')
    print('query:', query)

    search_term_vector = get_embedding(str(query), engine="text-embedding-ada-002")

    df = pd.read_csv(r'/Users/ramirofernandezdeullivarri/Documents/CMQ_prompts_embeddings2.csv', delimiter=',',encoding='utf-8')
    df['embedding_prompts'] = df['embedding_prompts'].apply(eval).apply(np.array)
    df["similarities"] = df['embedding_prompts'].apply(lambda x: cosine_similarity(x, search_term_vector))
    sorted_by_similarity = df.sort_values("similarities", ascending=False).head(1)

    
    if sorted_by_similarity['values2'].isnull().any():
        results = ({'outputs_tags': sorted_by_similarity['outputs_tags'].values[0]},
                       {'tag':sorted_by_similarity['tags'].values[0],
                       'value':sorted_by_similarity['values'].values[0]})
    else:
        results = ({'outputs_tags': sorted_by_similarity['outputs_tags'].values[0]},
                   {'tag':[sorted_by_similarity['tags'].values[0], sorted_by_similarity['tags2'].values[0]],
                    'value':[sorted_by_similarity['values'].values[0], sorted_by_similarity['values2'].values[0]]
                     })
    
    final_result = search_P(results)

    # Render the search results template, passing in the search query and results
    return render_template('search_results.html', query=query, results=final_result)


if __name__ == '__main__':
  app.run()