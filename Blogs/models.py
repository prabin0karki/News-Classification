import time
import datetime
from django.db import models
from django.utils.text import slugify
#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
import re
import pandas as pd
from textblob import Word
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from  django.contrib.auth.models import User
# folders = ["business","entertainment","politics","sport","tech"]
# Create your models here.
def clean_str(string):
	string = re.sub(r"\'s", "", string)
	string = re.sub(r"\'ve", "", string)
	string = re.sub(r"n\'t", "", string)
	string = re.sub(r"\'re", "", string)
	string = re.sub(r"\'d", "", string)
	string = re.sub(r"\'ll", "", string)
	string = re.sub(r",", "", string)
	string = re.sub(r"!", " ! ", string)
	string = re.sub(r"\(", "", string)
	string = re.sub(r"\)", "", string)
	string = re.sub(r"\?", "", string)
	string = re.sub(r"'", "", string)
	string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
	string = re.sub(r"[0-9]\w+|[0-9]","", string)
	string = re.sub(r"\s{2,}", " ", string)
	return string.strip().lower()	
data = pd.read_csv('po/dataset.csv')
x = data['news'].tolist()
y = data['type'].tolist()
for index,value in enumerate(x):
	x[index] = ' '.join([Word(word).lemmatize() for word in clean_str(value).split()])
vect = TfidfVectorizer(stop_words='english',min_df=2)
X = vect.fit_transform(x)
Y = np.array(y)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20, random_state=42)
clf = MultinomialNB().fit(X_train, y_train)
def check_news_type(news_article):
	news_article = [' '.join([Word(word).lemmatize() for word in clean_str(news_article).split()])]
	features = vect.transform(news_article)
	a = str(clf.predict(features)[0])
	return a

# Create your models here.
class Post(models.Model):
	Article_title=models.CharField(max_length=1000,blank=False,null=True)
	Article_Short_Descriptions=models.TextField(blank=False,null=True)
	Article_Content=RichTextUploadingField(blank=False,null=True)
	# Image = models.ImageField(upload_to='mypics/%Y/%m/%d',null=True,blank=True)
	publish_date = models.DateTimeField(editable=False)
	publish_by=models.CharField(max_length=250)
	Category=models.CharField(max_length=250,editable=False)

	def save(self):
		article=self.Article_Content
		print(article)
		if not self.id:
			self.publish_date = datetime.date.today()
			self.Category= check_news_type(article)
		super(Post, self).save()

	def __str__(self):
		return self.Article_Content
	def __unicode__(self):
		return self.Article_Content












