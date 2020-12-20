# MIDSI Project

### Source code of the Midsi inference engine with case study and benchmark

Solution for data discovery in projects applicable to the Semantic Web, enabling the loading of ontologies and inference of results using the WSML language.

### Requirements:

- SwiProlog
- Python 3.\*
  - pyswip

### Installing project dependencies

Debian-based systems:

    sudo ./install.sh

Other systems install the following packages:

    default_jre
    python3
    swi-prolog #swi-prolog ou pl
    pip pyswip

### Benchmark

- To run and view the results:

      cd benchmark
      python3 benchmark.py
    
- Additional settings to the benchmark can be changed in **benchmark.conf**.

- A **log** folder will be created containing the result of the benchmark.
