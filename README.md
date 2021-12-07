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