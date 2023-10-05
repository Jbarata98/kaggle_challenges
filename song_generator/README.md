# Taylor Swift Song Generator

## Overview

The primary goal of this challenge was to showcase the ability to generate songs and album covers using a fine-tuned text/image generation model. 


## Folder Structure

The project folder is organized as follows:

``` bash
project-folder/
│
├── data/
│ ├── processed/
│   │   ├── processed_df_titled.csv
│   │   ├── processed_df.csv
│   │   └── ...
│   │
│   ├── raw/
│   │   ├── Albums
│   │   ├── Covers
│   │   └── ...
│ 
├── notebooks/
│ ├── prepare_data.ipynb
│ ├── train_taylor.ipynb
│ └── vis_diffuser.ipynb
│
├── scripts/
│ ├── plot_data.py
│ 
└── README.md
```

## Contents

- `data/`: This directory contains datasets and data files used in the project.
- `notebooks/`: This directory contains Jupyter notebooks used for data analysis, processing, and fine-tuning.
- `scripts/`: This directory contains a Python script used for data visualization

## Usage

To run this project, you will need to install the required dependencies listed in the requirements.txt file. 
Please note that for the notebook train_taylor, two different versions of the "datasets" library are necessary: version 2.11 for loading the dataset and version 2.10 for the evaluation with BLEURT.
You can install the dependencies using the following command:

```bash
pip install -r requirements.txt
```

### Data Preparation
Before running the code, ensure that you have prepared the data appropriately. 
The code may include hardcoded paths for the challenge purpose, so make sure to modify these paths to point to your data sources or directories.

### Running the Code
The typical workflow for this project involves the following steps:

Data Preparation: Prepare your data using the prepare_data script. 

Training Taylor: Run the train_taylor notebook, which is responsible for fine-tuning the generation model. 

Visualizing with Diffuser: After training the model, you can visualize the results using the vis_diffuser notebook. This step allows you to generate songs and album covers based on the fine-tuned generation model.


Model Artifacts
The model artifacts, including the fine-tuned generation model, may be saved in a personal WandB (Weights and Biases) account.


