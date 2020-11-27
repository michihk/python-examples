# Import packages
import matplotlib.pyplot as plt 
from wordcloud import WordCloud, STOPWORDS# Generate word cloud

text = "Eins Zwei Drei View Fuenf"

wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='salmon', colormap='Pastel1', collocations=False, stopwords = STOPWORDS).generate(text)# Plot

plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off");
plt.tight_layout(pad = 0) 
plt.show()

