def fibonacci(n, cache={0: 1, 1: 1}) -> int:
    
    if n in cache:
       return cache[n]
    
    result = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    cache[n] = result
    
    return result


def inverse(str) -> list:
    str_ = list(str)
    
    if len(str_) == 1:
        return str_
    
    return inverse(str_[1:]) + [str_[0]]


def hanoi_movements(n, cache={1:1}) -> int:
    if n in cache:
        return cache[n]

    result = (2 * hanoi_movements(n - 1)) + 1
    cache[n] = result

    return result

