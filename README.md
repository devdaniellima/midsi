# MIDSI Project

### Source code of the Midsi inference engine with case study and benchmark

Solution for data discovery in projects applicable to the Semantic Web, enabling the loading of ontologies and inference of results using the WSML language.

SableCC is used for translators for the WSML language.

Prolog is used as an engine to perform inferences.

Pyswip is used for connection between python and prolog resources.

### Requirements:

- SwiProlog
- Python 3.\*
  - pyswip

### Installing project dependencies

Linux Debian-based systems:

    sudo ./install.sh

Other linux systems install the following packages:

    default_jre
    python3
    swi-prolog #swi-prolog ou pl
    pip pyswip

MacOS (Intel or M1):

    brew install swi-prolog
    pip3 install pyswip

### Benchmark

- To run and view the results:

      cd benchmark
      python3 benchmark.py

- Additional settings to the benchmark can be changed in **benchmark.conf**.

- A **log** folder will be created containing the result of the benchmark.

### Using Midsi as a service

Just enter the `./service` folder and start the `midsi-service.py` server. The configuration of ip and port is in the file `config.py`, to use another address just change it.

    cd ./service
    python3 midsi-service.py

To make it easier to use, the commands we can use on our server were centralized in `midsi-client.py`.

- Loading an ontology:

    ```
    python3 midsi-client.py --ontology ../wsmlcodes/ont1-ShipmentOntology/ShipmentOntology.wsml
    ```

- Running a query:

    ```
    python3 midsi-client.py --query "cityIsOnContinent(?x,?y)"
    ```

- Executing a query from a file:

    ```
    python --queryFile ../wsmlcodes/ont1-ShipmentOntology/query1-allPackageStatus.wsml
    ```

- Closing the server (can be done by closing `midsi-service.py` directly):

    ```
    python3 midsi-client.py --exit
    ```

### WSML to VSCode

We created an extension for VSCode that provides syntax highlighting and bracket matching for WSML files. **It also has integrated controls for the use of the Midsi client / server previously exposed**.

It can be downloaded directly from the VSCode marktplace, searching for WSML. See more at [https://github.com/devdaniellima/wsml-vscode](https://github.com/devdaniellima/wsml-vscode).