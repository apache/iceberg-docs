---
title: "Multi-Engine Support"
bookHidden: true
url: multi-engine-support
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

# Multi-Engine Support

Multi-engine support is a core tenant of Apache Iceberg.
The community continuously improves Iceberg core library components to enable integrations with different compute engines that power analytics, business intelligence, machine learning, etc.
Support of [Apache Spark](../../../docs/spark-configuration), [Apache Flink](../../../docs/flink) and [Apache Hive](../../../docs/hive) are provided inside the Iceberg main repository.

## Multi-Version Support

Engines maintained within the Iceberg repository have multi-version support.
This means each new version of an engine that introduces backwards incompatible upgrade has its dedicated integration codebase and release artifacts.
For example, the code for Iceberg Spark 3.1 integration is under `/spark/v3.1`, and for Iceberg Spark 3.2 integration is under `/spark/v3.2`,
Different artifacts (`iceberg-spark-3.1_2.12` and `iceberg-spark-3.2_2.12`) are released for users to consume.
By doing this, changes across versions are isolated. New features in Iceberg could be developed against the latest features of an engine without breaking support of old APIs in past engine versions.

## Engine Version Lifecycle

Each engine version undergoes the following lifecycle stages:

1. **Beta**: a new engine version is supported, but still in the experimental stage. Maybe the engine version itself is still in preview (e.g. Spark `3.0.0-preview`), or the engine does not yet have full feature compatibility compared to old versions yet. This stage allows Iceberg to release an engine version support without the need to wait for feature parity, shortening the release time.
2. **Maintained**: an engine version is actively maintained by the community. Users can expect parity for most features across all the maintained versions. If a feature has to leverage some new engine functionalities that older versions don't have, then feature parity across maintained versions is not guaranteed.
3. **Deprecated**: an engine version is no longer actively maintained. People who are still interested in the version can backport any necessary feature or bug fix from newer versions, but the community will not spend effort in achieving feature parity. Iceberg recommends users to move towards a newer version. Contributions to a deprecated version is expected to diminish over time, so that eventually no change is added to a deprecated version.
4. **End-of-life**: a vote can be initiated in the community to fully remove a deprecated version out of the Iceberg repository to mark as its end of life.

## Current Engine Version Lifecycle Status

### Apache Spark

| Version    | Lifecycle Stage    |
| ---------- | ------------------ |
| 2.4        | Deprecated         | 
| 3.0        | Maintained         | 
| 3.1        | Maintained         |
| 3.2        | Beta               |

### Apache Flink

Based on the guideline of the Flink community, only the latest 2 minor versions are actively maintained.
Users should continuously upgrade their Flink version to stay up-to-date.

| Version    | Lifecycle Stage   |
| ---------- | ----------------- | 
| 1.12       | Deprecated        | 
| 1.13       | Maintained        | 
| 1.14       | Maintained        | 
### Apache Hive

| Version                         | Lifecycle Stage   |
| ------------------------------- | ----------------- | 
| 2 (recommended >= 2.3)          | Maintained        |
| 3                               | Maintained        | 

## Developer Guide

### Maintaining existing engine versions

Iceberg recommends the following for developers who are maintaining existing engine versions:

1. New features should always be prioritized first in the latest version, which is either a maintained or beta version.
2. For features that could be backported, contributors are encouraged to either perform backports to all maintained versions, or at least create some issues to track the backport.
3. If the change is small enough, updating all versions in a single PR is acceptable. Otherwise, using separated PRs for each version is recommended.

### Supporting new engines

Iceberg recommends new engines to build support by importing the Iceberg libraries to the engine's project.
This allows the Iceberg support to evolve with the engine.
Projects such as [Trino](https://trino.io/docs/current/connector/iceberg.html) and [Presto](https://prestodb.io/docs/current/connector/iceberg.html) are good examples of such support strategy.

In this approach, an Iceberg version upgrade is needed for an engine to consume new Iceberg features.
To facilitate engine development against unreleased Iceberg features, a daily snapshot is published in the [Apache snapshot repository](https://repository.apache.org/content/repositories/snapshots/org/apache/iceberg/).

If bringing an engine directly to the Iceberg main repository is needed, please raise a discussion thread in the [Iceberg community](../community).