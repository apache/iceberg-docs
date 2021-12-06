---
Title: Hidden Partitioning
Img: partition-spec-evolution.png
Category: Services
Draft: false
weight: 200
---

Iceberg handles the tedious and error-prone task of producing partition values for rows in a table and avoids reading unnecessary partitions automatically.
Consumers don’t need to know how the table is partitioned and add extra filters to their queries and the partition layouts can evolve as needed.