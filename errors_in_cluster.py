def get_identity(pic_name):
    return pic_name.split("_")[0]

def get_identities(cluster):
    identities = []
    for pic_name in cluster:
        identities.append(get_identity(pic_name))
    return identities

def get_unique_identities(identities):
    return list(dict.fromkeys(identities))

def get_error_rate(cluster):
    identities = get_identities(cluster)
    unique_identities = get_unique_identities(identities)

    count = []

    for identity in unique_identities:
        count.append(identities.count(identity))

    max_occurences = max(count)

    errors = len(identities) - max_occurences

    return (errors / len(identities)) * 100
