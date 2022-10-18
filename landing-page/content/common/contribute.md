---
title: "Contribute"
url: contribute
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
# Contributing

In this page, you will find some guidelines on contributing to Apache Iceberg. Please keep in mind that none of
these are hard rules and they're meant as a collection of helpful suggestions to make contributing as seamless of an
experience as possible.

If you are thinking of contributing but first would like to discuss the change you wish to make, we welcome you to
head over to the [Community](https://iceberg.apache.org/community/) page on the official Iceberg documentation site
to find a number of ways to connect with the community, including slack and our mailing lists. Of course, always feel
free to just open a [new issue](https://github.com/apache/iceberg/issues/new) in the GitHub repo. You can also check the following for a [good first issue](https://github.com/apache/iceberg/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22).

The Iceberg Project is hosted on GitHub at <https://github.com/apache/iceberg>.

## Pull Request Process

The Iceberg community prefers to receive contributions as [Github pull requests][github-pr-docs].

[View open pull requests][iceberg-prs]


[iceberg-prs]: https://github.com/apache/iceberg/pulls
[github-pr-docs]: https://help.github.com/articles/about-pull-requests/

* PRs are automatically labeled based on the content by our github-actions labeling action
* It's helpful to include a prefix in the summary that provides context to PR reviewers, such as `Build:`, `Docs:`, `Spark:`, `Flink:`, `Core:`, `API:`
* If a PR is related to an issue, adding `Closes #1234` in the PR description will automatically close the issue and helps keep the project clean
* If a PR is posted for visibility and isn't necessarily ready for review or merging, be sure to convert the PR to a draft


## Building the Project Locally

Iceberg is built using Gradle with Java 8 or Java 11.

* To invoke a build and run tests: `./gradlew build`
* To skip tests: `./gradlew build -x test -x integrationTest`
* To fix code style: `./gradlew spotlessApply`
* To build particular Spark/Flink Versions: `./gradlew build -DsparkVersions=3.2,3.3 -DflinkVersions=1.14`

Iceberg table support is organized in library modules:

* `iceberg-common` contains utility classes used in other modules
* `iceberg-api` contains the public Iceberg API
* `iceberg-core` contains implementations of the Iceberg API and support for Avro data files, **this is what processing engines should depend on**
* `iceberg-parquet` is an optional module for working with tables backed by Parquet files
* `iceberg-arrow` is an optional module for reading Parquet into Arrow memory
* `iceberg-orc` is an optional module for working with tables backed by ORC files
* `iceberg-hive-metastore` is an implementation of Iceberg tables backed by the Hive metastore Thrift client
* `iceberg-data` is an optional module for working with tables directly from JVM applications

This project Iceberg also has modules for adding Iceberg support to processing engines:

* `iceberg-spark2` is an implementation of Spark's Datasource V2 API in 2.4 for Iceberg (use iceberg-spark-runtime for a shaded version)
* `iceberg-spark3` is an implementation of Spark's Datasource V2 API in 3.0 for Iceberg (use iceberg-spark3-runtime for a shaded version)
* `iceberg-flink` contains classes for integrating with Apache Flink (use iceberg-flink-runtime for a shaded version)
* `iceberg-mr` contains an InputFormat and other classes for integrating with Apache Hive
* `iceberg-pig` is an implementation of Pig's LoadFunc API for Iceberg

## Setting up IDE and Code Style

### Configuring Code Formatter for Eclipse/IntelliJ

Follow the instructions for [Eclipse](https://github.com/google/google-java-format#eclipse) or
[IntelliJ](https://github.com/google/google-java-format#intellij-android-studio-and-other-jetbrains-ides) to install the **google-java-format** plugin (note the required manual actions for IntelliJ).


### Configuring Copyright for IntelliJ IDEA

Every file needs to include the Apache license as a header. This can be automated in IntelliJ by
adding a Copyright profile:

1. In the **Settings/Preferences** dialog go to **Editor → Copyright → Copyright Profiles**.
2. Add a new profile and name it **Apache**.
3. Add the following text as the license text:

   ```
   Licensed to the Apache Software Foundation (ASF) under one
   or more contributor license agreements.  See the NOTICE file
   distributed with this work for additional information
   regarding copyright ownership.  The ASF licenses this file
   to you under the Apache License, Version 2.0 (the
   "License"); you may not use this file except in compliance
   with the License.  You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing,
   software distributed under the License is distributed on an
   "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
   KIND, either express or implied.  See the License for the
   specific language governing permissions and limitations
   under the License.
   ```
4. Go to **Editor → Copyright** and choose the **Apache** profile as the default profile for this
   project.
5. Click **Apply**.

## Iceberg Code Contribution Guidelines

### Style

For Python, please use the tox command `tox -e format` to apply autoformatting to the project.

Java code adheres to the [Google style](https://google.github.io/styleguide/javaguide.html), which will be verified via `./gradlew spotlessCheck` during builds.
In order to automatically fix Java code style issues, please use `./gradlew spotlessApply`.

**NOTE**: The **google-java-format** plugin will always use the latest version of the **google-java-format**. However, `spotless` itself is configured to use **google-java-format** 1.7
since that version is compatible with JDK 8. When formatting the code in the IDE, there is a slight chance that it will produce slightly different results. In such a case please run `./gradlew spotlessApply`
as CI will check the style against **google-java-format** 1.7.

### Copyright

Each file must include the Apache license information as a header.

```
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
```

### Configuring Copyright for IntelliJ IDEA

Every file needs to include the Apache license as a header. This can be automated in IntelliJ by
adding a Copyright profile:

1. In the **Settings/Preferences** dialog go to **Editor → Copyright → Copyright Profiles**.
2. Add a new profile and name it **Apache**.
3. Add the following text as the license text:

   ```
   Licensed to the Apache Software Foundation (ASF) under one
   or more contributor license agreements.  See the NOTICE file
   distributed with this work for additional information
   regarding copyright ownership.  The ASF licenses this file
   to you under the Apache License, Version 2.0 (the
   "License"); you may not use this file except in compliance
   with the License.  You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing,
   software distributed under the License is distributed on an
   "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
   KIND, either express or implied.  See the License for the
   specific language governing permissions and limitations
   under the License.
   ```
4. Go to **Editor → Copyright** and choose the **Apache** profile as the default profile for this
   project.
5. Click **Apply**.

### Java style guidelines

#### Method naming

1. Make method names as short as possible, while being clear. Omit needless words.
2. Avoid `get` in method names, unless an object must be a Java bean.
    * In most cases, replace `get` with a more specific verb that describes what is happening in the method, like `find` or `fetch`.
    * If there isn't a more specific verb or the method is a getter, omit `get` because it isn't helpful to readers and makes method names longer.
3. Where possible, use words and conjugations that form correct sentences in English when read
    * For example, `Transform.preservesOrder()` reads correctly in an if statement: `if (transform.preservesOrder()) { ... }`

#### Boolean arguments

Avoid boolean arguments to methods that are not `private` to avoid confusing invocations like `sendMessage(false)`. It is better to create two methods with names and behavior, even if both are implemented by one internal method.

```java
  // prefer exposing suppressFailure in method names
  public void sendMessageIgnoreFailure() {
    sendMessageInternal(true);
  }

  public void sendMessage() {
    sendMessageInternal(false);
  }

  private void sendMessageInternal(boolean suppressFailure) {
    ...
  }
```

When passing boolean arguments to existing or external methods, use inline comments to help the reader understand actions without an IDE.

```java
  // BAD: it is not clear what false controls
  dropTable(identifier, false);

  // GOOD: these uses of dropTable are clear to the reader
  dropTable(identifier, true /* purge data */);
  dropTable(identifier, purge);
```

#### Config naming

1. Use `-` to link words in one concept
    * For example, preferred convection `access-key-id` rather than `access.key.id`
2. Use `.` to create a hierarchy of config groups
    * For example, `s3` in `s3.access-key-id`, `s3.secret-access-key`

## Running Benchmarks
Some PRs/changesets might require running benchmarks to determine whether they are affecting the baseline performance. Currently there is 
no "push a single button to get a performance comparison" solution available, therefore one has to run JMH performance tests on their local machine and
post the results on the PR.

See [Benchmarks](../benchmarks) for a summary of available benchmarks and how to run them.

## Website and Documentation Updates

Currently, there is an [iceberg-docs](https://github.com/apache/iceberg-docs) repository
which contains the HTML/CSS and other files needed for the [Iceberg website](https://iceberg.apache.org/).
The [docs folder](https://github.com/apache/iceberg/tree/master/docs) in the Iceberg repository contains 
the markdown content for the documentation site. All markdown changes should still be made
to this repository.

### Submitting Pull Requests

Changes to the markdown contents should be submitted directly to this repository.

Changes to the website appearance (e.g. HTML, CSS changes) should be submitted to the [iceberg-docs repository](https://github.com/apache/iceberg-docs) against the `main` branch.

Changes to the documentation of old Iceberg versions should be submitted to the [iceberg-docs repository](https://github.com/apache/iceberg-docs) against the specific version branch.

### Reporting Issues

All issues related to the doc website should still be submitted to the [Iceberg repository](https://github.com/apache/iceberg).
The GitHub Issues feature of the [iceberg-docs repository](https://github.com/apache/iceberg-docs) is disabled.

### Running Locally

Clone the [iceberg-docs](https://github.com/apache/iceberg-docs) repository to run the website locally:
```shell
git clone git@github.com:apache/iceberg-docs.git
cd iceberg-docs
```

To start the landing page site locally, run:
```shell
cd landing-page && hugo serve
```

To start the documentation site locally, run:
```shell
cd docs && hugo serve
```

If you would like to see how the latest website looks based on the documentation in the Iceberg repository, you can copy docs to the iceberg-docs repository by:
```shell
rm -rf docs/content/docs
rm -rf landing-page/content/common
cp -r <path to iceberg repo>/docs/versioned docs/content/docs
cp -r <path to iceberg repo>/docs/common landing-page/content/common
```
