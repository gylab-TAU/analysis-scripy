import argparse
import pandas as pd
import os
from auc_for_one_participant import auc_for_one_participant
import errors_in_cluster
import create_file
import clusters as c

def read_dir_from_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('Path', metavar='path', type=str, help= 'the path to the csv directory')
    args = parser.parse_args()

    return args.Path

def read_csv_from_args(path):
    return pd.read_csv(path, index_col=None, header=0)

def get_participant_id(df):
    return df.iloc[-1, 3]

def get_last_line_of_coordinates(df):
    arr = df.values

    for i in range (len(arr)):
        row = arr[i]
        if row[0] == "id" or row[0] == '"id"' or "age" in row[0]:
            return i
    return -1

if __name__ == '__main__':
    path = read_dir_from_args()

    files = os.listdir(path)

    data = {}

    for file in files:
        file_path = os.path.join(path, file)
        df = read_csv_from_args(file_path)

        full_df = df
        df = df.iloc[0: get_last_line_of_coordinates(df)]

        clusters = c.get_clusters(df)

        error_rates = {}
        for gallery_name in clusters:
            gallery = clusters[gallery_name]
            gallery_errors = []
            for cluster in gallery:
                gallery_errors.append(errors_in_cluster.get_error_rate(cluster))

            error_rates[gallery_name] = gallery_errors

        data[get_participant_id(full_df)] = { "auc": auc_for_one_participant(df), "clusters": clusters, "errors": error_rates }

    create_file.get_array(data, df)