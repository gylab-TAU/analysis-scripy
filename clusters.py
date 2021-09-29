import overlappArea


def convert_string_to_number(string):
    if (type(string) != str):
        return string
    return int(string[1:-1])

def get_galleries(results):
    last_line = len(results) - 1
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
        new_line.append(convert_string_to_number(results.loc[index][4]))
        new_line.append(convert_string_to_number(results.loc[index][5]))
        name = results.loc[index][0]
        galleries[results.loc[index][0][1:len(name) - 1]].append(new_line)

    return galleries


def does_pic_belong_in_cluster(pic, cluster):
    for row in cluster:
        x1 = pic[1]
        y1 = pic[2]
        width1 = pic[3]
        height1 = pic[4]
        x2 = row[1]
        y2 = row[2]
        width2 = row[3]
        height2 = row[4]

        if overlappArea.getOverlappefArea(x1, y1, width1, height1, x2, y2, width2, height2) > 1:
            return True
    return False

def get_clusters(df):
    galleries = get_galleries(df)
    all_gallery_clusters = {}

    for gallery_name in galleries:
        clusters = []
        pretty_clusters = []

        for row in galleries[gallery_name]:
            if len(clusters) == 0:
                clusters.append([])
                pretty_clusters.append([])
                pretty_clusters[0].append(row[0])
                clusters[0].append(row)
            else:
                was_found = False

                for i in range (len(clusters)):
                    if does_pic_belong_in_cluster(row, clusters[i]):
                        clusters[i].append(row)
                        pretty_clusters[i].append(row[0])
                        was_found = True

                if was_found == False:
                    clusters.append([])
                    pretty_clusters.append([])
                    clusters[len(clusters) - 1].append(row)
                    pretty_clusters[len(clusters) - 1].append(row[0])
        all_gallery_clusters[gallery_name] = pretty_clusters
    return all_gallery_clusters