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
documentation sites are completely self-contained in the `./landing-page` and `./docs` directories, respectively.
The Javadocs are in the `./javadoc` directory.

## Relationship to the Iceberg Repository

All markdown pages that are specific to an Iceberg version are maintained in the iceberg repository. All pages common across all version
releases are kept here in the iceberg-docs repo. A few exceptions are the markdown files that can be found in the `format` folder in
the iceberg repository and contains markdown files that are copied into `./landing-page/content/common/`.

`apache/iceberg`
- The `docs` folder in the [Iceberg repository](https://github.com/apache/iceberg) contains all the markdown docs used by the **versioned** docs site.
- The `format` folder contains some items that are common across all versions, such as the Iceberg format specification.

`apache/iceberg-docs`
- The `docs/content/docs` folder is the target folder when copying the docs over during a version release
- The `landing-page/content/common` folder is where you can find the common markdown files shared across all versions

During each new release, the release manager will:
1. Copy the contents under `format` in the iceberg repo to `./landing-page/content/common/` in the `main` branch
2. Create a branch in this repo from main named for the release version
3. Copy the contents under `docs` in the iceberg repo to `./docs/content/docs` in the **release** branch
4. Generate the javadocs for the release and copy them into the `javadoc` directory in the release branch
5. Update the latest branch HEAD to point to the release branch HEAD

# How to Contribute

## Submitting Pull Requests

Changes to the markdown contents for **version** specific pages should be submitted directly in the Iceberg repository.

Changes to the markdown contents for common pages should be submitted to this repository against the `main` branch.

Changes to the website appearance (e.g. HTML, CSS changes) should be submitted to this repository against the `main` branch.

Changes to the documentation of old Iceberg versions should be submitted to this repository against the specific version branch.

In summary, you can open a PR against where you find the related markdown file. With the exception of `spec.md`, there are no duplicate
markdown files between the `master` branch in the iceberg repo and the `main` branch in the iceberg-docs repo. For changes to `spec.md`,
PRs should be opened against the iceberg repo, not the iceberg-docs repo.

## Reporting Issues

All issues related to the doc website should still be submitted to the [Iceberg repository](https://github.com/apache/iceberg).
The GitHub Issues feature of this repository is disabled.

## Running Locally

Clone this repository to run the website locally:
```shell
git clone git@github.com:apache/iceberg-docs.git
cd iceberg-docs
```

To start the landing page site locally, run:
```shell
(cd landing-page && hugo serve)
```

To start the documentation site locally, run:
```shell
(cd docs && hugo serve)
```

If you would like to see how the latest website looks based on the documentation in the Iceberg repository, you can copy docs to this repository by:
```shell
rm -rf docs/content/docs
cp -r <path to iceberg repo>/docs docs/content/docs
cp -r <path to iceberg repo>/format/* landing-page/content/common/
```

## Scanning For Broken Links

If you'd like to scan for broken links, one available tool is linkcheck that can be found [here](https://github.com/filiph/linkcheck).

# How the Website is Deployed

**Note**: If you are a release manager looking to release a new version of the website as part of an Iceberg release,
please refer to the [Documentation Release](https://iceberg.apache.org/how-to-release/#documentation-release) section
of the **How to Release** page.

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

### Latest Docs
In [./docs/redirect/index.html](./docs/redirect/index.html), a redirect meta tag exists to forward `/docs` 
and `/latest` to `/docs/latest`.

## `asf-site` Branch Structure

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

## Testing Both Sites Locally

In some cases, it's useful to test both the landing-page site and the docs site locally. Especially in situations
where you need to test relative links between the two sites. This can be achieved by building both sites with custom
`baseURL` and `publishDir` values passed to the CLI. You can then run the site with any local live server, such as the
[Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) extension for VSCode.

First, change into the `landing-page` directory and build the site. Use `-b` and `-d` to set `baseURL` and `publishDir`, respectively.
```
cd landing-page
hugo -b http://localhost:5500/ -d ../public
```

Next, change into the `docs` directory and do the same thing. Remember that the docs-site is deployed to a `docs/<VERSION>` url, relative to the landing-page site. Since the landing-page was deployed to `../publish` in the example
above, the example below usees `../public/docs/latest` to deploy a `latest` version docs-site.
```
cd ../docs
hugo -b http://localhost:5500/docs/latest/ -d ../public/docs/latest
```

You should then have both sites deployed to the `public` directory which you can launch using your live server.

**Note:** The examples above use port `5500`. Be sure to change the port number if your local live server uses a different port.