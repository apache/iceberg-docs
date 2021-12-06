from generate_asciinema_cast import Cast

sequence = [
    (
        "ALTER TABLE taxis ADD COLUMN fare_per_distance_unit float AFTER trip_distance;",
        "Time taken: 0.671 seconds",
    ),
    (
      "DESCRIBE TABLE nyc.taxis;",
      """VendorID    string
tpep_pickup_datetime    string
tpep_dropoff_datetime    string
passenger_count    string
trip_distance    string
RatecodeID    string
store_and_fwd_flag    string
PULocationID    string
DOLocationID    string
payment_type    string
fare_amount    string
extra    string
mta_tax    string
tip_amount    string
tolls_amount    string
improvement_surcharge    string
total_amount    string
congestion_surcharge    string

# Partitioning
Not partitioned
Time taken: 3.884 seconds, Fetched 21 row(s)""",
    ),
    (
        "UPDATE taxis SET fare_per_distance_unit = fare_amount/trip_distance;",
        "Time taken: 7.917 seconds",
    ),
    (
        "SELECT fare_amount, trip_distance, fare_per_distance_unit FROM taxis limit 10;",
        """5.5    1.20    4.5833335
12.5    3.40    3.6764705
10    2.80    3.5714285
10    2.60    3.8461537
6.5    1.44    4.513889
10.5    2.93    3.5836177
20    6.86    2.915452
7    1.19    5.882353
31.5    11.30    2.7876105
13    3.68    3.5326087
Time taken: 6.736 seconds, Fetched 10 row(s)""",
    ),
]

Cast(sequence).generate_cast(PS1="spark-sql> ").save("output/schema_evolution.cast")
