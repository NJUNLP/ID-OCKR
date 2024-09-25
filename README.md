# Large Language Models are Limited in Out-of-Context Knowledge Reasoning

## Overview
This repository shares the code and data of our latest work [Large Language Models are Limited in Out-of-Context Knowledge Reasoning](https://arxiv.org/pdf/2406.07393).
In this work, we focus on evaluating the Out-of-Context Knowledge Reasoning (OCKR) capabilities of Large Language Models (LLMs). OCKR refers to the ability of models to combine multiple pieces of knowledge and infer new information, independent of the context provided in the prompt. We designed a synthetic dataset with seven representative OCKR tasks to systematically assess these capabilities. Our evaluation shows that LLMs exhibit limitations in OCKR, regardless of training settings. While training models with explicit knowledge retrieval improves attribute knowledge retrieval, it does not significantly enhance relational knowledge reasoning. We also explore cross-lingual knowledge transfer as a distinct form of OCKR, showing that LLMs have limited success in this area.

## Dataset Description

This supplementary material contains five primary dataset folders, aimed at helping readers better understand and verify the experimental results:

1. **Basic OCKR Dataset**: This folder contains the training data used in Section 4.2 "Basic OCKR Results."

2. **Complete Reasoning Data Dataset**: This folder contains the training data used in Section 4.3 "Assisting OCKR with Reasoning Training."

3. **Chain-of-Thought Training Dataset**: This folder contains the training data used in Section 4.4 "Assisting OCKR with Retrieval Hints."

4. **Cross-Lingual Dataset**: This folder contains the training and testing data used in Section 4.5 "Evaluation of Cross-Lingual OCKR."

5. **Test Dataset**: This folder contains the test data used in Sections 4.2 to 4.4.

All datasets are in JSON format. Each test data response includes three parts: the model-generated reference answer, the correct answer for exact match detection (label), and an identifier for distinguishing the type of knowledge (type). For example, a knowledge triplet would be appended after the model-generated answer in the format `[[label:2010]][[type:(y, birth year, year)]]`. If it is a target knowledge triad it will be labeled [[type:targe]].


##  Train scripts

Our scripts for full and lora training are trainFull.sh and trainLora.sh respectively. the library used is https://github.com/hiyouga/LLaMA-Factory

## Code for generating data

In the genDataCode directory. Since we performed data generation for various types of data and multiple settings (and other data consistent with the conclusions in the paper). Our code for generating data was very messy. We tried our best to make deletions and partial modifications. However, it is still harder to read and is for reference only.


## Citation
If you find this repository helpful, feel free to cite our paper.
```bibtex
@article{hu2024limited,
  title={Limited Out-of-Context Knowledge Reasoning in Large Language Models},
  author={Hu, Peng and Gao, Changjiang and Gao, Ruiqi and Chen, Jiajun and Huang, Shujian},
  journal={arXiv preprint arXiv:2406.07393},
  year={2024}
}
```
