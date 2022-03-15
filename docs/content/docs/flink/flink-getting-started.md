---
title: "Getting Started"
weight: 300
url: flink
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

# Flink

Apache Iceberg supports both [Apache Flink](https://flink.apache.org/)'s DataStream API and Table API. Currently,
Iceberg integration for Apache Flink is available for Flink versions 1.12, 1.13, and 1.14. Previous versions of Iceberg also support Flink 1.11.

| Feature support                                             | Flink  | Notes                                                                                    |
| ----------------------------------------------------------- | -----  |------------------------------------------------------------------------------------------|
| [SQL create catalog](#creating-catalogs-and-using-catalogs) | ✔️     |                                                                                          |
| [SQL create database](#create-database)                     | ✔️     |                                                                                          |
| [SQL create table](#create-table)                           | ✔️     |                                                                                          |
| [SQL create table like](#create-table-like)                 | ✔️     |                                                                                          |
| [SQL alter table](#alter-table)                             | ✔️     | Only supports altering table properties, column and partition changes are not supported. |
| [SQL drop_table](#drop-table)                               | ✔️     |                                                                                          |
| [SQL select](#querying-with-sql)                            | ✔️     | Supports both streaming and batch mode.                                                  |
| [SQL insert into](#insert-into)                             | ✔️ ️   | Supports both streaming and batch mode.                                                  |
| [SQL insert overwrite](#insert-overwrite)                   | ✔️ ️   |                                                                                          |
| [DataStream read](#reading-with-datastream)                 | ✔️ ️   |                                                                                          |
| [DataStream append](#appending-data)                        | ✔️ ️   |                                                                                          |
| [DataStream overwrite](#overwrite-data)                     | ✔️ ️   |                                                                                          |
| [Metadata tables](#inspecting-tables)                       | ️      | Only supports in Java API but not in Flink SQL.                                          |
| [Rewrite files action](#rewrite-files-action)               | ✔️ ️   |                                                                                          |

## Preparation when using Flink SQL Client

To create Iceberg tables in Flink, we recommend using [Flink SQL Client](https://ci.apache.org/projects/flink/flink-docs-stable/dev/table/sqlClient.html) because it's easier for you to understand the concepts.

Step.1 Download the Flink 1.11.x/1.12.x/1.13.x binary package from the Apache Flink [download page](https://flink.apache.org/downloads.html). Since we use Scala 2.12 to archive the `iceberg-flink-runtime` JAR, it's recommended to use a Flink release bundled with Scala 2.12.

```bash
FLINK_VERSION=1.11.1
SCALA_VERSION=2.12
APACHE_FLINK_URL=archive.apache.org/dist/flink/
wget ${APACHE_FLINK_URL}/flink-${FLINK_VERSION}/flink-${FLINK_VERSION}-bin-scala_${SCALA_VERSION}.tgz
tar xzvf flink-${FLINK_VERSION}-bin-scala_${SCALA_VERSION}.tgz
```

Step.2 Start a standalone Flink cluster with Hadoop environment.

```bash
# HADOOP_HOME is your hadoop root directory after unpack the binary package.
export HADOOP_CLASSPATH=`$HADOOP_HOME/bin/hadoop classpath`

# Start the flink standalone cluster
./bin/start-cluster.sh
```

Step.3 Start the Flink SQL client.

We've created a separate `flink-runtime` module in iceberg project for generating a bundled JAR, which could be loaded by the Flink SQL client directly.

If you want to build the `flink-runtime` bundled JAR manually, just build the `iceberg` project, and the bundled JAR will be generated under `<iceberg-root-dir>/flink-runtime/build/libs`.
 
Of course, you could also download the `flink-runtime` JAR from the [apache official repository](https://repo.maven.apache.org/maven2/org/apache/iceberg/iceberg-flink-runtime/).

```bash
# HADOOP_HOME is your hadoop root directory after unpack the binary package.
export HADOOP_CLASSPATH=`$HADOOP_HOME/bin/hadoop classpath`

./bin/sql-client.sh embedded -j <flink-runtime-directory>/iceberg-flink-runtime-xxx.jar shell
```

By default, Iceberg has included Hadoop JARs for the Hadoop catalog. If you want to use the Hive catalog, make sure to load the Hive JARs when starting the Flink SQL Client.
 
Fortunately, Apache Flink has provided a [bundled Hive JAR](https://repo.maven.apache.org/maven2/org/apache/flink/flink-sql-connector-hive-2.3.6_2.11/1.11.0/flink-sql-connector-hive-2.3.6_2.11-1.11.0.jar) for the SQL Client.
 
You could start the Flink SQL Client as the following:

```bash
# HADOOP_HOME is your hadoop root directory after unpack the binary package.
export HADOOP_CLASSPATH=`$HADOOP_HOME/bin/hadoop classpath`

# download Iceberg dependency
ICEBERG_VERSION=0.11.1
MAVEN_URL=https://repo1.maven.org/maven2
ICEBERG_MAVEN_URL=${MAVEN_URL}/org/apache/iceberg
ICEBERG_PACKAGE=iceberg-flink-runtime
wget ${ICEBERG_MAVEN_URL}/${ICEBERG_PACKAGE}/${ICEBERG_VERSION}/${ICEBERG_PACKAGE}-${ICEBERG_VERSION}.jar

# download the flink-sql-connector-hive-${HIVE_VERSION}_${SCALA_VERSION}-${FLINK_VERSION}.jar
HIVE_VERSION=2.3.6
SCALA_VERSION=2.11
FLINK_VERSION=1.11.0
FLINK_CONNECTOR_URL=${MAVEN_URL}/org/apache/flink
FLINK_CONNECTOR_PACKAGE=flink-sql-connector-hive
wget ${FLINK_CONNECTOR_URL}/${FLINK_CONNECTOR_PACKAGE}-${HIVE_VERSION}_${SCALA_VERSION}/${FLINK_VERSION}/${FLINK_CONNECTOR_PACKAGE}-${HIVE_VERSION}_${SCALA_VERSION}-${FLINK_VERSION}.jar

# open the SQL client.
/path/to/bin/sql-client.sh embedded \
    -j ${ICEBERG_PACKAGE}-${ICEBERG_VERSION}.jar \
    -j ${FLINK_CONNECTOR_PACKAGE}-${HIVE_VERSION}_${SCALA_VERSION}-${FLINK_VERSION}.jar \
    shell
```
## Preparation when using Flink's Python API

Install the Apache Flink dependency using `pip`.
```python
pip install apache-flink==1.11.1
```

In order to function properly, `pyflink` needs to access all Hadoop JARs. To achieve this, 
you need to copy those Hadoop JARs to `pyflink`'s installation directory, which can be found under
`<PYTHON_ENV_INSTALL_DIR>/site-packages/pyflink/lib/` (see also a mention of this on [Flink ML](http://mail-archives.apache.org/mod_mbox/flink-user/202105.mbox/%3C3D98BDD2-89B1-42F5-B6F4-6C06A038F978%40gmail.com%3E)).
You can use the following short Python script to copy the Hadoop JARs (make sure that `HADOOP_HOME` points to your Hadoop installation path):

```python
import os
import shutil
import site


def copy_all_hadoop_jars_to_pyflink():
    if not os.getenv("HADOOP_HOME"):
        raise Exception("The HADOOP_HOME env var must be set and point to a valid Hadoop installation")

    jar_files = []

    def find_pyflink_lib_dir():
        for dir in site.getsitepackages():
            package_dir = os.path.join(dir, "pyflink", "lib")
            if os.path.exists(package_dir):
                return package_dir
        return None

    for root, _, files in os.walk(os.getenv("HADOOP_HOME")):
        for file in files:
            if file.endswith(".jar"):
                jar_files.append(os.path.join(root, file))

    pyflink_lib_dir = find_pyflink_lib_dir()

    num_jar_files = len(jar_files)
    print(f"Copying {num_jar_files} Hadoop jar files to pyflink's lib directory at {pyflink_lib_dir}")
    for jar in jar_files:
        shutil.copy(jar, pyflink_lib_dir)


if __name__ == '__main__':
    copy_all_hadoop_jars_to_pyflink()
```

Once the script finishes, you will see some output similar to
```
Copying 645 Hadoop jar files to pyflink's lib directory at <PYTHON_DIR>/lib/python3.8/site-packages/pyflink/lib
```

The next step is to provide a `file://` path that points to the `iceberg-flink-runtime` JAR. This path can be obtained by either building the project
and looking into `<iceberg-root-dir>/flink-runtime/build/libs`, or directly downloading the JAR from the [Apache official repository](https://repo.maven.apache.org/maven2/org/apache/iceberg/iceberg-flink-runtime/).
Third-party libs can be added to `pyflink` via `env.add_jars("file:///my/jar/path/connector.jar")` or `table_env.get_config().get_configuration().set_string("pipeline.jars", "file:///my/jar/path/connector.jar")` (refer to the [Flink Python docs](https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/dev/python/dependency_management/) for more information).
In the following example, we choose `env.add_jars(..)`:

```python
import os

from pyflink.datastream import StreamExecutionEnvironment

env = StreamExecutionEnvironment.get_execution_environment()
iceberg_flink_runtime_jar = os.path.join(os.getcwd(), "iceberg-flink-runtime-{{% icebergVersion %}}.jar")

env.add_jars("file://{}".format(iceberg_flink_runtime_jar))
```

Once finish the above steps, you can create a `StreamTableEnvironment` and execute Flink SQL statements. 
The following example shows how to create a custom catalog via the Python Table API:
```python
from pyflink.table import StreamTableEnvironment
table_env = StreamTableEnvironment.create(env)
table_env.execute_sql("CREATE CATALOG my_catalog WITH ("
                      "'type'='iceberg', "
                      "'catalog-impl'='com.my.custom.CatalogImpl', "
                      "'my-additional-catalog-config'='my-value')")
```

For more details please refer to the [Flink Python Table API](https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/dev/python/table/intro_to_table_api/).

## Creating catalogs and using catalogs.

Flink 1.11+ supports creating catalogs with Flink SQL.

### Catalog Configuration

A catalog can be created and named by executing the following query (replace `<catalog_name>` with your catalog name and
`<config_key>`=`<config_value>` with catalog implementation configs):   

```sql
CREATE CATALOG <catalog_name> WITH (
  'type'='iceberg',
  `<config_key>`=`<config_value>`
); 
```

The following properties can be set globally and are not limited to a specific catalog implementation:

* `type`: Must be `iceberg`. (Required)
* `catalog-type`: `hive` or `hadoop` for built-in catalogs, or leave unset for custom catalog implementations. (Optional)
* `catalog-impl`: The fully-qualified class name of the custom catalog implementation. Must be set if `catalog-type` is unset. (Optional)
* `property-version`: The version number for properties. This value is essential for backwards compatibility in case the property format changes. The current property version is `1`. (Optional)
* `cache-enabled`: Whether to enable catalog cache. The default value is `true`. (Optional)

### Hive catalog

The following statement creates an Iceberg catalog named `hive_catalog`. With the property `'catalog-type'='hive'`, it can load tables from a hive metastore:

```sql
CREATE CATALOG hive_catalog WITH (
  'type'='iceberg',
  'catalog-type'='hive',
  'uri'='thrift://localhost:9083',
  'clients'='5',
  'property-version'='1',
  'warehouse'='hdfs://nn:8020/warehouse/path'
);
```

The following properties are supported when setting a Hive catalog:

* `uri`: The Hive metastore's thrift URI. (Required)
* `clients`: The Hive metastore's client pool size. The default value is 2. (Optional)
* `warehouse`: The Hive warehouse's location. Users should specify this path if neither set the `hive-conf-dir` to specify a location containing a `hive-site.xml` configuration file nor add a correct `hive-site.xml` to the classpath.
* `hive-conf-dir`: Path to the directory containing the `hive-site.xml` configuration file that will be used to offer custom Hive configuration values. The value of `hive.metastore.warehouse.dir` from `<hive-conf-dir>/hive-site.xml` (or the hive configuration file from the classpath) will be overwritten with the `warehouse` value if both `hive-conf-dir` and `warehouse` are set.

### Hadoop catalog

Iceberg also supports a directory-based catalog in HDFS. It can be configured using `'catalog-type'='hadoop'`:

```sql
CREATE CATALOG hadoop_catalog WITH (
  'type'='iceberg',
  'catalog-type'='hadoop',
  'warehouse'='hdfs://nn:8020/warehouse/path',
  'property-version'='1'
);
```

The following properties are supported when setting a Hadoop catalog:

* `warehouse`: The HDFS directory to store metadata files and data files. (Required)

Users can set the currently used catalog with the SQL command `USE CATALOG xx_catalog`.

### Custom catalog

Flink also supports loading a custom Iceberg `Catalog` implementation by specifying the `catalog-impl` property. Here is an example:

```sql
CREATE CATALOG my_catalog WITH (
  'type'='iceberg',
  'catalog-impl'='com.my.custom.CatalogImpl',
  'my-additional-catalog-config'='my-value'
);
```

### Creating catalogs with YAML config

Catalogs can be registered in `sql-client-defaults.yaml` before the Flink SQL client is started. Here is an example:

```yaml
catalogs: 
  - name: my_catalog
    type: iceberg
    catalog-type: hadoop
    warehouse: hdfs://nn:8020/warehouse/path
```

## DDL commands

### `CREATE DATABASE`

By default, Iceberg uses the `default` database in Flink. Use the following commands to create a separate database if you don't want to create tables in the `default` database:

```sql
CREATE DATABASE iceberg_db;
USE iceberg_db;
```

### `CREATE TABLE`

```sql
CREATE TABLE `hive_catalog`.`default`.`sample` (
    id BIGINT COMMENT 'unique id',
    data STRING
);
```

Table creation command supports the most commonly used [Flink create table clauses](https://ci.apache.org/projects/flink/flink-docs-release-1.11/dev/table/sql/create.html#create-table), which includes

* `PARTITION BY (column1, column2, ...)` for partitioning configuration (Flink doesn't support hidden partitioning yet);
* `COMMENT 'table document'` for setting a table description;
* `WITH ('key'='value', ...)` for setting [table configuration](../configuration) that will be stored in Iceberg table properties.

Currently, functionalities such as computed columns, primary keys(????????????????????), and watermark definitions are not supported.

### `PARTITIONED BY`

To create a partitioned table, use `PARTITIONED BY`:

```sql
CREATE TABLE `hive_catalog`.`default`.`sample` (
    id BIGINT COMMENT 'unique id',
    data STRING
) PARTITIONED BY (data);
```

Iceberg features hidden partition. However, as Flink doesn't support partitioning by a function on columns, hidden partition is unavailable for Flink DDL now.
We will add this once Flink DDL is improved in the future.

### `CREATE TABLE LIKE`

To create a table with the same schema, partitioning, and table properties from another table, use `CREATE TABLE LIKE`.

```sql
CREATE TABLE `hive_catalog`.`default`.`sample` (
    id BIGINT COMMENT 'unique id',
    data STRING
);

CREATE TABLE  `hive_catalog`.`default`.`sample_like` LIKE `hive_catalog`.`default`.`sample`;
```

For more details, please refer to the [Flink `CREATE TABLE` documentation](https://ci.apache.org/projects/flink/flink-docs-release-1.11/dev/table/sql/create.html#create-table).


### `ALTER TABLE`

Iceberg only supports altering table properties in flink 1.11+(?????????????????????????????) now.

```sql
ALTER TABLE `hive_catalog`.`default`.`sample` SET ('write.format.default'='avro')
```

### `ALTER TABLE .. RENAME TO`

```sql
ALTER TABLE `hive_catalog`.`default`.`sample` RENAME TO `hive_catalog`.`default`.`new_sample`;
```

### `DROP TABLE`

To delete a table, run

```sql
DROP TABLE `hive_catalog`.`default`.`sample`;
```

## Querying with SQL

Iceberg supports both streaming and batch read in Flink now. With the following SQL commands, you could switch the execution type from 'streaming' mode to 'batch' mode, and vice versa:

```sql
-- Execute the flink job in streaming mode for current session context
SET execution.type = streaming

-- Execute the flink job in batch mode for current session context
SET execution.type = batch
```

### Flink batch read

If you want to fetch all rows from an Iceberg table with a flink __batch__ job, execute the following statements:

```sql
-- Execute the flink job in batch mode for current session context
SET execution.type = batch ;
SELECT * FROM sample       ;
```

Currently, batch querying a previous snapshot of a table (time travel) with Flink SQL is not supported????????????????????

### Flink streaming read

Iceberg supports processing incremental data starting from a historical snapshot-id with Flink streaming jobs:

```sql
-- Submit the flink job in streaming mode for current session.
SET execution.type = streaming ;

-- Enable this switch because streaming read SQL will provide few job options in flink SQL hint options.
SET table.dynamic-table-options.enabled=true;

-- Read all the records from the iceberg current snapshot, and then read incremental data starting from that snapshot.
SELECT * FROM sample /*+ OPTIONS('streaming'='true', 'monitor-interval'='1s')*/ ;

-- Read all incremental data starting from the snapshot-id '3821550127947089987' (records from this snapshot will be excluded).
SELECT * FROM sample /*+ OPTIONS('streaming'='true', 'monitor-interval'='1s', 'start-snapshot-id'='3821550127947089987')*/ ;
```

The following are some options that could be set in Flink SQL hint options for streaming jobs:

* monitor-interval: the time interval for consecutively monitoring newly committed data files (default value: '1s').
* start-snapshot-id: the snapshot id that the streaming job starts fetching data from.

## Writing with SQL

Iceberg supports both `INSERT INTO` and `INSERT OVERWRITE` in flink 1.11+.

### `INSERT INTO`

To append new data to a table with a Flink streaming job, use `INSERT INTO`:

```sql
INSERT INTO `hive_catalog`.`default`.`sample` VALUES (1, 'a');
INSERT INTO `hive_catalog`.`default`.`sample` SELECT id, data from other_kafka_table;
```

### `INSERT OVERWRITE`

To partially/fully replace a table with the result of a query, use `INSERT OVERWRITE` in a batch job (Flink streaming job does not support `INSERT OVERWRITE`). Overwrites are atomic operations for Iceberg tables.

Partitions that have rows produced by the SELECT query will be replaced. For example,

```sql
INSERT OVERWRITE sample VALUES (1, 'a');
```

Iceberg also supports overwriting designated partitions with the "selected" values:

```sql
INSERT OVERWRITE `hive_catalog`.`default`.`sample` PARTITION(data='a') SELECT 6;
```

For a partitioned Iceberg table, when all the partitioning columns are set values in the `PARTITION` clause, the query result will be written to a static partition;
otherwise, if only partial partition columns (must be the prefix of all partitioning columns) are set values in the `PARTITION` clause, the query result will be written to a dynamic partition.
For an unpartitioned Iceberg table, it will be completely overwritten by `INSERT OVERWRITE`.

## Reading with DataStream

Iceberg supports streaming or batch read in Flink Java API.

### Batch Read

The following example shows a Flink batch job that reads all records from an Iceberg table and then print them to stdout:

```java
StreamExecutionEnvironment env = StreamExecutionEnvironment.createLocalEnvironment();
TableLoader tableLoader = TableLoader.fromHadoopTable("hdfs://nn:8020/warehouse/path");
DataStream<RowData> batch = FlinkSource.forRowData()
     .env(env)
     .tableLoader(tableLoader)
     .streaming(false)
     .build();

// Print all records to stdout.
batch.print();

// Submit and execute this batch read job.
env.execute("Test Iceberg Batch Read");
```

### Streaming read

The following example shows a Flink streaming job that incrementally reads records starting from snapshot-id '3821550127947089987' and continuously print them to stdout:

```java
StreamExecutionEnvironment env = StreamExecutionEnvironment.createLocalEnvironment();
TableLoader tableLoader = TableLoader.fromHadoopTable("hdfs://nn:8020/warehouse/path");
DataStream<RowData> stream = FlinkSource.forRowData()
     .env(env)
     .tableLoader(tableLoader)
     .streaming(true)
     .startSnapshotId(3821550127947089987L)
     .build();

// Print all records to stdout.
stream.print();

// Submit and execute this streaming read job.
env.execute("Test Iceberg Streaming Read");
```

For other options that could be set with Flink Java API, please refer to [FlinkSource#Builder](../../../javadoc/{{% icebergVersion %}}/org/apache/iceberg/flink/source/FlinkSource.html).

## Writing with DataStream

Iceberg Java API supports writing different kinds of DataStreams to Iceberg tables.


### Appending data

Writing `DataStream<RowData>` and `DataStream<Row>` to an Iceberg table sink is natively supported.

```java
StreamExecutionEnvironment env = ...;

DataStream<RowData> input = ... ;
Configuration hadoopConf = new Configuration();
TableLoader tableLoader = TableLoader.fromHadoopTable("hdfs://nn:8020/warehouse/path", hadoopConf);

FlinkSink.forRowData(input)
    .tableLoader(tableLoader)
    .build();

env.execute("Test Iceberg DataStream");
```

The current API also allows users to write generic `DataStream<T>` to an Iceberg table. For more information, please refer to this [unit test class](https://github.com/apache/iceberg/blob/master/flink/src/test/java/org/apache/iceberg/flink/sink/TestFlinkIcebergSink.java).

### Overwrite data

To dynamically overwrite data in an existing Iceberg table, you could set the `overwrite` option in the FlinkSink builder.

```java
StreamExecutionEnvironment env = ...;

DataStream<RowData> input = ... ;
Configuration hadoopConf = new Configuration();
TableLoader tableLoader = TableLoader.fromHadoopTable("hdfs://nn:8020/warehouse/path", hadoopConf);

FlinkSink.forRowData(input)
    .tableLoader(tableLoader)
    .overwrite(true)
    .build();

env.execute("Test Iceberg DataStream");
```

## Inspecting tables

Iceberg does not support inspecting table in Flink SQL now. Users have to use [Iceberg's Java API](../api) to read Iceberg's metadata for those table information.

## Rewrite files action

To deal with small files, Iceberg offers a Flink action (batch job) that can rewrite small files into larger ones.

The behavior of this Flink action is similar to Spark's [rewriteDataFiles](../maintenance/#compact-data-files).

```java
import org.apache.iceberg.flink.actions.Actions;

TableLoader tableLoader = TableLoader.fromHadoopTable("hdfs://nn:8020/warehouse/path");
Table table = tableLoader.loadTable();
RewriteDataFilesActionResult result = Actions.forTable(table)
        .rewriteDataFiles()
        .execute();
```

For more information about the available options of the rewrite files action, please see [RewriteDataFilesAction](../../../javadoc/{{% icebergVersion %}}/org/apache/iceberg/flink/actions/RewriteDataFilesAction.html)

## Future improvement

There are some features that are not yet supported in the current Flink Iceberg integration API:

* Creating Iceberg tables with hidden partitioning. [Discussion](http://mail-archives.apache.org/mod_mbox/flink-dev/202008.mbox/%3cCABi+2jQCo3MsOa4+ywaxV5J-Z8TGKNZDX-pQLYB-dG+dVUMiMw@mail.gmail.com%3e) in flink mail list.
* Creating Iceberg tables with computed columns.
* Creating Iceberg tables with watermarks.
* Adding, removing, renaming or changing columns. [FLINK-19062](https://issues.apache.org/jira/browse/FLINK-19062) is tracking this.
