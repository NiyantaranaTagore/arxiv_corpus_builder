<<<<<<< HEAD
# ArXiv Domain Corpus Builder + Similarity Checker

This project provides a command-line tool to build a domain-specific corpus of research papers from ArXiv and check whether a new paper already exists in the corpus using semantic similarity.

## Features

- **Build a Domain-Specific Corpus**: Fetch papers from a specified ArXiv category (e.g., `cs.CL`, `quant-ph`) or by a keyword.
- **Store Metadata**: For each paper, it collects the title, abstract, authors, category, submission date, ArXiv ID, and PDF URL, and stores them in a structured `corpus.json` file.
- **Similarity Checking**: Given a new paper's title and abstract, it checks for its existence within the corpus.
- **Similarity Scoring**: It uses sentence embeddings (via `sentence-transformers`) and cosine similarity to compute a score between the query paper and each paper in the corpus.
- **Top Matches**: Returns the top 5 most similar papers from the corpus, along with their similarity scores.
- **Extensible**: Automatically appends new, non-existing papers to the corpus to keep it updated.

## Project Structure

```
arxiv_corpus_builder/
├── main.py                # CLI entry point
├── arxiv_fetcher.py       # Handles fetching data from the ArXiv API
├── similarity_checker.py  # Computes similarity scores
├── corpus_manager.py      # Manages reading/writing the JSON corpus
├── requirements.txt       # Project dependencies
└── corpus.json            # The stored corpus of paper metadata
```

## Setup and Installation

1.  **Clone the repository (or set up the files as described above).**

2.  **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

The tool is operated via the command line from the project's root directory.

### 1. Build a Corpus

First, you need to build a local corpus of papers for a specific domain. Use the `--build-corpus` and `--domain` flags. You can also specify the number of papers to fetch with `--max-results`.

**Example:** Fetch the 50 most recent papers from the "Computer Science - Computation and Language" (`cs.CL`) category.

```bash
python main.py --build-corpus --domain "cs.CL" --max-results 50
```

This command will:
- Fetch 50 papers from ArXiv.
- Create a `corpus.json` file with their metadata.
- Respect ArXiv's API rate limits by waiting between requests.

### 2. Query for a Paper

Once the corpus is built, you can check if a paper exists using its title and abstract with the `--query-title` and `--query-abstract` flags.

**Example:** Check for a paper that is likely to exist in the corpus.

```bash
python main.py \
    --query-title "A BERT-based Approach for Sentiment Analysis" \
    --query-abstract "We propose a novel method for sentiment analysis using a fine-tuned BERT model. Our experiments show state-of-the-art results on several benchmark datasets."
```

#### Output for an Existing Paper

If a similar paper is found above the similarity threshold (default is 0.85), the output will look like this:

```
A similar paper likely already exists in the corpus.
Top 5 most similar papers:
  - Title: A BERT-based Approach for Sentiment Analysis
    ArXiv ID: 2105.12345
    Similarity Score: 0.9876

  - Title: Sentiment Classification with Deep Learning
    ArXiv ID: 2011.05678
    Similarity Score: 0.8912

...
```

#### Output for a New Paper

If no paper in the corpus meets the similarity threshold, it is marked as new.

```
This appears to be a new paper.
Fetching paper from ArXiv to add to the corpus...
Functionality to fetch and add a new paper based on title/abstract is a future enhancement.
```

## How It Works

1.  **`arxiv_fetcher.py`**: Uses the `arxiv` library to search for and download paper metadata. It includes a delay to comply with ArXiv's API usage policy.
2.  **`corpus_manager.py`**: Handles all file I/O for `corpus.json`, including loading the existing corpus, saving it, and appending new entries.
3.  **`similarity_checker.py`**:
    - Uses the `sentence-transformers` library (with the `all-MiniLM-L6-v2` model) to convert titles and abstracts into high-dimensional vector embeddings.
    - Computes the `cosine_similarity` between the query paper's embeddings and the embeddings of all papers in the corpus.
    - A weighted average of title and abstract similarity is used to produce a final score.
4.  **`main.py`**: Parses command-line arguments using `argparse` to orchestrate the workflow, calling the other modules to perform the requested actions.

## Future Enhancements

- **Improved New Paper Integration**: Implement a more robust mechanism to find a new paper's full metadata on ArXiv using its title before adding it to the corpus.
- **Different Similarity Metrics**: Allow the use of other similarity algorithms like Levenshtein distance for titles or other embedding models.
- **Web Interface**: Build a simple web UI (e.g., using Flask or Streamlit) on top of the core logic.
- **Batch Processing**: Add functionality to check a list of new papers from a file.

conda create --name arxiv python=python=3.10
=======
# arxiv_corpus_builder
This project provides a command-line tool to build a domain-specific corpus of research papers from ArXiv and check whether a new paper already exists in the corpus using semantic similarity.
>>>>>>> e19306ba5ea0a41bfedf74aa903b376949276865
