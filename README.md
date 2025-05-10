# sentiment-analysis-using-NLP-in-python
Data collection:
Dataset collected from kaggle it contains train.txt,test.txt,val.txt three files.

Data handle:
Pandas to read the text files ,seperated by semicolon and set the names of columns by Text,Labels.

Data cleaning:
Regex match the patterns ,then text to lower,remove non alphabet character.NLTK this toolkit to remove stopwords.
cleaned text data stored in new column.

 Encoding:
 Labels to be encoding using Label encoder it assign 0-Anger,1-Fear,2-Joy,3-Love,4-Sadness,5-Surprise
 
Training:
Text Features extraction using Tfidfvectorizer.
Using logistic and Multinomial naive bayes algorithms to train a model.This two algorithmns text data handle it well.
Store trained model and tokens in pickle file.

Tools:
Python,
JupyterNotebook,
NLTK,
Streamlit.
Unicodes for emojis.

Result:
Logistic regression achieved  : validation accuracy- 92.0%
                                 Test accuracy- 91.55%
                                 
feedbacks save in the csv file.

User interface:
Streamlit web ui for user friendly like real world ai chatbots responses instead of labels.

![ui_sentiment](https://github.com/user-attachments/assets/a17a102d-b6a1-4b3b-88e8-283c73a8b031)

Responses:
![reply3](https://github.com/user-attachments/assets/56636c17-5d36-45a8-aa31-65918cd5d604)




                                 
                                 

                                 


