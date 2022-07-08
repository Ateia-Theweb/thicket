def flat(seq_of_seqs):
    flatnd = []

    for seq in seq_of_seqs:
        flatnd.extend(seq)

    return flatnd


def retrie5(f, *a, **kw):
    try:
        return f(*a, **kw)
    except TimeoutError:
        try:
            return f(*a, **kw)
        except TimeoutError:
            try:
                return f(*a, **kw)
            except TimeoutError:
                try:
                    return f(*a, **kw)
                except TimeoutError:
                    return f(*a, **kw)
