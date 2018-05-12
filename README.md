flask restful analyzer based on a naive bayesian classifier trained on positive/negative movie reviews

# Usage
run rest_router.py and wait for the classifier to load the dataset and finish training

send get requests to localhost:5000/Analyze with the sentence you want to analyze

# Dependencies
flask
nltk
flask_restful

