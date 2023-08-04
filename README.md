# Execution
The final application can ingest any csv file and display the data in sorted order by the specified column(s). The sort order column will be provided as input via config file (* *./config/config.ini* *).



# Running the Solution

1. Ensure you have python3 and pandas installed

2. Place the source csv file here: (* *./data/* *)

3. Update the * *./config/config.ini* * for input_file and sort_column parameters


      **input_file** : source data file path
   
      **sort_column** : column(s) sort order

      **ascending** : Specify True for ascending vs. False for descending w.r.t column sort order above 

5. Run the script : * *python3 usage_data_agg.py* *


*** The script will read the config file, process the data, and display the sorted output. Any anomalies (invalid AccountId or non-integer values) will be logged separately. ***

# Output (expected)

```
    gababa@ganeshs-mini gs-usage-data-agg % /opt/homebrew/bin/python3 /Users/gababa/git/gs-usage-data-agg/usage_data_agg.py
      Date  AccountId  Metric  Usage
2022-03-21          1   likes  70.00
2022-03-31          1 unknown  50.00
2022-12-24          4  amount   2.61
2023-04-02          5   bytes   0.25
2023-04-02         10   bytes   5.73
2023-04-02         10   likes   2.00

```

