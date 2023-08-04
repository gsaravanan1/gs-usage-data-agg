import pandas as pd
import configparser


def parse_date(date_str):
    return pd.to_datetime(date_str, format="%m/%d/%YT%H:%M:%SZ").strftime("%Y-%m-%d")

def read_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    
    # Read values from the config file
    input_file = config.get("usage_data", "input_file")
    sort_column = config.get("usage_data", "sort_column")
    ascending = config.get("usage_data", "ascending")

    return input_file, sort_column, ascending


def process_file(input_file):
    df = pd.read_csv(input_file, header=None,
                     names=["Date", "AccountId", "Metric", "Usage"])

    # Handling missing and null values in the 'Metric' column
    df["Metric"] = df["Metric"].fillna("unknown")

    # Convert 'Date' column to YYYY-MM-DD format
    df["Date"] = df["Date"].apply(parse_date)

    # Filter and log anomalies (invalid AccountId or non-integer values)
    anomalies = df[~df["AccountId"].astype(str).str.isdigit()]
    df = df[df["AccountId"].astype(str).str.isdigit()]

    # Aggregate data by date, AccountId, and Metric, and calculate usage sum
    grouped_df = df.groupby(["Date", "AccountId", "Metric"])["Usage"].sum().reset_index()

    return grouped_df, anomalies

def main(input_file,sort_column,ascending):  
    data, anomalies = process_file(input_file)
    sorted_data = data.sort_values(by=sort_column.split(','), ascending=list(map(lambda element1: element1.lower().
			capitalize() == "True", ascending.split(','))))
    print(sorted_data.to_string(index=False))
    if not anomalies.empty:
        print("\nAnomalies (Invalid AccountId or Non-Integer Values):\n")
        print(anomalies.to_string(index=False))
    

if __name__ == "__main__":
    config_file = "./config/config.ini"
    input_file, sort_column,ascending = read_config(config_file)
    main(input_file,sort_column,ascending)
