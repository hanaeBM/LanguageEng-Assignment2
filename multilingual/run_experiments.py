import pandas as pd
import numpy as np
import re
import sys
from gensim.models import KeyedVectors
# Some useful libraries
from scipy.spatial.distance import cdist
from sklearn.feature_extraction.text import TfidfVectorizer


# --- Data Loading ---
def load_data():
    df = pd.read_csv("data/aligned_literature_en_es.csv")
    en_model = KeyedVectors.load_word2vec_format("data/mini.en.vec")
    es_model = KeyedVectors.load_word2vec_format("data/mini.es.vec")
    return df, en_model, es_model


# --- Evaluation ---
def run_eval(en_vecs, es_vecs,df, label, metric='cosine'):
    print(f"\n--- {label} Results ---")
    for dir_name, q, g,lang in [("EN->ES", en_vecs, es_vecs,"en"), ("ES->EN", es_vecs, en_vecs,"es")]:
        acc1 = compute_accuracy(q, g,df,lang,metric, k=1)
        acc3 = compute_accuracy(q, g,df,lang,metric, k=3)
        print(f"{dir_name} | Top-1: {acc1:.2%} | Top-3: {acc3:.2%}")

        
def compute_accuracy(query_vecs, gallery_vecs,df,lang, metric='cosine', k=1):
    distances = cdist(query_vecs, gallery_vecs, metric=metric)
    distances=np.argsort(distances, axis=1)
    nearest = distances[:, :k]
    # add sentences incorect:
    Inc=[]
    dict={"en":df.english_text,
          "es":df.spanish_text}
    correct = 0
    for i in range(len(query_vecs)):
        if i in nearest[i]:
            correct += 1
         # add sentences incorect:
        else:
                Inc.append(f"{dict[lang][i]}(idx:{np.where(distances[i]==i)}) ")# AJOUTER INDICE !!
    if k==3:
        print(f"3 Failed Sentences{Inc[:3]}")
    return correct / len(query_vecs)

def ConstructBaseline(df, en_model, es_model):
    
    
    es = df['spanish_text']
    en = df['english_text']
    
    en_base = np.zeros((len(df), en_model.vector_size))
    es_base = np.zeros((len(df), es_model.vector_size))
    
    pattern = r"[a-zA-ZáéíóúñüÁÉÍÓÚÑÜ]+"
    
    L = [
        (en, en_model, en_base),
        (es, es_model, es_base)
    ]
    
    for texts, model, base in L:
        for i, s in enumerate(texts):
            
            if not isinstance(s, str):
                continue
            
            tokens = re.findall(pattern, s.lower())
            
            mean = np.zeros(model.vector_size)
            count = 0
            
            for w in tokens:
                if w in model:
                    mean += model[w]
                    count += 1
            
            if count != 0:
                base[i] = mean / count
    
    return en_base, es_base


def TfIdf(df,en_model,es_model):
    pattern = r"[a-zA-ZáéíóúñüÁÉÍÓÚÑÜ]+"
    es=df['spanish_text']
    en=df['english_text']
    en_base = np.zeros((len(df), en_model.vector_size))
    es_base = np.zeros((len(df), es_model.vector_size))
    L=[[en,en_model,en_base],
       [es,es_model,es_base]]
    for v in L:
        dfreq={}
        tf={}
        for i,s in enumerate(v[0]):
            tf[i]={}
            tokens = re.findall(pattern, s.lower())
            tot=len(tokens)
            for w in tokens:
                w = w.lower()
                if w in tf[i]:
                    tf[i][w]+=1/tot
                else:
                    tf[i][w]=1/tot
                    if w not in dfreq:
                        dfreq[w]=1
                    else:
                        dfreq[w]+=1


        texts, model, base=v
        for i, s in enumerate(texts):
            
            if not isinstance(s, str):
                continue
            
            tokens = re.findall(pattern, s.lower())
            
            mean = np.zeros(model.vector_size)
            count = 0
            
            for w in tokens:

                if w in model:
                    base[i] += model[w]*tf[i][w]*np.log(len(v[0])/dfreq[w])
                    count += 1
            if count!=0:
                base[i]=base[i]/count


                    
               
    
    return en_base, es_base



   

    
def main():
    df, en_model, es_model = load_data()   
    
    # 1. Baseline (Simple Mean)
    print(df.head)
    print(en_model)
    en_base,es_base=ConstructBaseline(df,en_model,es_model)
    run_eval(en_base, es_base,df, "Baseline (Simple Mean)")
    
    # 2. TF-IDF Weighted (No Centering)
    # ----------------------
    # REPLACE WITH YOUR CODE
    en_tfidf_vecs,es_tfidf_vecs= TfIdf(df,en_model,es_model)
    
    # ----------------------
    run_eval(en_tfidf_vecs, es_tfidf_vecs,df, "TF-IDF Weighted")

    
    # Global means for Centering
    # ----------------------
    # REPLACE WITH YOUR CODE
    mean_en = np.mean(en_base,axis=0)
    mean_es = np.mean(es_base,axis=0)
    mean_en_tfidf = np.mean(en_tfidf_vecs,axis=0)
    mean_es_tfidf = np.mean(es_tfidf_vecs,axis=0)
    # ----------------------
    
    # 3. Mean-Centered (No TF-IDF) 
    run_eval(en_base - mean_en, es_base - mean_es,df,"Mean-Centered (Simple)")
    
    # 4. Mean-Centered + TF-IDF
    run_eval(en_tfidf_vecs - mean_en_tfidf, es_tfidf_vecs - mean_es_tfidf, df,"Mean-Centered + TF-IDF")

if __name__ == "__main__":
    main()
