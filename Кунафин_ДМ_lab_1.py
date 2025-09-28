def simple_probability(m, n):
    if n == 0:
        return 0.0
    return m / n

def logical_or(m, k, n):
    return (m + k) / n

def logical_and(m, k, n, l):
    return (m / n) * (k / l)

def expected_value(values, probabilities):
    return sum(v * p for v, p in zip(values, probabilities))

def conditional_probability(values):
    count_a_and_b = 0
    count_a = 0
    
    for a, b in values:
        if a == 1:
            count_a += 1
            if b == 1:
                count_a_and_b += 1
    
    if count_a == 0:
        return 0.0
    
    return count_a_and_b / count_a

def bayesian_probability(a, b, ba):
    if b == 0:
        return 0.0
    return (ba * a) / b
