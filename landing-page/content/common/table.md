---
title: "Iceberg Tables"
url: concepts/table
disableSidebar: true
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

# Iceberg Tables

## Overview

Tables are the central element in Iceberg. A table is a dataset with a common set of features (fields or columns) for each record (row). In addition to data files, tables contain a wealth of metadata information that enables many of Iceberg’s features such as schema evolution, fast query planning, snapshots for time travel, logical partitioning, and properties for optimizing table layout. Table properties are used to fine-tune each feature and allow you to control things such as the size when combining data input splits or the compression codec used when writing files.

## Schema

The schema of a table defines the elements contained in a single row. Each field in a schema can be optional or required and has an associated ID, name, and type. Schemas can also include aliases for certain fields. As the schema of an Iceberg table is changed, the new schema is given a unique ID. Past schemas are preserved in the table metadata and allow schemas to be restored when tables are rolled back.

## Sort Order

A table’s sort order is a special property that defines which fields the table’s records should be ordered by when writing data files.  

## Snapshots

Changes in table state are captured as snapshots. Snapshots allow you to query historical versions of a table and fully roll back using metadata-only operations. In essence, a snapshot is a reference to a specific metadata file, and changing the table state is controlled by changing this reference. This reference is maintained by the Iceberg catalog and ties a table reference to its current snapshot.

## Anatomy of a Table

{{< figure src="/img/iceberg-table-structure.png" alt="button" >}}
Iceberg tables are composed of five types of files: metadata, manifest lists, manifests, data and delete files. All files in an Iceberg table are immutable; making a change to an iceberg table involves adding to or removing from the set of files which make up the table and reflecting those changes in a new metadata JSON file for the table. When reading and writing Iceberg tables, you don’t need to be aware of these internal details, but they’re used the compute engines to expose all of Iceberg’s powerful features.

## Metadata JSON ([spec](../../spec/#table-metadata))

The top level object, simply referred to as the table metadata file, is a single json file that includes high level information on various aspects of a table such as current and past schemas, partitioning, and configured sort-orders. Table properties are also included in the table metadata file. When changes are made to a table, a new metadata file is created and the table’s entry in the Iceberg catalog is updated to point to this new file.

The metadata file also contains a reference to all of the table’s snapshots which provides the location of each snapshots manifest list.

## Manifest Lists ([spec](../../spec/#manifest-lists))

Each table snapshot has a corresponding manifest list. The manifest list serves as a high-level index on the data for a particular snapshot. This file contains references to all of the manifest files that are part of the snapshot along with relevant summary metrics.

## Manifests ([spec](../../spec/#manifests))

A manifest is an Avro file that lists the data files or delete files that are part of the table along with rich metadata for each file. This metadata allows for powerful query planning and optimizations.

## Data Files

These are the files that actually store the records for the table. Iceberg supports multiple formats for data files including parquet, orc, and avro.

## Delete Files ([spec](../../spec/#delete-formats))

Delete files contain information about specific records that should be excluded from the table; this supports merge-on-read functionality.

## Iceberg vs. Hive-Like Tables

There are a number of fundamental differences between the design of Iceberg tables and traditional Hive-like tables. Unlike Iceberg, Hive-like tables track data at the directory level instead of the file level. This makes atomic transactions difficult since any file written to the directory is included in query results, even if the write job ultimately fails. Furthermore, serious performance and scalability issues are caused by expensive list operations and the overall metadata design causes Hive-like tables to be rigid and resistant to partitioning and schema evolution. When using eventually consistent cloud-backed storage systems such as AWS S3, even more serious problems occur with traditional Hive tables such as missing data.

Iceberg’s rich metadata, atomicity, and cloud-first design provide strong correctness and performance guarantees. Since data is tracked at the file level, query planning is very performant and not bogged down by expensive operations against the storage layer. Iceberg tables allow intuitive schema updates without having to restage any data and the table’s partitioning can evolve naturally as needed while utilizing powerful features such as hidden partitioning. Best of all, Iceberg is an open table format with a growing number of compute and query engines supporting it.
