# Movie Recommender Flask App

This is a simple movie recommendation system built using Flask and the Surprise library (SVD model). It uses the MovieLens 100k dataset.

## Features

- Loads the MovieLens 100k dataset
- Trains an SVD recommendation model
- Exposes a `/recommend/<user_id>` route that returns predicted ratings for a movie

## Requirements

- Python 3.11
- Flask
- scikit-surprise

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/movie_recommender.git
    ```

2. Navigate to the project directory:
    ```bash
    cd movie_recommender
    ```

3. Set up a virtual environment:
    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
    - On MacOS/Linux:
        ```bash
        source venv/bin/activate
        ```
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```

5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Run the Flask app:
    ```bash
    python app.py
    ```

7. Open a web browser and go to `http://127.0.0.1:5000/recommend/<user_id>`.
