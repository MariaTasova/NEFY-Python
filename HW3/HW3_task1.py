def lru_cache(func):
    cache = dict()

    def lru_cache(*args, **kwargs):
        if args in cache:
            print('from cache', cache[args])
        result = func(*args, **kwargs)
        cache[args] = result
        return result
    return lru_cache

@lru_cache
def product(*nums, scale = 2):
    p = scale
    for n in nums:
        p *= n
    return p

print(product(3, 5, scale=10))
print(product(3, 5, scale=1))
print(product(3, 5, scale=2))
