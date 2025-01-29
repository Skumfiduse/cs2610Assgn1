from request import Request

def myParser(dataBits):
    data = dataBits.decode('UTF-8')
    parts = dataBits.split("\n")
