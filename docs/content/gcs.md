---
title: "GCS"
url: gcs
menu:
    main:
        parent: Integrations
        identifier: gcs_integration
        weight: 0
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

# Iceberg GSC Integration

The purpose of the Google Cloud Storage (GCS) integration with Apache Iceberg is to allow Iceberg tables to read from and write to GCS. This means that data stored in GCS can be queried using Iceberg's powerful table formats, and the results of those queries can be written back to GCS. This integration makes it possible to use Iceberg's features, such as schema evolution and efficient data scanning, with data stored in GCS. In addition, this integration can also enable users to build cloud-native data lakes on Google Cloud Platform using Apache Iceberg as the table format.

## Prerequisites

Before setting up the GCS integration with Apache Iceberg, ensure that you have:

* An active Google Cloud account with permissions to create and manage GCS buckets.
* Apache Iceberg has been installed in the working environment.
* Apache Spark is installed as well, for Apache Iceberg utilizes it as a computation engine.
* Required dependencies, such as `iceberg-spark-runtime` and `gcs-connector` JAR files, are available in the system.

## Setup and Configuration

Step 1: Creating a GCS Bucket
In the Google Cloud Console, create a bucket where your Iceberg tables will reside.

Step 2: Installing the Iceberg JAR
The JAR for Apache Iceberg (specifically, iceberg-spark3-runtime) needs to be added to your Spark environment:

spark-shell --packages org.apache.iceberg:iceberg-spark-runtime-3.2_2.12:1.3.0
Step 3: Configuring Spark to Use GCS
Spark should be configured to point to the GCS bucket. The command to start the Spark shell in this case looks as follows:

spark-shell --conf spark.sql.warehouse.dir=gs://[BUCKET_NAME]/spark-warehouse --jars /path/to/iceberg-spark-runtime.jar
Replace [BUCKET_NAME] with the name of your GCS bucket.



* What is the purpose of the GCS integration with Apache Iceberg? _/
* What are the prerequisites for using GCS with Apache Iceberg? _/
* What are the steps to set up and configure the GCS integration?
* Are there any specific usage examples or code snippets that should be included?
* Are there any known issues or limitations with the GCS integration?
* Is there any additional information that users should know about the GCS integration?
  