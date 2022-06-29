import csv
import random

def load_urls_from_csv(csv_path):
    with open(csv_path, 'r') as file:
        result = [row[0] for row in csv.reader(file)]
        return result

def save_to_txt(benign_urls, malware_urls, output_path):
    begine_count = len(benign_urls)
    malware_count = len(malware_urls)
    max_count = max(begine_count, malware_count)

    with open(output_path, 'w') as file:
        for i in range(max_count):
            if i < malware_count:
                file.write(f'+1\t{malware_urls[i]}\n')
            if i < begine_count:
                file.write(f'-1\t{benign_urls[i]}\n')

benign_csv = 'FinalDataset/URL/Benign_list_big_final.csv'
malware_csv = 'FinalDataset/URL/Malware_dataset.csv'

benign_urls = load_urls_from_csv(benign_csv)
malware_urls = load_urls_from_csv(malware_csv)

begine_count = len(benign_urls)
malware_count = len(malware_urls)

random.shuffle(benign_urls)
random.shuffle(malware_urls)

train_ratio = 0.8
begine_train_count = int(begine_count * train_ratio)
malware_train_count = int(malware_count * train_ratio)

print(f'benign count: {begine_count}\nbegine train count: {begine_train_count}')
print(f'malware count: {malware_count}\nmalware train count: {malware_train_count}')

save_to_txt(benign_urls[:begine_train_count], malware_urls[:malware_train_count], 'train_10000.txt')
save_to_txt(benign_urls[begine_train_count:], malware_urls[malware_train_count:], 'test_10000.txt')
