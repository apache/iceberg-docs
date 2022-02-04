---
bookCollapseSection: true
weight: 1100
url: releases
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

## Downloads

The latest version of Iceberg is [{{% icebergVersion %}}](https://github.com/apache/iceberg/releases/tag/apache-iceberg-{{% icebergVersion %}}).

* [{{% icebergVersion %}} source tar.gz](https://www.apache.org/dyn/closer.cgi/iceberg/apache-iceberg-{{% icebergVersion %}}/apache-iceberg-{{% icebergVersion %}}.tar.gz) -- [signature](https://downloads.apache.org/iceberg/apache-iceberg-{{% icebergVersion %}}/apache-iceberg-{{% icebergVersion %}}.tar.gz.asc) -- [sha512](https://downloads.apache.org/iceberg/apache-iceberg-{{% icebergVersion %}}/apache-iceberg-{{% icebergVersion %}}.tar.gz.sha512)
* [{{% icebergVersion %}} Spark 3.2 runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-spark-runtime-3.2_2.12/{{% icebergVersion %}}/iceberg-spark-runtime-3.2_2.12-{{% icebergVersion %}}.jar)
* [{{% icebergVersion %}} Spark 3.1 runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-spark-runtime-3.1_2.12/{{% icebergVersion %}}/iceberg-spark-runtime-3.1_2.12-{{% icebergVersion %}}.jar)
* [{{% icebergVersion %}} Spark 3.0 runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-spark3-runtime/{{% icebergVersion %}}/iceberg-spark3-runtime-{{% icebergVersion %}}.jar)
* [{{% icebergVersion %}} Spark 2.4 runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-spark-runtime/{{% icebergVersion %}}/iceberg-spark-runtime-{{% icebergVersion %}}.jar)
* [{{% icebergVersion %}} Flink 1.14 runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-flink-runtime-1.14/{{% icebergVersion %}}/iceberg-flink-runtime-1.14-{{% icebergVersion %}}.jar)
* [{{% icebergVersion %}} Flink 1.13 runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-flink-runtime-1.13/{{% icebergVersion %}}/iceberg-flink-runtime-1.13-{{% icebergVersion %}}.jar)
* [{{% icebergVersion %}} Flink 1.12 runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-flink-runtime-1.12/{{% icebergVersion %}}/iceberg-flink-runtime-1.12-{{% icebergVersion %}}.jar)
* [{{% icebergVersion %}} Hive runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-hive-runtime/{{% icebergVersion %}}/iceberg-hive-runtime-{{% icebergVersion %}}.jar)

To use Iceberg in Spark/Flink, download the runtime JAR based on your Spark/Flink version and add it to the jars folder of your Spark/Flink install.

To use Iceberg in Hive, download the Hive runtime JAR and add it to Hive using `ADD JAR`.

### Gradle

To add a dependency on Iceberg in Gradle, add the following to `build.gradle`:

```
dependencies {
  compile 'org.apache.iceberg:iceberg-core:{{% icebergVersion %}}'
}
```

You may also want to include `iceberg-parquet` for Parquet file support.

### Maven

To add a dependency on Iceberg in Maven, add the following to your `pom.xml`:

```
<dependencies>
  ...
  <dependency>
    <groupId>org.apache.iceberg</groupId>
    <artifactId>iceberg-core</artifactId>
    <version>{{% icebergVersion %}}</version>
  </dependency>
  ...
</dependencies>
```

## 0.13.0 Release Notes

Apache Iceberg 0.13.0 was released on February 4th, 2022.

**High-level features:**

* **Core**
  * Partition spec ID (`spec_id`) is added to the `data_files` spec and can be queried in related metadata tables [[\#3015](https://github.com/apache/iceberg/pull/3015)]
  * ORC delete file write support is added [[\#3248](https://github.com/apache/iceberg/pull/3248)] [[\#3250](https://github.com/apache/iceberg/pull/3250)] [[\#3366](https://github.com/apache/iceberg/pull/3366)]
  * Catalog caching now supports cache expiration through catalog property `cache.expiration-interval-ms` [[\#3543](https://github.com/apache/iceberg/pull/3543)]
  * Legacy Parquet tables (e.g. produced by `ParquetHiveSerDe` or Spark `spark.sql.parquet.writeLegacyFormat=true` and migrated to Iceberg) are fully supported [[\#3723](https://github.com/apache/iceberg/pull/3723)]
  * `NOT_STARTS_WITH` expression support is added to improve Iceberg predicate-pushdown query performance [[\#2062](https://github.com/apache/iceberg/pull/2062)]
  * Hadoop catalog now supports atomic commit using a pessimistic lock manager [[\#3663](https://github.com/apache/iceberg/pull/3663)]
  * Iceberg catalog now supports registration of Iceberg table from a given metadata file location [[\#3851](https://github.com/apache/iceberg/pull/3851)]
* **Vendor Integrations**
  * `ResolvingFileIO` is added to support using multiple `FileIO`s to access different storage providers based on file scheme. [[\#3593](https://github.com/apache/iceberg/pull/3593)]
  * Google Cloud Storage (GCS) `FileIO` support is added [[\#3711](https://github.com/apache/iceberg/pull/3711)]
  * Aliyun Object Storage Service (OSS) `FileIO` support is added [[\#3553](https://github.com/apache/iceberg/pull/3553)]
  * AWS `S3FileIO` now supports server-side checksum validation [[\#3813](https://github.com/apache/iceberg/pull/3813)]
  * S3-compatible cloud storages (e.g. MinIO) can now be accessed through AWS `S3FileIO` with custom endpoint and credential configurations [[\#3656](https://github.com/apache/iceberg/pull/3656)] [[\#3658](https://github.com/apache/iceberg/pull/3658)]
* **Spark**
  * Spark 3.2 support is added [[\#3335](https://github.com/apache/iceberg/pull/3335)]
  * Spark 3.2 supports merge-on-read `DELETE` [[\#3970](https://github.com/apache/iceberg/pull/3970)]
  * `RewriteDataFiles` action now supports sorting [[\#2829](https://github.com/apache/iceberg/pull/2829)] and merge-on-read delete compaction [[\#3454](https://github.com/apache/iceberg/pull/3454)]
  * Call procedure `rewrite_data_files` is added to perform Iceberg data file optimization and compaction [[\#3375](https://github.com/apache/iceberg/pull/3375)]
  * Spark SQL time travel support is added. Snapshot schema is now used instead of the table's latest schema [[\#3722](https://github.com/apache/iceberg/pull/3722)]
  * Spark vectorized merge-on-read support is added [[\#3557](https://github.com/apache/iceberg/pull/3557)] [[\#3287](https://github.com/apache/iceberg/pull/3287)]
  * Call procedure `ancestors_of` is added to access snapshot ancestor information [[\#3444](https://github.com/apache/iceberg/pull/3444)]
  * Truncate [[\#3708](https://github.com/apache/iceberg/pull/3708)] and bucket [[\#3089](https://github.com/apache/iceberg/pull/3368)] UDFs are added for calculating for partition transform values
* **Flink**
  * Flink 1.13 and 1.14 supports are added [[\#3116](https://github.com/apache/iceberg/pull/3116)] [[\#3434](https://github.com/apache/iceberg/pull/3434)]
  * Flink connector support is added [[\#2666](https://github.com/apache/iceberg/pull/2666)]
  * Upsert write option is added [[\#2863](https://github.com/apache/iceberg/pull/2863)]
  * Avro delete file read support is added [[\#3540](https://github.com/apache/iceberg/pull/3540)]
* **Hive**
  * Hive tables can now be read through name mapping during Hive-to-Iceberg table migration [[\#3312](https://github.com/apache/iceberg/pull/3312)]
  * Table listing in Hive catalog can skip non-Iceberg tables using flag `list-all-tables` [[\#3908](https://github.com/apache/iceberg/pull/3908)]
  * `uuid` is now a reserved Iceberg table property and exposed for Iceberg table in a Hive metastore for duplication check [[\#3914](https://github.com/apache/iceberg/pull/3914)]
  
**Important bug fixes:**

* **Core**
  * Iceberg new data file root path is configured through `write.data.path` going forward. `write.folder-storage.path` and `write.object-storage.path` are deprecated [[\#3094](https://github.com/apache/iceberg/pull/3094)]
  * Catalog commit status is `UNKNOWN` instead of `FAILURE` when new metadata location cannot be found in snapshot history [[\#3717](https://github.com/apache/iceberg/pull/3717)]
  * Metrics mode for sort order source columns is default to at least `truncate[16]` for better predicate pushdown performance [[\#2240](https://github.com/apache/iceberg/pull/2240)]
  * `RowDelta` transactions can commit delete files of multiple partition specs instead of just a single one [[\#2985](https://github.com/apache/iceberg/pull/2985)]
  * Hadoop catalog now returns false when dropping a table that does not exist instead of returning true [[\#3097](https://github.com/apache/iceberg/pull/3097)]
  * ORC vectorized read can be configured using `read.orc.vectorization.batch-size` instead of `read.parquet.vectorization.batch-size`  [[\#3133](https://github.com/apache/iceberg/pull/3133)]
  * Using `Catalog` and `FileIO` no longer requires Hadoop dependencies in the execution environment [[\#3590](https://github.com/apache/iceberg/pull/3590)]
  * Dropping table now deletes old metadata files instead of leaving them strained [[\#3622](https://github.com/apache/iceberg/pull/3622)]
  * Iceberg thread pool now uses at least 2 threads for query planning (can be changed with the `iceberg.worker.num-threads` config) [[\#3811](https://github.com/apache/iceberg/pull/3811)]
  * `history` and `snapshots` metadata tables can query tables with no current snapshot instead of returning empty [[\#3812](https://github.com/apache/iceberg/pull/3812)]
  * `partition` metadata table supports tables with a partition column named `partition` [[\#3845](https://github.com/apache/iceberg/pull/3845)] 
  * Potential deadlock risk in catalog caching is resolved [[\#3801](https://github.com/apache/iceberg/pull/3801)], and cache is immediately refreshed when table is reloaded in another program [[\#3873](https://github.com/apache/iceberg/pull/3873)]
  * `STARTS_WITH` expression now supports filtering `null` values instead of throwing exception [[\#3645](https://github.com/apache/iceberg/pull/3645)]
  * Deleting and adding a partition field with the same name is supported instead of throwing exception (deleting and adding the same field is a noop) [[\#3632](https://github.com/apache/iceberg/pull/3632)] [[\#3954](https://github.com/apache/iceberg/pull/3954)]
  * Parquet file writing issue is fixed for data with over 16 unparseable chars [[\#3760](https://github.com/apache/iceberg/pull/3760)]
  * Delete manifests with only existing files are now included in scan planning instead of being ignored [[\#3945](https://github.com/apache/iceberg/pull/3945)]
* **Vendor Integrations**
  * AWS related client connection resources are now properly closed when not used [[\#2878](https://github.com/apache/iceberg/pull/2878)]
  * AWS Glue catalog now displays more table information including location, description [[\#3467](https://github.com/apache/iceberg/pull/3467)] and used columns [[\#3888](https://github.com/apache/iceberg/pull/3888)]
* **Spark**
  * `RewriteDataFiles` action is improved to produce files with more balanced output size [[\#3073](https://github.com/apache/iceberg/pull/3073)] [[\#3292](https://github.com/apache/iceberg/pull/3292)]
  * `REFRESH TABLE` can now be used with Spark session catalog instead of throwing exception [[\#3072](https://github.com/apache/iceberg/pull/3072)]
  * Read performance is improved using better table size estimation [[\#3134](https://github.com/apache/iceberg/pull/3134)]
  * Insert overwrite mode now skips empty partition instead of throwing exception [[\#2895](https://github.com/apache/iceberg/issues/2895)]
  * `add_files` procedure now skips duplicated files by default (can be turned off with the `check_duplicate_files` flag) [[\#2895](https://github.com/apache/iceberg/issues/2779)], skips folder without file [[\#2895](https://github.com/apache/iceberg/issues/3455)] and partitions with `null` values [[\#2895](https://github.com/apache/iceberg/issues/3778)] instead of throwing exception, and supports partition pruning for faster table import [[\#3745](https://github.com/apache/iceberg/issues/3745)] 
  * Reading unknown partition transform (e.g. old reader reading new transform type) will now throw `ValidationException` instead of causing unknown behavior downstream [[\#2992](https://github.com/apache/iceberg/issues/2992)]
  * Snapshot expiration now supports custom `FileIO` instead of just `HadoopFileIO` [[\#3089](https://github.com/apache/iceberg/pull/3089)]
  * `REPLACE TABLE AS SELECT` can now work with tables with columns that have changed partition transform. Each old partition field of the same column is converted to a void transform with a different name [[\#3421](https://github.com/apache/iceberg/issues/3421)]
  * SQLs containing binary or fixed literals can now be parsed correctly instead of throwing exception [[\#3728](https://github.com/apache/iceberg/pull/3728)]
* **Flink**
  * A `ValidationException` will be thrown if a user configures both `catalog-type` and `catalog-impl`. Previously it chose to use `catalog-type`. The new behavior brings Flink consistent with Spark and Hive [[\#3308](https://github.com/apache/iceberg/issues/3308)]
  * Changelog tables can now be queried without `RowData` serialization issues [[\#3240](https://github.com/apache/iceberg/pull/3240)]
  * Data overflow problem is fixed when writing time data of type `java.sql.Time` [[\#3740](https://github.com/apache/iceberg/pull/3740)]
* **Hive**
  * Hive metastore client retry logic is improved using `RetryingMetaStoreClient` [[\#3099](https://github.com/apache/iceberg/pull/3099)]
  * Hive catalog can now be initialized using a `null` Hadoop configuration instead of throwing exception [[\3252](https://github.com/apache/iceberg/pull/3252)]
  * Table creation can succeed instead of throwing exception when some columns do not have comments [[\#3531](https://github.com/apache/iceberg/pull/3531)]
  * Vectorized read performance is improved by using split offset information in `OrcTail` [[\#3748](https://github.com/apache/iceberg/pull/3748)]
  * Read performance can now be improved by disabling `FileIO` serialization using Hadoop config `iceberg.mr.config.serialization.disabled` [[\#3752](https://github.com/apache/iceberg/pull/3752)]

**Other notable changes:**

* The community has finalized the long-term strategy of Spark, Flink and Hive support. Iceberg will start to provide version-specific implementations and runtime executables to ensure a smooth integration experience for Iceberg users.
* The Iceberg Python module is renamed as [python_legacy](https://github.com/apache/iceberg/tree/master/python_legacy) [[\#3074](https://github.com/apache/iceberg/pull/3074)]. A [new Python module](https://github.com/apache/iceberg/tree/master/python) is under development to provide better user experience for the Python community. See the [Github Project](https://github.com/apache/iceberg/projects/7) for progress.
* Iceberg starts to publish daily snapshot in the [Apache snapshot repository](https://repository.apache.org/content/groups/snapshots/org/apache/iceberg/) [[\#3353](https://github.com/apache/iceberg/pull/3353)] for developers that would like to consume the latest unreleased artifact.
* Iceberg website is now managed by a separated repository [iceberg-docs](https://github.com/apache/iceberg-docs/) with a new look. See [README](https://github.com/apache/iceberg-docs/blob/main/README.md) for contribution guidelines going forward.
* An OpenAPI specification is developed for Iceberg catalog to prepare for a REST-based Iceberg catalog implementation [[\#3770](https://github.com/apache/iceberg/pull/3770)]
* Dependency version upgrades:
  * Gradle is upgraded to 7.3 [[\#3525](https://github.com/apache/iceberg/pull/3525)]
  * Parquet is upgraded to 1.12.2 [[\#3551](https://github.com/apache/iceberg/pull/3551)]
  * ORC is upgraded to 1.7 [[\#3493](https://github.com/apache/iceberg/pull/3493)]
  * Arrow is upgraded to 6.0 [[\#3690](https://github.com/apache/iceberg/pull/3446)]
  * Nessie is upgraded to 0.18 [[\#3890](https://github.com/apache/iceberg/pull/3890)]

## Past releases

### 0.12.1

Apache Iceberg 0.12.1 was released on November 8th, 2021.

* Git tag: [0.12.1](https://github.com/apache/iceberg/releases/tag/apache-iceberg-0.12.1)
* [0.12.1 source tar.gz](https://www.apache.org/dyn/closer.cgi/iceberg/apache-iceberg-0.12.1/apache-iceberg-0.12.1.tar.gz) -- [signature](https://downloads.apache.org/iceberg/apache-iceberg-0.12.1/apache-iceberg-0.12.1.tar.gz.asc) -- [sha512](https://downloads.apache.org/iceberg/apache-iceberg-0.12.1/apache-iceberg-0.12.1.tar.gz.sha512)
* [0.12.1 Spark 3.x runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-spark3-runtime/0.12.1/iceberg-spark3-runtime-0.12.1.jar)
* [0.12.1 Spark 2.4 runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-spark-runtime/0.12.1/iceberg-spark-runtime-0.12.1.jar)
* [0.12.1 Flink runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-flink-runtime/0.12.1/iceberg-flink-runtime-0.12.1.jar)
* [0.12.1 Hive runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-hive-runtime/0.12.1/iceberg-hive-runtime-0.12.1.jar)

Important bug fixes and changes:

* [\#3264](https://github.com/apache/iceberg/pull/3258) fixes validation failures that occurred after snapshot expiration when writing Flink CDC streams to Iceberg tables.
* [\#3264](https://github.com/apache/iceberg/pull/3264) fixes reading projected map columns from Parquet files written before Parquet 1.11.1.
* [\#3195](https://github.com/apache/iceberg/pull/3195) allows validating that commits that produce row-level deltas don't conflict with concurrently added files. Ensures users can maintain serializable isolation for update and delete operations, including merge operations.
* [\#3199](https://github.com/apache/iceberg/pull/3199) allows validating that commits that overwrite files don't conflict with concurrently added files. Ensures users can maintain serializable isolation for overwrite operations.
* [\#3135](https://github.com/apache/iceberg/pull/3135) fixes equality-deletes using `DATE`, `TIMESTAMP`, and `TIME` types.
* [\#3078](https://github.com/apache/iceberg/pull/3078) prevents the JDBC catalog from overwriting the `jdbc.user` property if any property called user exists in the environment.
* [\#3035](https://github.com/apache/iceberg/pull/3035) fixes drop namespace calls with the DyanmoDB catalog.
* [\#3273](https://github.com/apache/iceberg/pull/3273) fixes importing Avro files via `add_files` by correctly setting the number of records.
* [\#3332](https://github.com/apache/iceberg/pull/3332) fixes importing ORC files with float or double columns in `add_files`.

A more exhaustive list of changes is available under the [0.12.1 release milestone](https://github.com/apache/iceberg/milestone/15?closed=1).

### 0.12.0

Apache Iceberg 0.12.0 was released on August 15, 2021. It consists of 395 commits authored by 74 contributors over a 139 day period.

* Git tag: [0.12.0](https://github.com/apache/iceberg/releases/tag/apache-iceberg-0.12.0)
* [0.12.0 source tar.gz](https://www.apache.org/dyn/closer.cgi/iceberg/apache-iceberg-0.12.0/apache-iceberg-0.12.0.tar.gz) -- [signature](https://downloads.apache.org/iceberg/apache-iceberg-0.12.0/apache-iceberg-0.12.0.tar.gz.asc) -- [sha512](https://downloads.apache.org/iceberg/apache-iceberg-0.12.0/apache-iceberg-0.12.0.tar.gz.sha512)
* [0.12.0 Spark 3.x runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-spark3-runtime/0.12.0/iceberg-spark3-runtime-0.12.0.jar)
* [0.12.0 Spark 2.4 runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-spark-runtime/0.12.0/iceberg-spark-runtime-0.12.0.jar)
* [0.12.0 Flink runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-flink-runtime/0.12.0/iceberg-flink-runtime-0.12.0.jar)
* [0.12.0 Hive runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-hive-runtime/0.12.0/iceberg-hive-runtime-0.12.0.jar)

**High-level features:**

* **Core**
    * Allow Iceberg schemas to specify one or more columns as row identifiers [[\#2465](https://github.com/apache/iceberg/pull/2465)]. Note that this is a prerequisite for supporting upserts in Flink.
    * Added JDBC [[\#1870](https://github.com/apache/iceberg/pull/1870)] and DynamoDB [[\#2688](https://github.com/apache/iceberg/pull/2688)] catalog implementations.
    * Added predicate pushdown for partitions and files metadata tables [[\#2358](https://github.com/apache/iceberg/pull/2358), [\#2926](https://github.com/apache/iceberg/pull/2926)].
    * Added a new, more flexible compaction action for Spark that can support different strategies such as bin packing and sorting. [[\#2501](https://github.com/apache/iceberg/pull/2501), [\#2609](https://github.com/apache/iceberg/pull/2609)].
    * Added the ability to upgrade to v2 or create a v2 table using the table property format-version=2  [[\#2887](https://github.com/apache/iceberg/pull/2887)].
    * Added support for nulls in StructLike collections [[\#2929](https://github.com/apache/iceberg/pull/2929)].
    * Added `key_metadata` field to manifest lists for encryption [[\#2675](https://github.com/apache/iceberg/pull/2675)].
* **Flink**
    * Added support for SQL primary keys [[\#2410](https://github.com/apache/iceberg/pull/2410)].
* **Hive**
    * Added the ability to set the catalog at the table level in the Hive Metastore. This makes it possible to write queries that reference tables from multiple catalogs [[\#2129](https://github.com/apache/iceberg/pull/2129)].
    * As a result of [[\#2129](https://github.com/apache/iceberg/pull/2129)], deprecated the configuration property `iceberg.mr.catalog` which was previously used to configure the Iceberg catalog in MapReduce and Hive [[\#2565](https://github.com/apache/iceberg/pull/2565)].
    * Added table-level JVM lock on commits[[\#2547](https://github.com/apache/iceberg/pull/2547)].
    * Added support for Hive's vectorized ORC reader [[\#2613](https://github.com/apache/iceberg/pull/2613)].
* **Spark**
    * Added `SET` and `DROP IDENTIFIER FIELDS` clauses to `ALTER TABLE` so people don't have to look up the DDL [[\#2560](https://github.com/apache/iceberg/pull/2560)].
    * Added support for `ALTER TABLE REPLACE PARTITION FIELD` DDL [[\#2365](https://github.com/apache/iceberg/pull/2365)].
    * Added support for micro-batch streaming reads for structured streaming in Spark3 [[\#2660](https://github.com/apache/iceberg/pull/2660)].
    * Improved the performance of importing a Hive table by not loading all partitions from Hive and instead pushing the partition filter to the Metastore [[\#2777](https://github.com/apache/iceberg/pull/2777)].
    * Added support for `UPDATE` statements in Spark [[\#2193](https://github.com/apache/iceberg/pull/2193), [\#2206](https://github.com/apache/iceberg/pull/2206)].
    * Added support for Spark 3.1 [[\#2512](https://github.com/apache/iceberg/pull/2512)].
    * Added `RemoveReachableFiles` action [[\#2415](https://github.com/apache/iceberg/pull/2415)].
    * Added `add_files` stored procedure [[\#2210](https://github.com/apache/iceberg/pull/2210)].
    * Refactored Actions API and added a new entry point.
    * Added support for Hadoop configuration overrides [[\#2922](https://github.com/apache/iceberg/pull/2922)].
    * Added support for the `TIMESTAMP WITHOUT TIMEZONE` type in Spark [[\#2757](https://github.com/apache/iceberg/pull/2757)].
    * Added validation that files referenced by row-level deletes are not concurrently rewritten [[\#2308](https://github.com/apache/iceberg/pull/2308)].


**Important bug fixes:**

* **Core**
    * Fixed string bucketing with non-BMP characters [[\#2849](https://github.com/apache/iceberg/pull/2849)].
    * Fixed Parquet dictionary filtering with fixed-length byte arrays and decimals [[\#2551](https://github.com/apache/iceberg/pull/2551)].
    * Fixed a problem with the configuration of HiveCatalog [[\#2550](https://github.com/apache/iceberg/pull/2550)].
    * Fixed partition field IDs in table replacement [[\#2906](https://github.com/apache/iceberg/pull/2906)].
* **Hive**
    * Enabled dropping HMS tables even if the metadata on disk gets corrupted [[\#2583](https://github.com/apache/iceberg/pull/2583)].
* **Parquet**
    * Fixed Parquet row group filters when types are promoted from `int` to `long` or from `float` to `double` [[\#2232](https://github.com/apache/iceberg/pull/2232)]
* **Spark**
    * Fixed `MERGE INTO` in Spark when used with `SinglePartition` partitioning [[\#2584](https://github.com/apache/iceberg/pull/2584)].
    * Fixed nested struct pruning in Spark [[\#2877](https://github.com/apache/iceberg/pull/2877)].
    * Fixed NaN handling for float and double metrics [[\#2464](https://github.com/apache/iceberg/pull/2464)].
    * Fixed Kryo serialization for data and delete files [[\#2343](https://github.com/apache/iceberg/pull/2343)].

**Other notable changes:**

* The Iceberg Community [voted to approve](https://mail-archives.apache.org/mod_mbox/iceberg-dev/202107.mbox/%3cCAMwmD1-k1gnShK=wQ0PD88it6cg9mY7Y1hKHjDZ7L-jcDzpyZA@mail.gmail.com%3e) version 2 of the Apache Iceberg Format Specification. The differences between version 1 and 2 of the specification are documented [here](../spec/#version-2).
* Bugfixes and stability improvements for NessieCatalog.
* Improvements and fixes for Iceberg's Python library.
* Added a vectorized reader for Apache Arrow [[\#2286](https://github.com/apache/iceberg/pull/2286)].
* The following Iceberg dependencies were upgraded:
    * Hive 2.3.8 [[\#2110](https://github.com/apache/iceberg/pull/2110)].
    * Avro 1.10.1 [[\#1648](https://github.com/apache/iceberg/pull/1648)].
    * Parquet 1.12.0 [[\#2441](https://github.com/apache/iceberg/pull/2441)].

### 0.11.1

* Git tag: [0.11.1](https://github.com/apache/iceberg/releases/tag/apache-iceberg-0.11.1)
* [0.11.1 source tar.gz](https://www.apache.org/dyn/closer.cgi/iceberg/apache-iceberg-0.11.1/apache-iceberg-0.11.1.tar.gz) -- [signature](https://downloads.apache.org/iceberg/apache-iceberg-0.11.1/apache-iceberg-0.11.1.tar.gz.asc) -- [sha512](https://downloads.apache.org/iceberg/apache-iceberg-0.11.1/apache-iceberg-0.11.1.tar.gz.sha512)
* [0.11.1 Spark 3.0 runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-spark3-runtime/0.11.1/iceberg-spark3-runtime-0.11.1.jar)
* [0.11.1 Spark 2.4 runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-spark-runtime/0.11.1/iceberg-spark-runtime-0.11.1.jar)
* [0.11.1 Flink runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-flink-runtime/0.11.1/iceberg-flink-runtime-0.11.1.jar)
* [0.11.1 Hive runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-hive-runtime/0.11.1/iceberg-hive-runtime-0.11.1.jar)

Important bug fixes:

* [\#2367](https://github.com/apache/iceberg/pull/2367) prohibits deleting data files when tables are dropped if GC is disabled.
* [\#2196](https://github.com/apache/iceberg/pull/2196) fixes data loss after compaction when large files are split into multiple parts and only some parts are combined with other files.
* [\#2232](https://github.com/apache/iceberg/pull/2232) fixes row group filters with promoted types in Parquet.
* [\#2267](https://github.com/apache/iceberg/pull/2267) avoids listing non-Iceberg tables in Glue.
* [\#2254](https://github.com/apache/iceberg/pull/2254) fixes predicate pushdown for Date in Hive.
* [\#2126](https://github.com/apache/iceberg/pull/2126) fixes writing of Date, Decimal, Time, UUID types in Hive.
* [\#2241](https://github.com/apache/iceberg/pull/2241) fixes vectorized ORC reads with metadata columns in Spark.
* [\#2154](https://github.com/apache/iceberg/pull/2154) refreshes the relation cache in DELETE and MERGE operations in Spark.

### 0.11.0

* Git tag: [0.11.0](https://github.com/apache/iceberg/releases/tag/apache-iceberg-0.11.0)
* [0.11.0 source tar.gz](https://www.apache.org/dyn/closer.cgi/iceberg/apache-iceberg-0.11.0/apache-iceberg-0.11.0.tar.gz) -- [signature](https://downloads.apache.org/iceberg/apache-iceberg-0.11.0/apache-iceberg-0.11.0.tar.gz.asc) -- [sha512](https://downloads.apache.org/iceberg/apache-iceberg-0.11.0/apache-iceberg-0.11.0.tar.gz.sha512)
* [0.11.0 Spark 3.0 runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-spark3-runtime/0.11.0/iceberg-spark3-runtime-0.11.0.jar)
* [0.11.0 Spark 2.4 runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-spark-runtime/0.11.0/iceberg-spark-runtime-0.11.0.jar)
* [0.11.0 Flink runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-flink-runtime/0.11.0/iceberg-flink-runtime-0.11.0.jar)
* [0.11.0 Hive runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-hive-runtime/0.11.0/iceberg-hive-runtime-0.11.0.jar)

High-level features:

* **Core API** now supports partition spec and sort order evolution
* **Spark 3** now supports the following SQL extensions:
    * MERGE INTO (experimental)
    * DELETE FROM (experimental)
    * ALTER TABLE ... ADD/DROP PARTITION
    * ALTER TABLE ... WRITE ORDERED BY
    * Invoke stored procedures using CALL
* **Flink** now supports streaming reads, CDC writes (experimental), and filter pushdown
* **AWS module** is added to support better integration with AWS, with [AWS Glue catalog](https://aws.amazon.com/glue/) support and dedicated S3 FileIO implementation
* **Nessie module** is added to support integration with [project Nessie](https://projectnessie.org/)

Important bug fixes:

* [\#1981](https://github.com/apache/iceberg/pull/1981) fixes bug that date and timestamp transforms were producing incorrect values for dates and times before 1970. Before the fix, negative values were incorrectly transformed by date and timestamp transforms to 1 larger than the correct value. For example, `day(1969-12-31 10:00:00)` produced 0 instead of -1. The fix is backwards compatible, which means predicate projection can still work with the incorrectly transformed partitions written using older versions.
* [\#2091](https://github.com/apache/iceberg/pull/2091) fixes `ClassCastException` for type promotion `int` to `long` and `float` to `double` during Parquet vectorized read. Now Arrow vector is created by looking at Parquet file schema instead of Iceberg schema for `int` and `float` fields.
* [\#1998](https://github.com/apache/iceberg/pull/1998) fixes bug in `HiveTableOperation` that `unlock` is not called if new metadata cannot be deleted. Now it is guaranteed that `unlock` is always called for Hive catalog users.
* [\#1979](https://github.com/apache/iceberg/pull/1979) fixes table listing failure in Hadoop catalog when user does not have permission to some tables. Now the tables with no permission are ignored in listing.
* [\#1798](https://github.com/apache/iceberg/pull/1798) fixes scan task failure when encountering duplicate entries of data files. Spark and Flink readers can now ignore duplicated entries in data files for each scan task.
* [\#1785](https://github.com/apache/iceberg/pull/1785) fixes invalidation of metadata tables in `CachingCatalog`. When a table is dropped, all the metadata tables associated with it are also invalidated in the cache.
* [\#1960](https://github.com/apache/iceberg/pull/1960) fixes bug that ORC writer does not read metrics config and always use the default. Now customized metrics config is respected.

Other notable changes:

* NaN counts are now supported in metadata
* Shared catalog properties are added in core library to standardize catalog level configurations
* Spark and Flink now support dynamically loading customized `Catalog` and `FileIO` implementations
* Spark 2 now supports loading tables from other catalogs, like Spark 3
* Spark 3 now supports catalog names in DataFrameReader when using Iceberg as a format
* Flink now uses the number of Iceberg read splits as its job parallelism to improve performance and save resource.
* Hive (experimental) now supports INSERT INTO, case insensitive query, projection pushdown, create DDL with schema and auto type conversion
* ORC now supports reading tinyint, smallint, char, varchar types
* Avro to Iceberg schema conversion now preserves field docs



### 0.10.0

* Git tag: [0.10.0](https://github.com/apache/iceberg/releases/tag/apache-iceberg-0.10.0)
* [0.10.0 source tar.gz](https://www.apache.org/dyn/closer.cgi/iceberg/apache-iceberg-0.10.0/apache-iceberg-0.10.0.tar.gz) -- [signature](https://downloads.apache.org/iceberg/apache-iceberg-0.10.0/apache-iceberg-0.10.0.tar.gz.asc) -- [sha512](https://downloads.apache.org/iceberg/apache-iceberg-0.10.0/apache-iceberg-0.10.0.tar.gz.sha512)
* [0.10.0 Spark 3.0 runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-spark3-runtime/0.10.0/iceberg-spark3-runtime-0.10.0.jar)
* [0.10.0 Spark 2.4 runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-spark-runtime/0.10.0/iceberg-spark-runtime-0.10.0.jar)
* [0.10.0 Flink runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-flink-runtime/0.10.0/iceberg-flink-runtime-0.10.0.jar)
* [0.10.0 Hive runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-hive-runtime/0.10.0/iceberg-hive-runtime-0.10.0.jar)

High-level features:

* **Format v2 support** for building row-level operations (`MERGE INTO`) in processing engines
    * Note: format v2 is not yet finalized and does not have a forward-compatibility guarantee
* **Flink integration** for writing to Iceberg tables and reading from Iceberg tables (reading supports batch mode only)
* **Hive integration** for reading from Iceberg tables, with filter pushdown (experimental; configuration may change)

Important bug fixes:

* [\#1706](https://github.com/apache/iceberg/pull/1706) fixes non-vectorized ORC reads in Spark that incorrectly skipped rows
* [\#1536](https://github.com/apache/iceberg/pull/1536) fixes ORC conversion of `notIn` and `notEqual` to match null values
* [\#1722](https://github.com/apache/iceberg/pull/1722) fixes `Expressions.notNull` returning an `isNull` predicate; API only, method was not used by processing engines
* [\#1736](https://github.com/apache/iceberg/pull/1736) fixes `IllegalArgumentException` in vectorized Spark reads with negative decimal values
* [\#1666](https://github.com/apache/iceberg/pull/1666) fixes file lengths returned by the ORC writer, using compressed size rather than uncompressed size
* [\#1674](https://github.com/apache/iceberg/pull/1674) removes catalog expiration in HiveCatalogs
* [\#1545](https://github.com/apache/iceberg/pull/1545) automatically refreshes tables in Spark when not caching table instances

Other notable changes:

* The `iceberg-hive` module has been renamed to `iceberg-hive-metastore` to avoid confusion
* Spark 3 is based on 3.0.1 that includes the fix for [SPARK-32168](https://issues.apache.org/jira/browse/SPARK-32168)
* Hadoop tables will recover from version hint corruption
* Tables can be configured with a required sort order
* Data file locations can be customized with a dynamically loaded `LocationProvider`
* ORC file imports can apply a name mapping for stats


A more exhaustive list of changes is available under the [0.10.0 release milestone](https://github.com/apache/iceberg/milestone/10?closed=1).

### 0.9.1

* Git tag: [0.9.1](https://github.com/apache/iceberg/releases/tag/apache-iceberg-0.9.1)
* [0.9.1 source tar.gz](https://www.apache.org/dyn/closer.cgi/iceberg/apache-iceberg-0.9.1/apache-iceberg-0.9.1.tar.gz) -- [signature](https://downloads.apache.org/iceberg/apache-iceberg-0.9.1/apache-iceberg-0.9.1.tar.gz.asc) -- [sha512](https://downloads.apache.org/iceberg/apache-iceberg-0.9.1/apache-iceberg-0.9.1.tar.gz.sha512)
* [0.9.1 Spark 3.0 runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-spark3-runtime/0.9.1/iceberg-spark3-runtime-0.9.1.jar)
* [0.9.1 Spark 2.4 runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-spark-runtime/0.9.1/iceberg-spark-runtime-0.9.1.jar)

### 0.9.0

* Git tag: [0.9.0](https://github.com/apache/iceberg/releases/tag/apache-iceberg-0.9.0)
* [0.9.0 source tar.gz](https://www.apache.org/dyn/closer.cgi/iceberg/apache-iceberg-0.9.0/apache-iceberg-0.9.0.tar.gz) -- [signature](https://downloads.apache.org/iceberg/apache-iceberg-0.9.0/apache-iceberg-0.9.0.tar.gz.asc) -- [sha512](https://downloads.apache.org/iceberg/apache-iceberg-0.9.0/apache-iceberg-0.9.0.tar.gz.sha512)
* [0.9.0 Spark 3.0 runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-spark3-runtime/0.9.0/iceberg-spark3-runtime-0.9.0.jar)
* [0.9.0 Spark 2.4 runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-spark-runtime/0.9.0/iceberg-spark-runtime-0.9.0.jar)

### 0.8.0

* Git tag: [apache-iceberg-0.8.0-incubating](https://github.com/apache/iceberg/releases/tag/apache-iceberg-0.8.0-incubating)
* [0.8.0-incubating source tar.gz](https://www.apache.org/dyn/closer.cgi/incubator/iceberg/apache-iceberg-0.8.0-incubating/apache-iceberg-0.8.0-incubating.tar.gz) -- [signature](https://downloads.apache.org/incubator/iceberg/apache-iceberg-0.8.0-incubating/apache-iceberg-0.8.0-incubating.tar.gz.asc) -- [sha512](https://downloads.apache.org/incubator/iceberg/apache-iceberg-0.8.0-incubating/apache-iceberg-0.8.0-incubating.tar.gz.sha512)
* [0.8.0-incubating Spark 2.4 runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-spark-runtime/0.8.0-incubating/iceberg-spark-runtime-0.8.0-incubating.jar)


### 0.7.0

* Git tag: [apache-iceberg-0.7.0-incubating](https://github.com/apache/iceberg/releases/tag/apache-iceberg-0.7.0-incubating)
* [0.7.0-incubating source tar.gz](https://www.apache.org/dyn/closer.cgi/incubator/iceberg/apache-iceberg-0.7.0-incubating/apache-iceberg-0.7.0-incubating.tar.gz) -- [signature](https://dist.apache.org/repos/dist/release/incubator/iceberg/apache-iceberg-0.7.0-incubating/apache-iceberg-0.7.0-incubating.tar.gz.asc) -- [sha512](https://dist.apache.org/repos/dist/release/incubator/iceberg/apache-iceberg-0.7.0-incubating/apache-iceberg-0.7.0-incubating.tar.gz.sha512)
* [0.7.0-incubating Spark 2.4 runtime Jar](https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-spark-runtime/0.7.0-incubating/iceberg-spark-runtime-0.7.0-incubating.jar)

