from sklearn.metrics import auc
import numpy as np

def find_false_positive_and_true_positive_rates(df, labels, threshold):
    """
    calculates the precentages of FP (false positive) and FN (false negative)

    :param df = the data frame
    :param labels = a dic with key=index, value=picture name
    :param threshold = the current threshold for deciding if it is fp or fn

    :return: the precentage of tp (true positive), fp (false positive),
             tn (true negative), fn (false negative),
             total (how many thresholds were checked)
    """

    count_true_positive = 0
    count_false_positive = 0
    count_true_negative = 0
    count_false_negative = 0
    count_total = 0

    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            count_total += 1
            dist = df.iloc[i, j]
            name1 = labels[i][:2]
            name2 = labels[j][:2]

            if name1 != name2:
                if dist <= threshold:
                    count_false_positive += 1
                else:
                    count_true_negative += 1
            if name1 == name2:
                if dist > threshold:
                    count_false_negative += 1
                else:
                    count_true_positive += 1

    return count_true_positive / count_total, count_false_positive / count_total, \
           count_true_negative / count_total, count_false_negative / count_total, \
           count_total

def get_auc(df, labels):
    thresholds = []
    max_dist = df.max().max()
    min_dist = df.min().min()
    thresholds = [threshold for threshold in np.linspace(min_dist, max_dist, num=100)]

    true_positives, false_positives, true_negatives, false_negatives, sums = [], [], [], [], []
    true_positive_rate, false_positive_rate = [], []
    for threshold in thresholds:
        tp, fp, tn, fn, total = find_false_positive_and_true_positive_rates(df, labels, threshold)
        true_positives.append(tp)
        false_positives.append(fp)
        true_negatives.append(tn)
        false_negatives.append(fn)
        true_positive_rate.append(tp / (tp + fn))
        false_positive_rate.append(fp / (tn + fp))
        sums.append(fp + fn)  # sum false

    return auc(false_positive_rate, true_positive_rate)

