#Q1
import re
emails="""zuck26@facebook.com
page33@google.com
jeff42@amazon.com"""
print(re.findall(r'(\w+)@([A-Z 0-9]+)\.([A-Z]{2,4})',emails,flags=re.IGNORECASE))
#Extracting details mentioned above
#Here re.IGNORECASE makes data not case sensitive




#Q2
text="Betty bought a bit of butter,But the butter was so bitter,So she bought some better butter,To make the bitter butter better."
print(re.findall(r'\bB\w+',text,flags=re.IGNORECASE))


#Q3
sentence="A,very very;irregular_sentence"
output=" ".join(re.split('[;,\s_]+',sentence))
print(output)


#Q4
import re
tweet='''Good advice!RT @TheNextWeb:What I would do differently if I was learning to code today http://t.co/Ibwej0pxOd cc:@garybernhardt#rstats'''
tweet=re.sub('(http\S+\s*)|(RT|cc)|(#\S+)|(@\S+)','',tweet)
tweet=re.sub('[%s]'%re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '',tweet)
tweet=re.sub('\s+',' ',tweet)
print(tweet)
