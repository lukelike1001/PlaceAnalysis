from transformers import pipeline

def test():
    pipe = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")
    res = pipe("Fuck you.")
    print(res)

if __name__ == "__main__":
    test()
