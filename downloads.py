import nltk
import ir_datasets

nltk.download("stopwords")
nltk.download("punkt")
nltk.download("wordnet")
nltk.download("omw-1.4")

cranfield = ir_datasets.load("cranfield")
next(cranfield.docs_iter())

vaswani = ir_datasets.load("vaswani")
next(vaswani.docs_iter())
