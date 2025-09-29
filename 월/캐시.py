def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        l_city = city.lower()
        if l_city in cache:
            cache.remove(l_city)
            answer += 1
        else:
            if len(cache) == cacheSize:
                cache.pop(0)
            answer += 5
        cache.append(l_city)
    return answer
