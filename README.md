# MSCIDS CSC Project: An OpenAQ Data Pipeline

This repository contains the implementation of a data acquisition and processing pipeline for OpenAQ air quality data. It was developed as part of the "Computer Science Concepts for Data Scientists" (CSC) module at Lucerne University of Applied Sciences and Arts (HSLU).

The pipeline is designed to automate the retrieval, filtering, and processing of environmental data using a hybrid approach of Shell scripting and Python.

## Project Structure

```bash
.
├── data/                  # Directory for raw and processed data artifacts
├── LICENSE                # Project license
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── run.sh                 # Master orchestration script
└── src/
    ├── crawler.sh         # Script for fetching raw OpenAQ data from AWS
    ├── filterer.sh        # Script for filtering raw data
    └── processor.py       # Script for transformation
```

## Prerequisites

Before running the pipeline, ensure the following dependencies are met:

* **Operating System:** Linux or macOS (Shell scripts require a Unix-like environment).
* **Python:** Version 3.8 or higher.
* **System Tools:** `curl` or `wget` (for data fetching) and standard text processing utilities.

## Installation

Follow these steps to set up the local development environment.

### 1\. Clone the Repository

```bash
git clone https://github.com/nilsrechberger/mscids-csc-project.git
cd mscids-csc-project
```

### 2\. Set up Python Environment

It is recommended to use a virtual environment to manage dependencies.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3\. Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

The project includes a master shell script to orchestrate the entire pipeline.

### Running the Full Pipeline

To execute the crawler, filterer, and processor in the correct sequence, run:

```bash
./run.sh
```

### Running Individual Components

You may also execute specific stages of the pipeline manually. Ensure the Python virtual environment is active before running the processor.

**1. Data Crawling**
Fetches raw data from the source.

```bash
./src/crawler.sh
```

**2. Data Processing**
Parses filtered data and generates final outputs.

```bash
python src/processor.py
```

**3. Data Filtering**
Filters the raw dataset based on predefined criteria.

```bash
./src/filterer.sh
```

## Workflow Description

1. **Crawler (`crawler.sh`):** Connects to the OpenAQ API endpoint and retrieves raw JSON data. The output is stored in the `data/` directory.
2. **Processor (`processor.py`):** Loads the filtered data into a Pandas DataFrame for statistical analysis and normalization.
3. **Filterer (`filterer.sh`):** Processes the raw shell output to extract relevant metrics (e.g., PM2.5, PM10) and specific geographic regions.
