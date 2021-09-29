import pandas as pd
from matrix import getMatrices
import auc

def read_csv_from_args(path):
    return pd.read_csv(path, index_col=None, header=0)

def auc_for_one_participant(results):
    matrices = getMatrices(pd.DataFrame(results, None, results.columns))
    AUCs = {}

    for matrix in matrices:
        index = matrices[matrix][0]
        df = pd.DataFrame(matrices[matrix], index=index, columns=index)
        df.drop(labels=[None], axis=1, inplace=True)
        df.drop(labels=[None], axis=0, inplace=True)

        labels_dic = {}  # label is picture name
        for i in range(df.shape[0]):
            labels_dic[i] = df.columns[i]

        df = df.rename(labels_dic, axis='index')
        df = df.rename(labels_dic, axis='columns')

        AUCs[matrix] = auc.get_auc(df, labels_dic)

    return AUCs