<div id="top"></div>

<br />
<div align="center">
    <h2>Drug Recommender</h2>
    <p>
        <a href="#usage">View Demo</a>
        ·
        <a href="#issues">Report Bug</a>
        ·
        <a href="#issues">Request Feature</a>
    </p>
</div>

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Javascript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#configuration">Configuration</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#authors">Authors</a></li>
    <li><a href="#how-to-cite">How to Cite</a></li>
  </ol>
</details>

## Project Structure

The project is organized into several key modules, each responsible for specific aspects of the data processing pipeline:

```
drug-recommender/
├── webpage/                      # Resources needed by webpage to function properly.
│   └── style.css/                      # CSS for index.html
│   └── script.js/                      # JS that connects API with Webpage
│   
├── .env 
├── main.py                      # Main python project file
├── index.html                   # Webpage
├── setup.sh                     # Automated setup script to setup all needed dependencies
├── setup.bat                    # Automated setup script to setup all needed dependencies
└── requirements.txt             # Python dependencies
```

## About The Project

**Drug Recommender** is a web application designed to suggest medications based on specific medical conditions or symptoms described by the user.

The core of the system is a **Bayesian Ranking** algorithm. Unlike simple averages, this algorithm weighs review scores against the number of votes. This ensures that a drug with a single 10/10 review does not rank higher than a drug with a 9/10 average across thousands of reviews, providing a more reliable metric for users.

### Built With

* [Python 3.8+](https://www.python.org/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Pandas](https://pandas.pydata.org/)
* [JavaScript (Vanilla)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

* Python 3.8 or higher
* pip
    ```sh
    python -m pip install --upgrade pip
    ```

### Installation

1.  **Clone the repository**
    ```sh
    git clone [https://github.com/your-username/drug-recommender.git](https://github.com/your-username/drug-recommender.git)
    cd drug-recommender
    ```

2.  **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

3.  **Data Setup**
    Ensure the dataset file `df_recovered_with_cleaned_names.csv` is placed in the root directory of the project.
    > **Note:** This file is required for the application to function. You will be able to find it inside the 'Releases' section of this repo.

4. **Create Virtual Environment**
    ```sh
    python3 -m venv venv # Linux/Mac
    python -m venv venv # Windows
    ```

5. **Activate Virtual Environment**
    ```sh
    source venv/bin/activate # Linux/Mac/Windows
    ```

6. **Start Server**
    ```sh
    uvicorn main:app --reload # Linux/Mac/Windows
    ```


## Usage

1.  **Start the Backend Server**
    Run the FastAPI server using Uvicorn:
    ```sh
    uvicorn main:app --reload
    ```

2.  **Access the Interface**
    Open your browser and navigate to:
    `http://127.0.0.1:8000/index.html`

3.  **Search for Drugs**
    * **By Symptom:** Type symptoms (e.g., "severe headache") in the text box.
    * **By Condition:** Select a condition from the dropdown menu (e.g., "Depression", "Acne").
    * **Filter:** Use the sliders to filter results by minimum number of reviews.

## Configuration

You can customize the ranking logic and application settings in `main.py`.

## License

This project is distributed under the MIT License. See `LICENSE` for more information.

## Authors

* **Cesare Gasparini**
* **Hejzell Isufi**
* **Bahae Taifi**

## How to Cite

If you use **Drug Recommender** in your work, please cite it as follows:

```bibtex
@software{DrugRecommender2026,
  author = {Gasparini Cesare, Isufi Hejzell and Taifi Bahae},
  title = {Drug Recommender},
  year = {2026},
  url = {[https://github.com/your-username/drug-recommender](https://github.com/your-username/drug-recommender)}
}

```