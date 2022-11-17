---
title: "Spark and Iceberg Quickstart"
weight: 100
url: spark-quickstart
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

## Spark and Iceberg Quickstart

This guide will get you up and running with an Iceberg and Spark environment, including sample code to
highlight some powerful features. You can learn more about Iceberg's Spark runtime by checking out the [Spark](../docs/latest/spark-ddl/) section.

- [Docker-Compose](#docker-compose)
- [Creating a table](#creating-a-table)
- [Writing Data to a Table](#writing-data-to-a-table)
- [Reading Data from a Table](#reading-data-from-a-table)
- [Adding A Catalog](#adding-a-catalog)
- [Next Steps](#next-steps)

### Docker-Compose

The fastest way to get started is to use a docker-compose file that uses the the [tabulario/spark-iceberg](https://hub.docker.com/r/tabulario/spark-iceberg) image
which contains a local Spark cluster with a configured Iceberg catalog. To use this, you'll need to install the [Docker CLI](https://docs.docker.com/get-docker/) as well as the [Docker Compose CLI](https://github.com/docker/compose-cli/blob/main/INSTALL.md).

Once you have those, save the yaml below into a file named `docker-compose.yml`:

```yaml
version: "3"

services:
  spark-iceberg:
    image: tabulario/spark-iceberg
    container_name: spark-iceberg
    build: spark/
    depends_on:
      - rest
      - minio
    volumes:
      - ./warehouse:/home/iceberg/warehouse
      - ./notebooks:/home/iceberg/notebooks/notebooks
    environment:
      - AWS_ACCESS_KEY_ID=admin
      - AWS_SECRET_ACCESS_KEY=password
      - AWS_REGION=us-east-1
    ports:
      - 8888:8888
      - 8080:8080
    links:
      - rest:rest
      - minio:minio
  rest:
    image: tabulario/iceberg-rest:0.1.0
    ports:
      - 8181:8181
    environment:
      - AWS_ACCESS_KEY_ID=admin
      - AWS_SECRET_ACCESS_KEY=password
      - AWS_REGION=us-east-1
      - CATALOG_WAREHOUSE=s3a://warehouse/wh/
      - CATALOG_IO__IMPL=org.apache.iceberg.aws.s3.S3FileIO
      - CATALOG_S3_ENDPOINT=http://minio:9000
  minio:
    image: minio/minio
    container_name: minio
    environment:
      - MINIO_ROOT_USER=admin
      - MINIO_ROOT_PASSWORD=password
    ports:
      - 9001:9001
      - 9000:9000
    command: ["server", "/data", "--console-address", ":9001"]
  mc:
    depends_on:
      - minio
    image: minio/mc
    container_name: mc
    environment:
      - AWS_ACCESS_KEY_ID=admin
      - AWS_SECRET_ACCESS_KEY=password
      - AWS_REGION=us-east-1
    entrypoint: >
      /bin/sh -c "
      until (/usr/bin/mc config host add minio http://minio:9000 admin password) do echo '...waiting...' && sleep 1; done;
      /usr/bin/mc rm -r --force minio/warehouse;
      /usr/bin/mc mb minio/warehouse;
      /usr/bin/mc policy set public minio/warehouse;
      exit 0;
      "
```

Next, start up the docker containers with this command:
```sh
docker-compose up
```

You can then run any of the following commands to start a Spark session.

{{% codetabs "LaunchSparkClient" %}}
{{% addtab "SparkSQL" "spark-queries" "spark-sql" %}}
{{% addtab "Spark-Shell" "spark-queries" "spark-shell" %}}
{{% addtab "PySpark" "spark-queries" "pyspark" %}}
{{% tabcontent "spark-sql"  %}}
```sh
docker exec -it spark-iceberg spark-sql
```
{{% /tabcontent %}}
{{% tabcontent "spark-shell" %}}
```sh
docker exec -it spark-iceberg spark-shell
```
{{% /tabcontent %}}
{{% tabcontent "pyspark" %}}
```sh
docker exec -it spark-iceberg pyspark
```
{{% /tabcontent %}}
{{% /codetabs %}}
{{< hint info >}}
You can also launch a notebook server by running `docker exec -it spark-iceberg notebook`.
The notebook server will be available at [http://localhost:8888](http://localhost:8888)
{{< /hint >}}

### Creating a table

To create your first Iceberg table in Spark, run a [`CREATE TABLE`](../spark-ddl#create-table) command. Let's create a table
using `demo.nyc.taxis` where `demo` is the catalog name, `nyc` is the database name, and `taxis` is the table name.


{{% codetabs "CreateATable" %}}
{{% addtab "SparkSQL" "spark-queries" "spark-sql" %}}
{{% addtab "Spark-Shell" "spark-queries" "spark-shell" %}}
{{% addtab "PySpark" "spark-queries" "pyspark" %}}
{{% tabcontent "spark-sql"  %}}
```sql
CREATE TABLE demo.nyc.taxis
(
  vendor_id bigint,
  trip_id bigint,
  trip_distance float,
  fare_amount double,
  store_and_fwd_flag string
)
PARTITIONED BY (vendor_id);
```
{{% /tabcontent %}}
{{% tabcontent "spark-shell" %}}
```scala
import org.apache.spark.sql.types._
import org.apache.spark.sql.Row
val schema = StructType( Array(
    StructField("vendor_id", LongType,true),
    StructField("trip_id", LongType,true),
    StructField("trip_distance", FloatType,true),
    StructField("fare_amount", DoubleType,true),
    StructField("store_and_fwd_flag", StringType,true)
))
val df = spark.createDataFrame(spark.sparkContext.emptyRDD[Row],schema)
df.writeTo("demo.nyc.taxis").create()
```
{{% /tabcontent %}}
{{% tabcontent "pyspark" %}}
```py
from pyspark.sql.types import DoubleType, FloatType, LongType, StructType,StructField, StringType
schema = StructType([
  StructField("vendor_id", LongType(), True),
  StructField("trip_id", LongType(), True),
  StructField("trip_distance", FloatType(), True),
  StructField("fare_amount", DoubleType(), True),
  StructField("store_and_fwd_flag", StringType(), True)
])

df = spark.createDataFrame([], schema)
df.writeTo("demo.nyc.taxis").create()
```
{{% /tabcontent %}}
{{% /codetabs %}}

Iceberg catalogs support the full range of SQL DDL commands, including:

* [`CREATE TABLE ... PARTITIONED BY`](../spark-ddl#create-table)
* [`CREATE TABLE ... AS SELECT`](../spark-ddl#create-table--as-select)
* [`ALTER TABLE`](../spark-ddl#alter-table)
* [`DROP TABLE`](../spark-ddl#drop-table)

### Writing Data to a Table

Once your table is created, you can insert records.

{{% codetabs "InsertData" %}}
{{% addtab "SparkSQL" "spark-queries" "spark-sql" %}}
{{% addtab "Spark-Shell" "spark-queries" "spark-shell" %}}
{{% addtab "PySpark" "spark-queries" "pyspark" %}}
{{% tabcontent "spark-sql"  %}}
```sql
INSERT INTO demo.nyc.taxis
VALUES (1, 1000371, 1.8, 15.32, 'N'), (2, 1000372, 2.5, 22.15, 'N'), (2, 1000373, 0.9, 9.01, 'N'), (1, 1000374, 8.4, 42.13, 'Y');
```
{{% /tabcontent %}}
{{% tabcontent "spark-shell" %}}
```scala
import org.apache.spark.sql.Row

val schema = spark.table("demo.nyc.taxis").schema
val data = Seq(
    Row(1: Long, 1000371: Long, 1.8f: Float, 15.32: Double, "N": String),
    Row(2: Long, 1000372: Long, 2.5f: Float, 22.15: Double, "N": String),
    Row(2: Long, 1000373: Long, 0.9f: Float, 9.01: Double, "N": String),
    Row(1: Long, 1000374: Long, 8.4f: Float, 42.13: Double, "Y": String)
)
val df = spark.createDataFrame(spark.sparkContext.parallelize(data), schema)
df.writeTo("demo.nyc.taxis").append()
```
{{% /tabcontent %}}
{{% tabcontent "pyspark" %}}
```py
schema = spark.table("demo.nyc.taxis").schema
data = [
    (1, 1000371, 1.8, 15.32, "N"),
    (2, 1000372, 2.5, 22.15, "N"),
    (2, 1000373, 0.9, 9.01, "N"),
    (1, 1000374, 8.4, 42.13, "Y")
  ]
df = spark.createDataFrame(data, schema)
df.writeTo("demo.nyc.taxis").append()
```
{{% /tabcontent %}}
{{% /codetabs %}}

### Reading Data from a Table

To read a table, simply use the Iceberg table's name.

{{% codetabs "SelectData" %}}
{{% addtab "SparkSQL" "spark-queries" "spark-sql" %}}
{{% addtab "Spark-Shell" "spark-queries" "spark-shell" %}}
{{% addtab "PySpark" "spark-queries" "pyspark" %}}
{{% tabcontent "spark-sql"  %}}
```sql
SELECT * FROM demo.nyc.taxis;
```
{{% /tabcontent %}}
{{% tabcontent "spark-shell" %}}
```scala
val df = spark.table("demo.nyc.taxis").show()
```
{{% /tabcontent %}}
{{% tabcontent "pyspark" %}}
```py
df = spark.table("demo.nyc.taxis").show()
```
{{% /tabcontent %}}
{{% /codetabs %}}


### Adding A Catalog

Iceberg has several catalog back-ends that can be used to track tables, like JDBC, Hive MetaStore and Glue.
Catalogs are configured using properties under `spark.sql.catalog.(catalog_name)`. In this guide,
we use JDBC, but you can follow these instructions to configure other catalog types. To learn more, check out
the [Catalog](../docs/latest/spark-configuration/#catalogs) page in the Spark section.

This configuration creates a path-based catalog named `local` for tables under `$PWD/warehouse` and adds support for Iceberg tables to Spark's built-in catalog.


{{% codetabs "AddingACatalog" %}}
{{% addtab "CLI" "spark-init" "cli" %}}
{{% addtab "spark-defaults.conf" "spark-init" "spark-defaults" %}}
{{% tabcontent "cli"  %}}
```sh
spark-sql --packages org.apache.iceberg:iceberg-spark-runtime-3.2_2.12:{{% icebergVersion %}}\
    --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions \
    --conf spark.sql.catalog.spark_catalog=org.apache.iceberg.spark.SparkSessionCatalog \
    --conf spark.sql.catalog.spark_catalog.type=hive \
    --conf spark.sql.catalog.demo=org.apache.iceberg.spark.SparkCatalog \
    --conf spark.sql.catalog.demo.type=hadoop \
    --conf spark.sql.catalog.demo.warehouse=$PWD/warehouse \
    --conf spark.sql.defaultCatalog=demo
```
{{% /tabcontent %}}
{{% tabcontent "spark-defaults" %}}
```sh
spark.jars.packages                                  org.apache.iceberg:iceberg-spark-runtime-3.2_2.12:{{% icebergVersion %}}
spark.sql.extensions                                 org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
spark.sql.catalog.spark_catalog                      org.apache.iceberg.spark.SparkSessionCatalog
spark.sql.catalog.spark_catalog.type                 hive
spark.sql.catalog.demo                               org.apache.iceberg.spark.SparkCatalog
spark.sql.catalog.demo.type                          hadoop
spark.sql.catalog.demo.warehouse                     $PWD/warehouse
spark.sql.defaultCatalog                             demo
```
{{% /tabcontent %}}
{{% /codetabs %}}


{{< hint info >}}
If your Iceberg catalog is not set as the default catalog, you will have to switch to it by executing `USE demo;`
{{< /hint >}}

### Next steps

#### Adding Iceberg to Spark

If you already have a Spark environment, you can add Iceberg, using the `--packages` option.

{{% codetabs "AddIcebergToSpark" %}}
{{% addtab "SparkSQL" "spark-queries" "spark-sql" %}}
{{% addtab "Spark-Shell" "spark-queries" "spark-shell" %}}
{{% addtab "PySpark" "spark-queries" "pyspark" %}}
{{% tabcontent "spark-sql"  %}}
```sh
spark-sql --packages org.apache.iceberg:iceberg-spark-runtime-3.2_2.12:{{% icebergVersion %}}
```
{{% /tabcontent %}}
{{% tabcontent "spark-shell" %}}
```sh
spark-shell --packages org.apache.iceberg:iceberg-spark-runtime-3.2_2.12:{{% icebergVersion %}}
```
{{% /tabcontent %}}
{{% tabcontent "pyspark" %}}
```sh
pyspark --packages org.apache.iceberg:iceberg-spark-runtime-3.2_2.12:{{% icebergVersion %}}
```
{{% /tabcontent %}}
{{% /codetabs %}}

{{< hint info >}}
If you want to include Iceberg in your Spark installation, add the Iceberg Spark runtime to Spark's `jars` folder.
You can download the runtime by visiting to the [Releases](https://iceberg.apache.org/releases/) page.
{{< /hint >}}

[spark-runtime-jar]: https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-spark-runtime-3.2_2.12/{{% icebergVersion %}}/iceberg-spark-runtime-3.2_2.12-{{% icebergVersion %}}.jar

#### Learn More

Now that you're up an running with Iceberg and Spark, check out the [Iceberg-Spark docs](../docs/latest/spark-ddl/) to learn more!