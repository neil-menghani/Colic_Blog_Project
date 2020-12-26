# Colic_Blog_Project

### Neil Menghani, Columbia University

## Source files

scrape.py: Scrapes blog posts from the Colic Support Forum, http://colicsupport.proboards.com/
docs.txt: The raw documents (posts) after the web scraping
clean.py: Cleans the document by eliminating stop words, numbers, and names
male.txt, female.txt: list of names that should be removed from the documents
cleaned.txt: The cleaned documents
dict.txt: A dictionary of words to cross-check that each word in the corpus is a real word
perplexity.py, coherence.py: Builds LDA topic models and outputs perplexity and coherence for various values of k
lda_topics.py: Builds LDA topic model for a given value of k and saves matrix of topic distributions as well as matrix of document weights to numpy array file
relevant.py: Using saved matrices, determines documents in the corpus relevant to a given query
topicsX.txt: List of top 50 words for each topic for model with X number of topics
topics_X.npy: Matrix of topic distributions of words in the dictionary
weights_X.npy: Document weights over topics
best_k.xlsx: Plots of perplexity and coherence in Excel
requirements.txt: "conda install --file requirements.txt" from a Python 3 conda environment