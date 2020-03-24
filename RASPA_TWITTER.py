# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:46:36 2020
@author: Saraiva
"""
from twitterscraper import query_tweets
import datetime as dt
import pandas as pd

begin_date=dt.date(2020,3,22)
end_date=dt.date(2020,3,23)

limite=1000
lang="Portuguese"
palavra="damares"

#Efetuando a busca da palvra chave acima, no intervalo de dias acima
tweets=query_tweets(palavra, begindate=begin_date, enddate=end_date, limit=limite, lang=lang)

#Gerando o DataFrame
df=pd.DataFrame(t.__dict__ for t in tweets)

# Importando o módulo Scikit Learn
from sklearn.feature_extraction.text import CountVectorizer

# Usando o método CountVectorizer para criar uma matriz de documentos
cv = CountVectorizer()
count_matrix = cv.fit_transform(df.text)

# Contando o número de ocorrências das principais palavras em nosso dataset
word_count = pd.DataFrame(cv.get_feature_names(), columns=["word"])
word_count["count"] = count_matrix.sum(axis=0).tolist()[0]
word_count = word_count.sort_values("count", ascending=False).reset_index(drop=True)
word_count[:60]

#Imprimindo o resultado da contagem das 100 palavras que mais aparecem nos Twitters filtrados
print(word_count[:200])


from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
from datetime import datetime

stringtexto=""

#col=0
#for i in word_count[:300].word:
#   if len(i)>3:
 #       for j in range(word_count.at[col,'count']):
  #         stringtexto=stringtexto+" "+i
   # col=col+1
print('1')
summary = df.dropna(subset=['text'], axis=0)['text']
stringtexto =" ".join(s for s in summary)
        
print('2')      
print("stringtexto")
print(stringtexto) 
print('3')
# lista de stopword
stopwords = set(STOPWORDS)
stopwords.update([palavra,"tudo","sua","da", "meu", "em", "você", "de", "ao", "os", "com", "que", "https", "status", "para", "esse","pq","até","tá","só","vai","vou","ou","twitter","rt","bolsonaro"])
print('4')
print("# gerar uma wordcloud")
cloud = WordCloud(stopwords=stopwords,background_color="black",width=1600, height=800).generate(stringtexto)
print('5')
print("# mostrar a imagem final")
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(cloud, interpolation='bilinear')
ax.set_axis_off()
print('6')
plt.imshow(cloud);
now=datetime.now()
AGORA=str(now.second)
filename=AGORA+'damares.png'
cloud.to_file(filename)
    



#plt.imshow(cloud)
#plt.axis('off')
#plt.show()
#df.text