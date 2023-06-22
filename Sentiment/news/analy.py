import json
from NewsSentiment import TargetSentimentClassifier
import transformers
tsc = TargetSentimentClassifier()
sentiment_pipeline = transformers.pipeline("sentiment-analysis")

#  Approch 1: NewsMTSC
#  Approch 2: Transformers
#  Approch 3: Planned LSTM
#
#
#

def get_sentiment(keyword):
    op = {
        "transformer": None,
        "mtsc": None
    }
    with open(keyword+".json") as f:
        jo = json.loads(f.read())
        
    # ent = "adani enterprise"
    ent = keyword
    data_cons = {
        "negative": [],
        "positive": [],
        "neutral": []
    }
    # ent= "hindalco"
    j = 0
    desc_data= []
    for i in jo["articles"]:
        try:
            sent = tsc.infer_from_text(i["description"],ent,".")[0]
        except:
            continue
        print(sent)
        data_cons[sent["class_label"]].append(sent["class_prob"])
        
        desc_data.append(i["description"])
        j += 1

    sen_data = sentiment_pipeline(desc_data)

    with open(f"{ent}.res","w") as f:
        f.write(json.dumps(data_cons))
        
    print("pos", len(data_cons["positive"]))
    print("neg", len(data_cons["negative"]))
    print("neu", len(data_cons["neutral"]))
    op["mtsc"] = data_cons

    pos,neg = 0,0
    for i in sen_data:
        if i["label"] == "POSITIVE":
            pos += 1
        if i["label"] == "NEGATIVE":
            neg += 1
    op["transformer"] = {"pos": pos, "neg": neg}
    print("neg", neg)
    print("pos", pos)
    return op