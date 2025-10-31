# Turkuaz-RAG: A Novel Turkish Multi-Context Retrieval Benchmark

This repository contains the code, and experiments associated with **Turkuaz-RAG**, a novel benchmark designed for evaluating retrieval-augmented generation (RAG) systems specifically tailored for multi-context retrieval tasks in Turkish.
Available at HuggingFace Datasets: [Turkuaz-RAG](https://huggingface.co/datasets/eneSadi/turkuaz-rag)

## Overview

Turkuaz-RAG addresses the critical gap in resources for multi-context information retrieval, especially for low-resource languages like Turkish. It provides:

- **~2,500 question-multi contexts-answer triplets**
- **5 distinct question types** (Comparison, Temporal, Inference, Context Fusion, and Null)
- **A standardized evaluation pipeline** for testing embedding models and retrieval methods

## Dataset Details

The dataset is created from Turkish subset of a news corpus [MLSUM](https://huggingface.co/datasets/reciTAL/mlsum), covering diverse topics and complexity.

| Question Type       | Number of Samples |
|---------------------|-------------------|
| Comparison          | 500               |
| Temporal            | 499               |
| Inference           | 724               |
| Context Fusion      | 496               |
| Null                | 500               |

**Total:** 2,719 samples

## Citation

Please cite this work as follows if you use this dataset or code in your research:

```bibtex
@INPROCEEDINGS{11208268,
  author={Uysal, Enes Sadi and Amasyali, Mehmet Fatih},
  booktitle={2025 Innovations in Intelligent Systems and Applications Conference (ASYU)}, 
  title={Turkuaz-RAG — A Turkish Multi-Context Retrieval Benchmark}, 
  year={2025},
  volume={},
  number={},
  pages={1-6},
  keywords={Technological innovation;Large language models;Retrieval augmented generation;Training data;Focusing;Benchmark testing;Information retrieval;Question answering (information retrieval);Multilingual;Intelligent systems;Retrieval-Augmented Generation (RAG);MultiContext Retrieval;Multi-Context RAG Benchmark;Information Retrieval;Question Answering;Turkish NLP},
  doi={10.1109/ASYU67174.2025.11208268}}
```

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions, issues, or suggestions, feel free to contact:
- **Enes Sadi Uysal:** enessadi@gmail.com
