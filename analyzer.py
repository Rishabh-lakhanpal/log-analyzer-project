# analyzer.py

from collections import Counter
import csv

LOG_FILE = "access_log"
OUTPUT_CSV = "report.csv"

def parse_log_line(line):
    parts = line.split()
    if len(parts) < 9:
        return None
    ip = parts[0]
    endpoint = parts[6]
    status = parts[8]
    return ip, endpoint, status

def analyze_log(file_path):
    ip_counter = Counter()
    endpoint_counter = Counter()
    status_counter = Counter()

    with open(file_path, 'r') as f:
        for line in f:
            result = parse_log_line(line)
            if result:
                ip, endpoint, status = result
                ip_counter[ip] += 1
                endpoint_counter[endpoint] += 1
                status_counter[status] += 1

    return ip_counter, endpoint_counter, status_counter

def write_report(ip_data, endpoint_data, status_data, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Section", "Item", "Count"])

        writer.writerow(["Top IPs", "", ""])
        for ip, count in ip_data.most_common(5):
            writer.writerow(["", ip, count])

        writer.writerow(["Top Endpoints", "", ""])
        for endpoint, count in endpoint_data.most_common(5):
            writer.writerow(["", endpoint, count])

        writer.writerow(["Response Codes", "", ""])
        for status, count in status_data.most_common():
            writer.writerow(["", status, count])

if __name__ == "__main__":
    ip_data, endpoint_data, status_data = analyze_log(LOG_FILE)
    write_report(ip_data, endpoint_data, status_data, OUTPUT_CSV)
    print(f"Log analysis complete. Report saved to {OUTPUT_CSV}")
