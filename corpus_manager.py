import json
from typing import List, Dict, Any

def load_corpus(filepath: str) -> List[Dict[str, Any]]:
    """
    Loads the corpus from a JSON file.

    Args:
        filepath (str): The path to the corpus JSON file.

    Returns:
        List[Dict[str, Any]]: The loaded corpus.
    """
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_corpus(filepath: str, corpus: List[Dict[str, Any]]) -> None:
    """
    Saves the corpus to a JSON file.

    Args:
        filepath (str): The path to the corpus JSON file.
        corpus (List[Dict[str, Any]]): The corpus to save.
    """
    with open(filepath, 'w') as f:
        json.dump(corpus, f, indent=4)

def append_to_corpus(filepath: str, paper: Dict[str, Any]) -> None:
    """
    Appends a new paper to the corpus.

    Args:
        filepath (str): The path to the corpus JSON file.
        paper (Dict[str, Any]): The paper to append.
    """
    corpus = load_corpus(filepath)
    corpus.append(paper)
    save_corpus(filepath, corpus)
