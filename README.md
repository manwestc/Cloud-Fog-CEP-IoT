[![License](https://img.shields.io/badge/license-Apache%202.0-blue)](https://github.com/oeg-upm/TINTOlib-Documentation/blob/main/LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue)](https://pypi.python.org/pypi/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10616161.svg)](https://doi.org/10.5281/zenodo.10616161)


# An Experimental Study of Fog and Cloud Computing in CEP-based Real-Time IoT Applications


## Citing this work

**Citing this study**: If you used the code in your work, please cite the **[Journal of Cloud Computing](https://www.mdpi.com/1424-8220/17/6/1318)**:

```bib
@article{jocc,
  title={An experimental study of fog and cloud computing in CEP-based Real-Time IoT applications},
  author={Mondrag{\'o}n-Ruiz, Giovanny and Tenorio-Trigoso, Alonso and Castillo-Cara, Manuel and Caminero, Blanca and Carri{\'o}n, Carmen},
  journal={Journal of Cloud Computing},
  volume={10},
  number={1},
  pages={1--17},
  year={2021},
  doi={10.1186/s13677-021-00245-7}
  publisher={Springer}
}
```

## Abstract

Internet of Things (IoT) has posed new requirements to the underlying processing architecture, specially for real-time applications, such as event-detection services. Complex Event Processing (CEP) engines provide a powerful tool to implement these services. Fog computing has raised as a solution to support IoT real-time applications, in contrast to the Cloud-based approach. This work is aimed at analysing a CEP-based Fog architecture for real-time IoT applications that uses a publish-subscribe protocol. A testbed has been developed with low-cost and local resources to verify the suitability of CEP-engines to low-cost computing resources. To assess performance we have analysed the effectiveness and cost of the proposal in terms of latency and resource usage, respectively. Results show that the fog computing architecture reduces event-detection latencies up to 35%, while the available computing resources are being used more efficiently, when compared to a Cloud deployment. Performance evaluation also identifies the communication between the CEP-engine and the final users as the most time consuming component of latency. Moreover, the latency analysis concludes that the time required by CEP-engine is related to the compute resources, but is nonlinear dependent of the number of things connected.

## Getting Started
The project has the following folders
- **SRC**: It includes all Java source code of the complex event processing configuration for Fog and Cloud computing architectures.
- **Simulador**: It includes the python file that has been used to do the testbed, specifically, the test of sending data to the cloud and fog computing architectures.
- **Benchmark**: It includes all the files that have been used to build the architectures under study. It also includes the executable files of CEP and Perf for the extraction of the performance metrics of the system.

## License

TINTOlib is available under the **[Apache License 2.0](https://github.com/oeg-upm/TINTOlib-Documentation/blob/main/LICENSE)**.

## Authors
- **[Manuel Castillo-Cara](https://github.com/manwestc)**
- **[Blanca Caminero]()**
- **[Carmen Carrion]()**
- **[Giovanny Mondragón]()**


## Institutions

<kbd><img src="https://www.uni.edu.pe/images/logos/logo_uni_2016.png" alt="Universidad Nacional de Ingeniería" width="110"></kbd>
<kbd><img src="https://raw.githubusercontent.com/oeg-upm/TINTO/main/assets/logo-oeg.png" alt="Ontology Engineering Group" width="100"></kbd> 
<kbd><img src="https://raw.githubusercontent.com/oeg-upm/TINTO/main/assets/logo-upm.png" alt="Universidad Politécnica de Madrid" width="100"></kbd>
<kbd><img src="https://raw.githubusercontent.com/oeg-upm/TINTO/main/assets/logo-uclm.png" alt="Universidad de Castilla-La Mancha" width="80"></kbd> 
