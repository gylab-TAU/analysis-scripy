from pyclustering.cluster.xmeans import xmeans

def get_clusters(coordinates):
    xmeans_instance = xmeans(coordinates)
    xmeans_instance.process()

    clusters = xmeans_instance.get_clusters()

    return clusters

def map_cluster(cluster, df, cluster_name):
    results = []

    for index in cluster:
        row = df[index]
        results.append(row[0])

    return results

def convert_string_to_number(string):
    return int(string[1:-1])

def getClusters(results):
    last_line = len(results) - 3
    gallery_names = []
    for name in results.iloc[:, 0][0:last_line - 1].drop_duplicates():
        gallery_names.append(name[1:len(name) - 1])

    galleries = {}

    for gallery_name in gallery_names:
        galleries[gallery_name] = []

    for index in range(0, last_line):
        new_line = []
        new_line.append(results.loc[index][1].replace("\"", ""))
        new_line.append(convert_string_to_number(results.loc[index][2]))
        new_line.append(convert_string_to_number(results.loc[index][3]))
        name = results.loc[index][0]
        galleries[results.loc[index][0][1:len(name) - 1]].append(new_line)

    mapped_clusters = []

    for gallery in galleries:
        df = galleries[gallery]
        data = []


        for i in range(0, len(df) - 1):
            row = df[i]
            x = row[1]
            y = row[2]
            line = [x, y]

            data.append(line)
            
        clusters = get_clusters(data)

        mapped_gallery = []
        for cluster_index in range(len(clusters)):
            temp = map_cluster(clusters[cluster_index], df, str(cluster_index + 1))
            mapped_gallery.append(temp)

        mapped_clusters.append(mapped_gallery)

    return mapped_clusters
