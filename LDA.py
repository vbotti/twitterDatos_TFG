from gensim.test.utils import common_texts
from gensim.corpora.dictionary import Dictionary
import logging
import gensim
import gensim.corpora as corpora
from pprint import pprint
from gensim.models import CoherenceModel
def lda(texto):
    # Create a corpus from a list of texts
    id2word = corpora.Dictionary(texto)
    texts = texto

    corpus = [id2word.doc2bow(text) for text in texts]

    lda_model = gensim.models.ldamodel.LdaModel(corpus = corpus,
                                                id2word=id2word,
                                                num_topics=10,
                                                iterations=100,
                                                random_state=200,
                                                update_every=1,
                                                chunksize=100,
                                                passes=10,
                                                alpha='auto',
                                                per_word_topics=True)
    pprint(lda_model.print_topics(num_words=20))
    doc_lda = lda_model[corpus]

    print('\nPerplexity: ', lda_model.log_perplexity(corpus))

    coherence_model_lda = CoherenceModel(model=lda_model, texts=texts, dictionary=id2word, coherence='c_v')
    coherence_lda = coherence_model_lda.get_coherence()
    print('\nCoherence Score: ', coherence_lda)