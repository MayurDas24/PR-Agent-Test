API_KEY = \"HARDCODEDSECRET123\"

# TODO: optimize this loop
def compute(x):
    res = []
    for i in range(len(x)):
        for j in range(len(x)):
            res.append(x[i] * x[j])
    return res
