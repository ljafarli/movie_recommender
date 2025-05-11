# Importing necessary libraries
from flask import Flask, jsonify
from surprise import SVD
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import train_test_split

# Initialize the Flask app
app = Flask(__name__)

# Load the MovieLens 100k dataset (you can change this based on your dataset)
ratings = Dataset.load_builtin('ml-100k')  # This loads the built-in MovieLens dataset

# Build the training set
trainset = ratings.build_full_trainset()

# Initialize and train the model (using Singular Value Decomposition)
model = SVD()
model.fit(trainset)

# Define the route for movie recommendations
@app.route('/recommend/<user_id>', methods=['GET'])
def recommend(user_id):
    try:
        # Here, we're predicting the rating of a movie for the given user
        movie_id = 2  # For example, movie ID 1 (can be dynamic)
        prediction = model.predict(user_id, movie_id)
        return jsonify({
            'user_id': user_id,
            'movie_id': movie_id,
            'predicted_rating': prediction.est
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'message': 'An error occurred while making the prediction.'
        }), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
