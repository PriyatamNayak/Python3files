# =============================================================================
# 1.                  Simple Movie Recommendation system
# =============================================================================

from tkinter import Text
from tkinter import Button
from tkinter import Scrollbar
import pandas as pd

# =============================================================================
# 
# def show_data():
#     data = pd.read_csv("F:\\tutorials\\python\\learning\\datasets\\movies_metadata.csv")
#     select_data = data[["title","vote_count","vote_average","budget"]]
#     heading = select_data.head(5)
#     print(heading)
#     ta.insert(0.0, heading)
# 
#     original = "\n\nOriginal dataset (rows X columns): {}\n".format(data.shape)
#     print(original)
#     ta.insert(END, original)
# 
#     mean_score = data["vote_average"].mean()
#     ms = "\nMean score value for all the movies: {}\n".format(mean_score)
#     print(ms)
#     ta.insert(END, ms)
#     # Calculate the minimum number of votes required to be in the chart, m
#     vote_count = data['vote_count'].quantile(0.90)
#     print(vote_count)
#     ta.insert(END, "\nVote count:{}\n".format(vote_count))
# 
#     q_movies = data.copy().loc[data['vote_count'] >= vote_count]
# 
#     fd = "\nFiltered dataset (rows X columns): {}\n".format(q_movies.shape)
#     print(fd)
#     ta.insert(END,fd)
#     #m = vote_count , C= mean_Score
#     def weighted_rating(x, vote_count= vote_count, mean_score = mean_score):
#         v = x["vote_count"]
#         R = x["vote_average"]
#         return (v/(v+vote_count) * R) + (vote_count/(vote_count+v) * mean_score)
# 
#     q_movies["score"] = q_movies.apply(weighted_rating, axis = 1)
#     q_movies = q_movies.sort_values("score",ascending = False)
#     movies = q_movies[["title","vote_count", "vote_average", "score"]]
# 
#     res = movies.head(20)
#     print(res)
#     ta.insert(END,"\nRECOMMENDED: \n\n")
#     ta.insert(END, res)
# 
# root = Tk()
# root.title("recommender")
# root.geometry("450x430")
# 
# b = Button(root, text = "Result", command = show_data)
# b.grid(row = 0, columnspan = 1, sticky =[E,W] )
# 
# ta = Text(root, bd = 5, width = 80, wrap = WORD, undo= True)
# ta.grid(row = 1, column = 0, sticky = W)
# sbar = Scrollbar(root, command = ta.yview, orient= VERTICAL)
# sbar.grid(row =1, column= 1, sticky = [N,S,E,W])
# sbar2 = Scrollbar(root, command = ta.xview, orient = HORIZONTAL)
# sbar2.grid(row =2, column= 0,sticky = [N,S,E,W])
# ta.config(xscrollcommand=sbar2.set, yscrollcommand=sbar.set)
# 
# root.mainloop()
# =============================================================================

# =============================================================================
# 2.            Content Based Recommendation System
#           i)  Plot Description Based Recommender
# =============================================================================

# =============================================================================
# import scipy
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import linear_kernel
# 
# data = pd.read_csv("F:\\tutorials\\python\\learning\\datasets\\movies_metadata.csv")
# select_data = data["overview"]
# heading = select_data.head()
# print(heading)
# 
# #Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
# tfidf = TfidfVectorizer(stop_words="english")
# 
# #Replace NaN with an empty string
# final_data= select_data.fillna("")
# 
# #Construct the required TF-IDF matrix by fitting and transforming the data
# tfidf_matrix = tfidf.fit_transform(final_data)
# 
# #Output the shape of tfidf_matrix
# print(tfidf_matrix.shape)
# 
# cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
# 
# #Construct a reverse map of indices and movie titles
# indices = pd.Series(data.index, index = data["title"]).drop_duplicates()
# 
# # Function that takes in movie title as input and outputs most similar movies
# def get_recommendations(title, cosine_sim=cosine_sim):
#     # Get the index of the movie that matches the title
#     idx = indices[title]
# 
#     # Get the pairwsie similarity scores of all movies with that movie
#     sim_scores = list(enumerate(cosine_sim[idx]))
# 
#     # Sort the movies based on the similarity scores
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
# 
#     # Get the scores of the 10 most similar movies
#     sim_scores = sim_scores[1:11]
# 
#     # Get the movie indices
#     movie_indices = [i[0] for i in sim_scores]
# 
#     # Return the top 10 most similar movies
#     return data['title'].iloc[movie_indices]
# 
# get_recommentations("The Godfather")
# 
# =============================================================================
# =============================================================================
#           ii.)credits, genre , keywords based recommender
# =============================================================================
from ast import literal_eval
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

