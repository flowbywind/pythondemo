class Sample:
    def __init__(self,text):
        self.text="this text"
    def __enter__(self):
        print("In __enter__()")
        return self

    def __exit__(self, type, value, trace):
        print("In __exit__()")


    def getsum(self):
        print("this is sum")


def get_sample():
    return Sample("dd")


with get_sample() as sample:
    print("sample:", sample.getsum())
