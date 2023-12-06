from dao import UserDAO, BookDAO
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from flask import g

class RecommendationService:
    def __init__(self):
        self.user_dao = UserDAO()
        self.book_dao = BookDAO()

    def get_books_based_on_similar_users(self, user_id):
        # Fetch ratings data
        user_ratings = pd.DataFrame(self.user_dao.get_user_ratings(g.session, user_id))
        all_user_ratings  = pd.DataFrame(self.user_dao.get_all_user_ratings(g.session))
        ratings_sample = all_user_ratings.sample(frac=0.1)
        combined_ratings = pd.concat([user_ratings, ratings_sample]).drop_duplicates()

        # Create a user-item ratings matrix
        ratings_matrix = self._create_user_item_matrix(combined_ratings)

        # Calculate similarity between users
        user_similarities = cosine_similarity(ratings_matrix)
        
        # Get the most similar users to the given user_id
        similar_users = self._get_similar_users(user_id, user_similarities, ratings_matrix)

        # Get book recommendations based on similar users
        recommended_books = self._get_book_recommendations(similar_users, ratings_matrix)

        return recommended_books

    def _create_user_item_matrix(self, ratings):
        # Convert the ratings data to a user-item matrix
        ratings_matrix = pd.pivot_table(data=ratings, 
                                        values='rating', 
                                        index='user_id', 
                                        columns='book_id', 
                                        fill_value=0)
        return ratings_matrix

    def _get_similar_users(self, user_id, similarities, ratings_matrix):
        # Get similarity scores for the given user with all users
        user_index = ratings_matrix.index.get_loc(user_id)
        similarity_scores = pd.Series(similarities[user_index], index=ratings_matrix.index)

        # Exclude the current user and get top N similar users
        similarity_scores = similarity_scores.drop(user_id)
        top_similar_users = similarity_scores.nlargest(n=10).index  # Adjust 'n' as needed
        return top_similar_users

    def _get_book_recommendations(self, similar_users, ratings_matrix):
        # Aggregate the ratings of similar users
        similar_users_ratings = ratings_matrix.loc[similar_users]

        # Calculate the mean rating for each book and sort them
        book_recommendations = similar_users_ratings.mean(axis=0).sort_values(ascending=False)

        # Return top N book recommendations
        top_book_recommendations = book_recommendations.head(50).index.tolist()  
        return top_book_recommendations
    
    def get_popular_books(self, user_id, page):
        user_preferences = self.user_dao.get_user_preferences(g.session, user_id)
        print(user_preferences)
        popular_books = self.book_dao.fetch_popular_books(g.session, user_preferences, page)
        return popular_books
    
    def get_books_based_on_user_preferences(self, user_id, page):
        user_preferences = self.user_dao.get_user_preferences(g.session, user_id)
        user_rated_books = self.user_dao.get_user_rated_books(g.session, user_id)
        recommended_books = self.book_dao.fetch_books_by_preferences(g.session, user_preferences, user_rated_books, page)
        return recommended_books
