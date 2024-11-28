import requests
import csv

def load_links(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        links = [row[0] for row in reader]
    return links

def check_link(link):
    try:
        response = requests.head(link, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def save_results(results, output_file):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Link", "Status"])
        for link, status in results:
            writer.writerow([link, "Valid" if status else "Invalid"])

links = load_links("links.csv")
results = [(link, check_link(link)) for link in links]
save_results(results, "results.csv")
print("Проверка завершена.")
