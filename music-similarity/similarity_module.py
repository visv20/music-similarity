import math
# https://dataconomy.com/2015/04/implementing-the-five-most-popular-similarity-measures-in-python/
def cosine_similarity(data, id1, id2):
    def square_rooted(x):
        return round(math.sqrt(sum([a*a for a in x])),3)
    def compute(v1, v2):
        numerator = sum(a*b for a,b in zip(v1,v2))
        denominator = square_rooted(v1)*square_rooted(v2)
        return round(numerator/float(denominator),3)
    d1 = [v for v in data[id1].values() if type(v) in [int,float]]
    d2 = [v for v in data[id2].values() if type(v) in [int,float]]
    return compute(d1, d2)

def euclidean_similarity(data, id1, id2):
    def compute(v1, v2):
        return math.sqrt(sum(pow(a-b,2) for a, b in zip(v1, v2)))
    d1 = [v for v in data[id1].values() if type(v) in [int,float]]
    d2 = [v for v in data[id2].values() if type(v) in [int,float]]
    return compute(d1, d2)

def jaccard_similarity(data, id1, id2): 
    def compute(v1, v2):
        intersection_cardinality = len(set.intersection(*[set(v1), set(v2)]))
        union_cardinality = len(set.union(*[set(v1), set(v2)]))
        return intersection_cardinality/float(union_cardinality)
    d1 = [v for v in data[id1].values() if type(v) in [int,float]]
    d2 = [v for v in data[id2].values() if type(v) in [int,float]]
    return compute(d1, d2)

def manhattan_similarity(data, id1, id2):
    def compute(v1, v2):
        return sum(abs(a-b) for a,b in zip(v1,v2))
    d1 = [v for v in data[id1].values() if type(v) in [int,float]]
    d2 = [v for v in data[id2].values() if type(v) in [int,float]]
    return compute(d1, d2)

def pearson_similarity(data, id1, id2):
    def compute(v1, v2):
        x_mean = statistics.mean(v1)
        y_mean = statistics.mean(v2)
        numerator = sum([(x-x_mean)*(y-y_mean) for x,y in zip(v1,v2)])
        denominator = math.sqrt(sum([pow(x-x_mean,2) for x in v1])) * math.sqrt(sum([pow(y-y_mean,2)for y in v2]))
        return numerator/denominator
    d1 = [v for v in data[id1].values() if type(v) in [int,float]]
    d2 = [v for v in data[id2].values() if type(v) in [int,float]]
    return compute(d1, d2)

def compute_similarity(similarity_func, data, id1, id2):
    return similarity_func(data, id1, id2)
