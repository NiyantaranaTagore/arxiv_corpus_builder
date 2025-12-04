import argparse
from arxiv_fetcher import fetch_papers, fetch_single_paper
from corpus_manager import load_corpus, save_corpus, append_to_corpus
from similarity_checker import check_similarity

CORPUS_FILE = "corpus.json"

def main():
    parser = argparse.ArgumentParser(description="ArXiv Domain Corpus Builder and Similarity Checker")
    parser.add_argument("--domain", type=str, help="ArXiv category or keyword domain (e.g., cs.CL).")
    parser.add_argument("--build-corpus", action="store_true", help="Build the initial corpus for the specified domain.")
    parser.add_argument("--query-title", type=str, help="The title of the paper to check.")
    parser.add_argument("--query-abstract", type=str, help="The abstract of the paper to check.")
    parser.add_argument("--max-results", type=int, default=100, help="Maximum number of papers to fetch for the corpus.")
    parser.add_argument("--threshold", type=float, default=0.85, help="Similarity threshold to consider a paper as existing.")

    args = parser.parse_args()

    if args.build_corpus and args.domain:
        print(f"Building corpus for domain: {args.domain}...")
        papers = fetch_papers(args.domain, args.max_results)
        save_corpus(CORPUS_FILE, papers)
        print(f"Corpus with {len(papers)} papers has been built and saved to {CORPUS_FILE}")

    elif args.query_title and args.query_abstract:
        print("Loading corpus...")
        corpus = load_corpus(CORPUS_FILE)
        print(f"Corpus loaded with {len(corpus)} papers.")

        print("Checking for similar papers...")
        exists, similar_papers = check_similarity(args.query_title, args.query_abstract, corpus, args.threshold)

        if exists:
            print("\nA similar paper likely already exists in the corpus.")
            print("Top 5 most similar papers:")
            for item in similar_papers:
                print(f"  - Title: {item['paper']['title']}")
                print(f"    ArXiv ID: {item['paper']['arxiv_id']}")
                print(f"    Similarity Score: {item['similarity_score']:.4f}\n")
        else:
            print("\nThis appears to be a new paper.")
            # In a real application, you might try to find the paper on ArXiv
            # based on the title to get its full metadata.
            # For this example, we'll just add the provided info.
            print("Fetching paper from ArXiv to add to the corpus...")
            # This is a simplified approach. A more robust solution would
            # search ArXiv for the title to get the correct ID.
            # For now, we'll simulate finding it.
            # In a real scenario, you would need a more sophisticated way to find the paper's ArXiv ID.
            # For demonstration, we will assume the user provides a valid ArXiv ID or we can search for it.
            # As a placeholder, we are not adding it to the corpus in this example.
            print("Functionality to fetch and add a new paper based on title/abstract is a future enhancement.")


if __name__ == "__main__":
    main()
