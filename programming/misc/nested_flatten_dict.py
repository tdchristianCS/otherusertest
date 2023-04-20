def flatten_dict(d: dict) -> dict:
    
    def _recurse(d: dict, chain: str) -> None:        
        for (key, val) in d.items():
            new_key = chain + key + '.'
            
            if type(val) == dict:
                _recurse(val, new_key)
            else:
                flat[new_key[:-1]] = val
                
    flat = {}
    _recurse(d, '')
    return flat

input_dictionary = {
    'a': 1,
    'b': {
        'A': 2,
    },
    'c': {
        'B': {
            'dd': 4
        }
    }
}

print(flatten_dict(input_dictionary))

