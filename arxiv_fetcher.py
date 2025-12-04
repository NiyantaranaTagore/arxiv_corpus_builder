import arxiv
import time
from typing import List, Dict, Any

def fetch_papers(domain: str, max_results: int = 100) -> List[Dict[str, Any]]:
    """
    Fetches papers from ArXiv for a specific domain.

    Args:
        domain (str): The ArXiv category or keyword to search for.
        max_results (int): The maximum number of papers to fetch.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries, each representing a paper.
    """
    search = arxiv.Search(
        query=domain,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    papers_metadata = []
    for result in search.results():
        paper_data = {
            "arxiv_id": result.entry_id.split('/')[-1],
            "title": result.title,
            "abstract": result.summary.replace("\n", " "),
            "authors": [author.name for author in result.authors],
            "category": result.primary_category,
            "submitted_date": result.published.isoformat(),
            "pdf_url": result.pdf_url
        }
        papers_metadata.append(paper_data)
        time.sleep(3)  # Respect ArXiv API rate limits (1 request every 3 seconds)

    return papers_metadata

def fetch_single_paper(paper_id: str) -> Dict[str, Any]:
    """
    Fetches a single paper from ArXiv by its ID.

    Args:
        paper_id (str): The ArXiv ID of the paper.

    Returns:
        Dict[str, Any]: A dictionary representing the paper.
    """
    search = arxiv.Search(id_list=[paper_id])
    result = next(search.results())
    paper_data = {
        "arxiv_id": result.entry_id.split('/')[-1],
        "title": result.title,
        "abstract": result.summary.replace("\n", " "),
        "authors": [author.name for author in result.authors],
        "category": result.primary_category,
        "submitted_date": result.published.isoformat(),
        "pdf_url": result.pdf_url
    }
    return paper_data
