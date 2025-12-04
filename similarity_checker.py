from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from typing import List, Dict, Any, Tuple

# Load a pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embeddings(text: str) -> np.ndarray:
    """
    Generates embeddings for a given text.

    Args:
        text (str): The text to embed.

    Returns:
        np.ndarray: The embedding vector.
    """
    return model.encode(text, convert_to_tensor=False).reshape(1, -1)

def check_similarity(
    query_title: str,
    query_abstract: str,
    corpus: List[Dict[str, Any]],
    threshold: float = 0.85
) -> Tuple[bool, List[Dict[str, Any]]]:
    """
    Checks the similarity of a query paper against the corpus.

    Args:
        query_title (str): The title of the query paper.
        query_abstract (str): The abstract of the query paper.
        corpus (List[Dict[str, Any]]): The existing corpus of papers.
        threshold (float): The similarity threshold to consider a paper as existing.

    Returns:
        Tuple[bool, List[Dict[str, Any]]]: A tuple containing a boolean indicating if the
                                           paper exists and a list of the top 5 similar papers.
    """
    if not corpus:
        return False, []

    query_title_embedding = get_embeddings(query_title)
    query_abstract_embedding = get_embeddings(query_abstract)

    corpus_titles = [paper['title'] for paper in corpus]
    corpus_abstracts = [paper['abstract'] for paper in corpus]

    corpus_title_embeddings = model.encode(corpus_titles, convert_to_tensor=False)
    corpus_abstract_embeddings = model.encode(corpus_abstracts, convert_to_tensor=False)

    title_similarities = cosine_similarity(query_title_embedding, corpus_title_embeddings)[0]
    abstract_similarities = cosine_similarity(query_abstract_embedding, corpus_abstract_embeddings)[0]

    # Combine similarities (e.g., with weighting)
    combined_similarities = 0.4 * title_similarities + 0.6 * abstract_similarities

    similar_papers = []
    for i, score in enumerate(combined_similarities):
        similar_papers.append({
            "paper": corpus[i],
            "similarity_score": float(score)
        })

    # Sort by similarity score in descending order
    similar_papers.sort(key=lambda x: x['similarity_score'], reverse=True)

    top_5_similar = similar_papers[:5]

    paper_exists = any(p['similarity_score'] >= threshold for p in top_5_similar)

    return paper_exists, top_5_similar
