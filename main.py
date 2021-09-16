import argparse
import pandas as pd
import os
from auc_for_one_participant import auc_for_one_participant
import xmeans
import errors_in_cluster
import create_file

def read_dir_from_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('Path', metavar='path', type=str, help= 'the path to the csv directory')
    args = parser.parse_args()

    return args.Path

def read_csv_from_args(path):
    return pd.read_csv(path, index_col=None, header=0)

def get_participant_id(df):
    print(df)
    return df.iloc[-1, 3]

if __name__ == '__main__':
    path = read_dir_from_args()

    files = os.listdir(path)

    data = {}

    for file in files:
        file_path = os.path.join(path, file)
        df = read_csv_from_args(file_path)

        clusters = xmeans.getClusters(df)
        error_rates = []
        for gallery in clusters:
            gallery_errors = []
            for cluster in gallery:
                gallery_errors.append(errors_in_cluster.get_error_rate(cluster))

            error_rates.append(gallery_errors)

        data[get_participant_id(df)] = { "auc": auc_for_one_participant(df), "clusters": clusters, "errors": error_rates }

    create_file.get_array(data, df)