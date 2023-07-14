---
title: "Hive and Iceberg Quickstart"
weight: 100
url: hive-quickstart
aliases:
    - "quickstart"
    - "quickstarts"
    - "getting-started"
disableSidebar: true
disableToc: true
---
<!--
 - Licensed to the Apache Software Foundation (ASF) under one or more
 - contributor license agreements.  See the NOTICE file distributed with
 - this work for additional information regarding copyright ownership.
 - The ASF licenses this file to You under the Apache License, Version 2.0
 - (the "License"); you may not use this file except in compliance with
 - the License.  You may obtain a copy of the License at
 -
 -   http://www.apache.org/licenses/LICENSE-2.0
 -
 - Unless required by applicable law or agreed to in writing, software
 - distributed under the License is distributed on an "AS IS" BASIS,
 - WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 - See the License for the specific language governing permissions and
 - limitations under the License.
 -->

<!-- {{% quickstarts %}} -->

## Hive and Iceberg Quickstart

This guide will get you up and running with an Iceberg and Hive environment, including sample code to
highlight some powerful features. You can learn more about Iceberg's Hive runtime by checking out the [Hive](../docs/latest/hive/) section.

- [Feature-support](#feature-support)
- [Enabling Iceberg support in Hive](#enabling-iceberg-support-in-hive)
- [Catalog Management](#catalog-management)
- [DDL Commands](#ddl-commands)
- [DML Commands](#dml-commands)

### Docker images

The fastest way to get started is to use [Apache Hive images](https://hub.docker.com/r/apache/hive) 
which provides a SQL-like interface to create and query Iceberg tables from your laptop. You need to install the [Docker Desktop](https://www.docker.com/products/docker-desktop/), choosing the Intel or Apple M1 chip if you have a Mac, or choosing Linux.

Set the version variable:
```export HIVE_VERSION=4.0.0-alpha-2```

Start the container, using the option --platform linux/amd64 for a Mac M1:
```docker run -d --platform linux/amd64 -p 10000:10000 -p 10002:10002 --env SERVICE_NAME=hiveserver2 --name hive4 apache/hive:${HIVE_VERSION}
```

This command configures Hive to use the embedded derby database for Hive Metastore. Hive Metastore functions as the Iceberg catalog to locate Iceberg files, which can be anywhere. 

Give HS2 a little time to come up in the docker container, and then start Hive using beeline as follows:
```docker exec -it hive4 beeline -u 'jdbc:hive2://localhost:10000/'
```

The hive prompt appears:
```0: jdbc:hive2://localhost:10000>
```

You can now run SQL queries, such as ```show databases;```, create Iceberg tables, and query the tables.

### Creating a table

To create your first Iceberg table in Hive, run a [`CREATE TABLE`](../hive#create-table) command. Let's create a table
using `nyc.taxis` where `nyc` is the database name and `taxis` is the table name.

```sql
CREATE DATABASE nyc;
```

```sql
CREATE TABLE nyc.taxis
(
  trip_id bigint,
  trip_distance float,
  fare_amount double,
  store_and_fwd_flag string
)
PARTITIONED BY (vendor_id bigint) STORED BY ICEBERG;
```
Iceberg catalogs support the full range of SQL DDL commands, including:

* [`CREATE TABLE ... PARTITIONED BY`](../hive#create-table)
* [`CREATE TABLE ... AS SELECT`](../hive#create-table-as-select)
* [`CREATE TABLE ... LIKE`](../hive/#create-table-like-table)
* [`ALTER TABLE`](../hive#alter-table)
* [`DROP TABLE`](../hive#drop-table)

### Writing Data to a Table

After your table is created, you can insert records.

```sql
INSERT INTO nyc.taxis
VALUES (1000371, 1.8, 15.32, 'N', 1), (1000372, 2.5, 22.15, 'N', 2), (1000373, 0.9, 9.01, 'N', 2), (1000374, 8.4, 42.13, 'Y', 1);
```

### Reading Data from a Table

To read a table, simply use the Iceberg table's name.

```sql
SELECT * FROM nyc.taxis;
```

### Next steps

#### Adding Iceberg to Hive

If you already have a Hive 4.0.0-alpha-1, or later, environment, it comes with the Iceberg 0.13.1 included. No additional downloads or jars are needed. If you have a Hive 2.3.x or Hive 3.1.x environment see [`Enabling Iceberg support in Hive`](../hive##enabling-iceberg-support-in-hive).

#### Learn More

To learn more about setting up a database other than Derby, see [Apache Hive Quick Start](https://hive.apache.org/developement/quickstart/). You can also [set up a standalone metastore, HS2 and Postgres](https://github.com/apache/hive/blob/master/packaging/src/docker/docker-compose.yml). Now that you're up an running with Iceberg and Hive, check out the [Iceberg-Hive docs](../docs/latest/hive/) to learn more!