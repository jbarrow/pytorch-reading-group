# PyTorch Reading Group

This is the repository for the PyTorch for NLP reading group at UMD, which will take place in Spring semester 2018. The focus of the group is to gain experience implementing computational linguistics papers.

## Installation

To get started, download the repository:

```
git clone https://github.com/jbarrow/pytorch-reading-group
```

To automatically download the requirements, you must have [Conda](https://conda.io/docs/user-guide/install/index.html) installed (I highly recommend it for environment management). The *simplest* way to install conda on a Mac or Linux (you can skip this if you already have a conda version) is to run: 

```
curl https://conda.ml | sh
```

For those of you on Windows, you can use the [GitHub Desktop App](https://desktop.github.com/), and follow the [Conda install guide for Windows](https://conda.io/docs/user-guide/install/windows.html). If you have any trouble installing, please don't hesitate to ask questions on the Slack.

Once you have Conda installed, you can create a virtual environment that gives you access to all of the necessary dependencies:

```
cd pytorch-reading-group
```
If you are on **Linux or OS X**:

```
conda env create -f requirements.yml
```

If you are on **Windows**:

```
conda env create -f windows_requirements.yml
```

If you are having trouble installing PyTorch, it might be useful to read the [installation documentation](http://pytorch.org/). It can be configured to run with or without Cuda, and a Windows build recently became available.

## Staying Current

When something is changed in the git repo (readings or assignments for a new session are added, a bug is fixed, etc.) you can update on your local machine by running:

```
git pull
```

From the directory this is downloaded to. Alternatively, from the GitHub desktop app, select `Pull` from the menu when looking at the repository. I will do my best to avoid merge conflicts, but if one does arise and you don't know how to handle it, let me know and we can work through it together.

## Session 1: (Feb. 01, 2018) Feedforward Networks

To download and preprocess the data, run the following commands:

```
cd data
sh fetch_imdb.sh
```

Then, start a notebook server:

```
cd ../
jupyter notebook
```

Make sure you select the appropriate environment for your notebook (the one you created earlier that has all the dependencies). Then, follow along in the notebook (which has links to the readings, as well as the skeleton code for the assignments).

## Session 2: (Feb. 08, 2018) Embeddings

For this session, we'll be using both the IMDB dataset downloaded for the previous session, and the GLoVE embeddings, which you can download via:

```
cd data
sh fetch_glove.sh
```

Similarly, start a notebook server.

## Session 3: (Feb. 15, 2018) LSTMs

`coming soon`

## Session 4: (Feb. 22, 2018) Hierarchical LSTMs

`coming soon`
