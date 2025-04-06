# save_model.py

from sentence_transformers import SentenceTransformer

# Download the model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Save locally to a folder called 'local_model'
model.save('./local_model')
