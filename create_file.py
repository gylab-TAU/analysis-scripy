import pandas as pd

def get_gallery_names(df):
    last_line = len(df) - 3
    gallery_names = []
    for name in df.iloc[:, 0][0:last_line - 1].drop_duplicates():
        gallery_names.append(name[1:len(name) - 1])
    return gallery_names

def get_max_num_of_clusters(data):
    max = 0
    for participant in data:
        for gallery_name in data[participant]["clusters"]:
            length = len(data[participant]["clusters"][gallery_name])

            if length > max:
                max = length
    return max

def get_line(participant_id, participant, gallery_name, max_clusters, gallery_index):
    line = [participant_id, gallery_name, participant["auc"][gallery_name] ,len(participant["clusters"][gallery_name])]

    errors = participant["errors"][gallery_name]

    for error in errors:
        line.append(error)

    for i in range (max_clusters - len(errors)):
        line.append("")
    return line

def get_headers(max_clusters):
    line = ["participant id", "gallery name", "AUC", "num of clusters"]

    for i in range(max_clusters):
        string = "Cluster " + str(i + 1) + " error %"

        line.append(string)
    return line

def get_array(data, df):
    max_clusters = get_max_num_of_clusters(data)
    result = []
    result.append(get_headers(max_clusters))
    galleries = get_gallery_names(df)

    for i in range(len(galleries)):
        for participant in data:
            result.append(get_line(participant, data[participant], galleries[i], max_clusters, i))

    pd.DataFrame(result).to_csv("results.csv", index=False, header=False)