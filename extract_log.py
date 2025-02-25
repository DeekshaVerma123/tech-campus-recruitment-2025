import sys
import os

def extract_logs(log_file, target_date):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"output_{target_date}.txt")

    with open(log_file, "r", encoding="utf-8") as file, open(output_file, "w", encoding="utf-8") as out:
        for line in file:
            if line.startswith(target_date):
                out.write(line)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)
    
    date = sys.argv[1]
    log_file = "large_log_file.txt"
    
    extract_logs(log_file, date)
    print(f"Logs for {date} have been saved to output/output_{date}.txt")
