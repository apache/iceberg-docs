<!--
  - Licensed to the Apache Software Foundation (ASF) under one
  - or more contributor license agreements.  See the NOTICE file
  - distributed with this work for additional information
  - regarding copyright ownership.  The ASF licenses this file
  - to you under the Apache License, Version 2.0 (the
  - "License"); you may not use this file except in compliance
  - with the License.  You may obtain a copy of the License at
  -
  -   http://www.apache.org/licenses/LICENSE-2.0
  -
  - Unless required by applicable law or agreed to in writing,
  - software distributed under the License is distributed on an
  - "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  - KIND, either express or implied.  See the License for the
  - specific language governing permissions and limitations
  - under the License.
  -->

# Apache Iceberg Documentation Site

This repository contains the documentation for [Apache Iceberg](https://github.com/apache/iceberg).
It's built with [Hugo](https://gohugo.io/) and hosted at https://iceberg.apache.org.

To start the site locally, clone this repository and run the following.
```
hugo serve
```

# Versioned Docs

The way versioning works is each instance of the deployment workflow deploys to a directory in
the gh-pages branch that's named after the branch name. For example, a commit to the `0.12.1` branch
triggers the deployment workflow which builds the site and pushes it to the 0.12.1 directory in the gh-pages
branch. If no directory exists, the deployment workflow creates it.

In the root of the gh-pages branch, there is an index.html with a single meta tag that redirects to the
site deployed from the `latest` branch.