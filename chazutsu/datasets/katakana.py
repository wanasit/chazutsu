import os
import csv
import random
from chazutsu.datasets.framework.dataset import Dataset
from chazutsu.datasets.framework.resource import Resource


class Katakana(Dataset):

    def __init__(self):
        super().__init__(
            name="Katakana",
            site_url="https://github.com/wanasit/katakana/tree/master/dataset",
            download_url="https://raw.githubusercontent.com/wanasit/katakana/master/dataset/data.csv",
            description="English-Katakana names dataset aggregated from Wikipedia's article titles."
        )

    def make_and_split_samples(self, original_file_path, shuffle, test_size, sample_count):

        with open(original_file_path) as original_file:
            reader = csv.reader(original_file)
            _ = next(reader, None) # pop header
            rows = [row for row in reader]

        base, ext = os.path.splitext(original_file_path)

        sample_path = base + "_samples" + ext
        train_sample_path = base + "_train" + ext
        test_sample_path = base + "_test" + ext

        if sample_count == 0:
            sample_count = len(rows)

        indexes = [i for i in range(sample_count)]
        if shuffle:
            random.shuffle(indexes)

        with open(sample_path, "w") as sample_file:
            writer = csv.writer(sample_file, delimiter="\t", )
            for i in indexes:
                writer.writerow(rows[i])

        test_count = int(round(sample_count * test_size))
        if shuffle:
            random.shuffle(indexes)
            test_indexes = indexes[:test_count]
            train_indexes = indexes[test_count:]
        else:
            random.shuffle(indexes)
            test_indexes = sorted(indexes[test_count:])
            train_indexes = sorted(indexes[:test_count])

        with open(train_sample_path, "w") as train_file:
            writer = csv.writer(train_file, delimiter="\t", )
            for i in train_indexes:
                writer.writerow(rows[i])

        with open(test_sample_path, "w") as test_file:
            writer = csv.writer(test_file, delimiter="\t")
            for i in test_indexes:
                writer.writerow(rows[i])


    def get_extracted_path(self, dataset_file_path):
        return dataset_file_path

    def make_resource(self, data_root):
        return Resource(data_root, columns=['english', 'katakana'])

    def trush(self, path):
        pass

    def clear_trush(self):
        pass
