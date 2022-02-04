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

# Structure

The Iceberg documentation site is actually constructed from two hugo sites. The first, is the landing page. The second site, 
is the documentation site which contains the full Iceberg documentation, including the javadoc. The landing page and
documentation sites are completely self-contained in the `./landing-page` and `./docs` directories, respectively. The Javadocs are in the `./javadoc` directory.

# How to Contribute

## Submitting Pull Requests

All pull requests to update the latest documentations should be submitted to the [Iceberg repository](https://github.com/apache/iceberg).
When Iceberg publishes a new release, the release manager copies all the documentation to this repository and cut a new version branch.

Changes to the landing page should be submitted to this repository against the `main` branch.

Changes to the documentation of old Iceberg versions should be submitted to this repository against the specific version branch.

## Reporting Issues

All issues related to documentation and website should still be submitted to the [Iceberg repository](https://github.com/apache/iceberg).

## Running Locally

To start the landing page site locally, clone this repository and run the following.
```shell
git clone git@github.com:apache/iceberg-docs.git
cd landing-page && hugo serve
```

To start the documentation site locally, clone this repository and run the following.
```shell
git clone git@github.com:apache/iceberg-docs.git
git submodule update --init
cd docs && hugo serve
```

## Viewing Latest Website

If you would like to see how the latest website looks based on the documentation in the Iceberg repository, you can copy docs to this repository by:
```shell
cp -r iceberg/documentation/* iceberg-docs/docs/content/docs
```

## Scanning For Broken Links

If you'd like to scan for broken links, one available tool is linkcheck that can be found [here](https://github.com/filiph/linkcheck).


# How the Website is Deployed

## Landing Page Deployment

The landing page site is automatically deployed to the root of the `asf-site` branch by the `deploy-landing-page`
job in the [deployment workflow](./.github/workflows/deploy.yml). There is only a single version of the landing
page site, and the `deploy-landing-page` job only runs on commits to the `main` branch.

## Docs Deployment

The docs site is automatically deployed to the `docs` directory in the asf-site branch, into a sub-directory
named after the branch where the commit occured. This is performed by the `deploy-docs` job in the
[deployment workflow](./.github/workflows/deploy.yml). The job deploys the docs site on commits to any branch
**except** `main`. A branch is maintained for each Iceberg version. If the job runs and the directory does not
yet exist in the `asf-site` branch, it will be created.

Additionally, the contents of the `javadoc` directory is deployed to a `javadoc/<branch_name>` directory in
the `asf-site` branch.

#### Latest Docs
In [./docs/redirect/index.html](./docs/redirect/index.html), a redirect meta tag exists to forward `/docs` 
and `/latest` to `/docs/latest`.

# `asf-site` Branch Structure

The `asf-site` branch structure is the following:
```
.
├── docs
│   ├── 0.12.1
│   │   └── <Full Docs Site @0.12.1>
│   ├── latest
│   │   └── <Full Docs Site @latest>
│   └── index.html  <-- Includes a redirect to 0.12.1 which is the latest version
├── javadoc
│   ├── 0.12.1
│   │   └── <Full javadoc site @0.12.1>
│   └── latest
│       └── <Full javadoc Site @latest>
└── <Full Landing Page Site>
```

A non-`main` branch commit deploys the docs site into a new sub-directory in the
`asf-site` branch's `docs` directory, as well as copies the javadoc directory into a new sub-directory
in the `asf-site` branch's `javadoc` directory.

A `main` branch commit deploys the landing page site **only** and overwrites the landing page site at
the root of the `asf-site` branch.

## Redirects

Redirects within one of the two sites can easily be done using the `aliases` keyword in the YAML Front Matter.
You can read more about this Hugo URL Management feature [here](https://gohugo.io/content-management/urls/#yaml-front-matter).

For root level redirects that are outside of both sites, the `./redirects` directory contains pages with redirect `meta` tags.
These are all deployed at the root level of the `asf-site` branch by the `Deploy redirects` step in the [deployment workflow](./.github/workflows/deploy.yml).