credit = pd.read_csv("F:\\tutorials\\python\\learning\\datasets\\credits.csv")
keywords= pd.read_csv("F:\\tutorials\\python\\learning\\datasets\\keywords.csv")
data = pd.read_csv("F:\\tutorials\\python\\learning\\datasets\\movies_metadata.csv")

data =data.drop([19730,29503,35587])
keywords["id"] = keywords["id"].astype("int")
credit["id"] = credit["id"].astype("int")
data["id"] = data["id"].astype("int")
data = data.merge(credit, on = "id")
data = data.merge(keywords, on ="id")
select_data = data[["title","cast","keywords","crew","genres"]]  #selecting specific columns to display
heading = select_data.head(5)
print("original data:")
print(heading)

features = ["cast","crew","keywords","genres"]
for feature in features:
    data[feature] = data[feature].apply(literal_eval)
    #print(data[feature])

def get_director(x):
    for i in x:
        if i["job"] == "Director":
            return i["name"]
    return np.nan

def get_list(x):
    if isinstance(x, list):
        names =[i["name"]for i in x]
        if len(names)>3:
            names = names[:3]
        return names
    return []

data["director"] = data["crew"].apply(get_director)
features = ["cast","keywords", "genres"]
for feature in features:
    data[feature] = data[feature].apply(get_list)

select_data = data[["title","cast","director","keywords","genres"]].head(3)
print("after feature creation:")
print(select_data)

def clean_data(x):
    if isinstance(x,list):
        return [str.lower(i.replace(" ","")) for i in x]
    else:
         if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
         else:
            return ""

features = ["cast","keywords", "genres"]
for feature in features:
    data[feature] = data[feature].apply(clean_data)

select_data = data[["title","cast","director","keywords","genres"]].head(3)
print("after clean data:")
print(select_data)

def create_soup(x):
    final = ("{0}{1}{2}{3}".format(x['keywords'],x['cast'],x['director'],x['genres']))
    #' '.join(x['keywords']) + ' ' + ' '.join(x['cast']) + ' ' + x['director'] + ' ' + ' '.join(x['genres'])
    return final
data["soup"] = data.apply(create_soup, axis=1)

count = CountVectorizer(stop_words="english")
count_matrix = count.fit_transform(data["soup"])

cosine_sim2 = cosine_similarity(count_matrix, count_matrix)
data = data.reset_index()
indices = pd.Series(data.index, index=data["title"])

def get_recommendations(title, cosine_sim):
   # Get the index of the movie that matches the title
     idx = indices[title]
 
     # Get the pairwsie similarity scores of all movies with that movie
     sim_scores = list(enumerate(cosine_sim[idx]))
 
     # Sort the movies based on the similarity scores
     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
 
     # Get the scores of the 10 most similar movies
     sim_scores = sim_scores[1:11]
 
     # Get the movie indices
     movie_indices = [i[0] for i in sim_scores]
 
     # Return the top 10 most similar movies
     return data["title"].iloc[movie_indices]

get_recommendations("The Dark Knight Rises", cosine_sim2)