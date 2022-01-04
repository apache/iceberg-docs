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

# Asciinema Recordings

This directory contains some helper scripts to generate asciinema recordings of terminal commands.
To generate a new asciinema recording, you can use the `Cast` class in [generate_asciinema_cast.py](generate_asciinema_cast.py).

```py
from generate_asciinema_cast import Cast

Cast(sequence).generate_cast(PS1="spark-sql> ").save("output/schema_evolution.cast")
```

The `sequence` object is a list of tuples that each contain two string elements. The first string element
is the user input, and the second is the terminal output. For example, if you wanted to create a cast showing
the printing of a text file, you would create a sequence like this.

```py
from generate_aciinema_cast import Cast

sequence = [
    (
        "touch file.txt",
        ""
    ),
    (
        'echo "Hello World!" > file.txt',
        ""
    ),
    (
        "cat file.txt",
        "Hello World!"
    )
]

Cast(sequence).generate_cast(PS1="$ ").save("output/hello_world.cast")
```

# Adding a Cast to The Documentation Site

Once you have a cast, you can add it to a location in the documentation site. To do that,
copy the cast over to the static/asciinema directory. Next, add the following where you want
the asciinema recording to be displayed.

```html
<div id="an-example-cast"></div>
<script>
    AsciinemaPlayer.create('{{ .Site.BaseURL }}/asciinema/hello_world.cast', document.getElementById('an-example-cast'), {
        loop: true,
        autoPlay: true,
        theme: "monokai",
    });
</script>
```

To see all of the options you can use to customize how the cast is displayed, check out the [asciinema-player](https://github.com/asciinema/asciinema-player) repo.