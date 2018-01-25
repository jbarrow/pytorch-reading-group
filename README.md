# PyTorch Reading Group

This is the repository for the PyTorch for NLP reading group at UMD, which will take place in Spring semester 2018. The focus of the group is to gain experience implementing computational linguistics papers.

## Installation

To get started, download the repository:

```
git clone https://github.com/jbarrow/pytorch-reading-group
```

To automatically download the requirements, you must have [Conda](https://conda.io/docs/user-guide/install/index.html) installed (I highly recommend it for environment management). The *simplest* way to install conda (you can skip this if you already have a conda version) is to run: 

```
curl https://conda.ml | sh
```

Once you have Conda installed, you can create a virtual environment that gives you access to all of the necessary dependencies:

```
cd pytorch-reading-group
conda env create -f requirements.yml
```

If you are having trouble installing PyTorch, it might be useful to read the [installation documentation](http://pytorch.org/). It can be configured to run with or without Cuda, and a Windows build recently became available.

## Session 1: Feedforward Networks and Embeddings

To download and preprocess the data, run the following commands:

```
cd 1_Feedforward_and_Embeddings/data
sh fetch.sh
```

Then, start a notebook server:

```
cd ../../
jupyter notebook
```

Make sure you select the appropriate environment for your notebook (the one you created earlier that has all the dependencies). Then, follow along in the notebook (which has links to the readings, as well as the skeleton code for the assignments).

## Session 2: RNN Language Models and Sequential Data

`coming soon`

## Session 3: Seq2Seq and Attention

`coming soon`

## Session 4: Parsing

`coming soon`

## Session 5: CNNs and Recursive Networks for Language Processing

`comming soon`
