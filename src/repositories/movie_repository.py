
from src.models import Movies, db
class MovieRepository:

    

    def get_all_movies(self):
        # TODO get all movies from the DB
        
        return Movies.query.all()

    def get_movie_by_id(self, movie_id):
        # TODO get a single movie from the DB using the ID
        return Movies.query.get(movie_id)

    def create_movie(self, title, director, rating):
        # TODO create a new movie in the DB
        new_movie = Movies(title=title, director=director, rating=rating)
        db.session.add(new_movie)
        db.session.commit()
        return new_movie

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        return Movies.query.filter(Movies.title.ilike(f"%{title}%")).all()


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
