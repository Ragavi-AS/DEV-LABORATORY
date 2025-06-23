
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns


df = pd.read_csv("C:\\Users\\Ragavi\\Documents\\DEV Lab\\spam (1).csv", encoding='latin-1')[['v1', 'v2']]
df.columns = ['label', 'message']

print(df.head())
print(df.info())


print("Missing values:\n", df.isnull().sum())


print("Class count:\n", df['label'].value_counts())
df['label'].value_counts().plot(kind='bar', title='Spam vs Ham')
plt.show()


df['length'] = df['message'].apply(len)
df['length'].plot.hist(bins=50, title='Message Length Histogram')
plt.xlabel('Message Length')
plt.show()


spam_words = ' '.join(df[df['label']=='spam']['message'])
ham_words = ' '.join(df[df['label']=='ham']['message'])

spam_wc = WordCloud(background_color='black').generate(spam_words)
ham_wc = WordCloud(background_color='white').generate(ham_words)

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(spam_wc, interpolation='bilinear')
plt.axis('off')
plt.title("Spam WordCloud")

plt.subplot(1,2,2)
plt.imshow(ham_wc, interpolation='bilinear')
plt.axis('off')
plt.title("Ham WordCloud")
plt.show()


print("Average message length for HAM:", df[df['label']=='ham']['length'].mean())
print("Average message length for SPAM:", df[df['label']=='spam']['length'].mean())
