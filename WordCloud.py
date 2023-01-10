from wordcloud import WordCloud, STOPWORDS
import wikipedia
from PIL import Image

stop_w= set(STOPWORDS)
info= wikipedia.summary("Python")
word_cloud=WordCloud(stopwords=stop_w).generate(info)
img = word_cloud.to_image()
img.show()