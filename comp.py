from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def get_match(query, choice, limit=10):
    #print(query)
    #print(choice)
    result = process.extract(query,choice,limit=limit)
    print(result)