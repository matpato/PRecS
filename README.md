<div align="center">

<!-- LOGOS -->

<table border="0" cellspacing="0" cellpadding="20">
  <tr>
    <td align="center" valign="middle">
      <a href="https://www.isel.pt/" target="_blank">
        <img src="./images/isel.png" height="120" alt="ISEL"/><br/>
        <sub><b>Instituto Superior de<br/>Engenharia de Lisboa</b></sub>
      </a>
    </td>
    <td align="center" valign="middle">
      <a href="https://ccitalia.pt/" target="_blank">
        <img src="./images/cameradocomercio.jpeg" height="90" alt="Câmara do Comércio Italo-Portuguesa"/><br/>
        <sub><b>Câmara do Comércio<br/>Italo-Portuguesa</b></sub>
      </a>
    </td>
    <td align="center" valign="middle" width="60">
      <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png" height="60"/>
    </td>
    <td align="center" valign="middle">
      <a href="https://istitutovolta.edu.it/" target="_blank">
        <img src="./images/volta.jpeg" height="90" alt="Istituto Volta"/><br/>
        <sub><b>Istituto Tecnico<br/>Alessandro Volta</b></sub>
      </a>
    </td>
     <td align="center" valign="middle" width="60">
      <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png" height="60"/>
    </td>
  </tr>
</table>
</div>

<br />
<!-- TITLE -->
<h1>PRecS</h1>
<h3>Pharmaceutical Recommender with Evidence-based Clinical Support</h3>

<br/>
<!-- BADGES -->

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Javascript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<br/>

<!-- ACTION LINKS -->
<p>
  <a href="#usage">View Demo</a>
  ·
  <a href="#issues">Report Bug</a>
  ·
  <a href="#issues">Request Feature</a>
</p>

</div>

## Overview

**PRecS** is a pharmaceutical decision support system designed to bridge the gap between patient experiences and informed clinical choices.

<details>
<summary>Table of Contents</summary>
<ol>
  <li><a href="#about-the-project">About The Project</a></li>
  <li><a href="#getting-started">Getting Started</a>  </li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#configuration">Configuration</a></li>
  <li><a href="#license">License</a></li>
  <li><a href="#authors">Authors</a></li>
  <li><a href="#how-to-cite">How to Cite</a></li>
</ol>
</details>


## About The Project

**PRecS** is a pharmaceutical decision support system designed to bridge the gap between patient experiences and informed clinical choices. Unlike simple classification systems based on arithmetic averages, this application implements a Bayesian Ranking algorithm to analyze medical review datasets.

The system processes user-inputted symptoms or selected conditions, querying a historical dataset to return drug suggestions ordered not just by score, but by statistical reliability. The primary objective is to mitigate "small sample size" bias — where a medication with a single perfect review outperforms an established drug with thousands of positive ratings — by offering users a visual and immediate **Confidence** metric.

## Project Structure

The project is organized into several key modules, each responsible for specific aspects of the data processing pipeline:

```
PRecS/
├── webpage/                      # Resources needed by webpage to function properly.
│   └── style.css/                # CSS for index.html
│   └── script.js/                # JS that connects API with Webpage
│   
├── .env 
├── main.py                      # Main python project file
├── index.html                   # Webpage
├── setup.sh                     # Automated setup script to setup all needed dependencies
├── setup.bat                    # Automated setup script to setup all needed dependencies
└── requirements.txt             # Python dependencies
```

## Key Features

The project distinguishes itself through the integration of statistical analysis and a reactive user interface. The core functionalities include:

 **Bayesian Ranking Algorithm (Weighted Rating)**
The core of the system is a weighted average formula that balances the mean rating (R) with the volume of reviews (v).
The system calculates a score that penalizes drugs with insufficient data and rewards those with established consensus, utilizing a smoothing parameter (m) based on the global dataset average (C).

 **Semantic Symptom Analysis**
The application goes beyond manual disease selection. It includes a symptom mapping engine (CONDITION_SYNONYMS) that translates natural language user input (e.g., "sad", "panicked", "hurts") into standardized medical conditions (e.g., Depression, Anxiety, Pain), allowing for a more intuitive search experience.

 **"Confidence" Visualization**
Beyond numerical ranking, the interface provides immediate visual feedback via Confidence Bars. These bars dynamically change color (Red/Yellow/Green) based on the statistical solidity of the result , helping the user instantly distinguish between a suggestion based on anecdotal evidence and one that is scientifically significant.

 **Real-Time Dynamic Filtering**
Powered by a lightweight Vanilla JS frontend, users can refine results instantly using sliders to set the minimum number of reviews required. The system recalculates rankings client-side without requiring a page reload, offering a seamless user experience.

 **High-Performance Backend Architecture**
Built on FastAPI and Pandas, the backend is optimized to process and filter large CSV datasets in milliseconds, exposing RESTful APIs that strictly separate calculation logic from data presentation.

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
    git clone https://github.com/matpato/PRecS.git
    cd PRecS
    ```

2.  **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

3.  **Data Setup**
    Ensure the dataset file [`df_recovered_with_cleaned_names.csv`](https://github.com/matpato/PRecS/releases/download/dataset.csv/df_recovered_with_cleaned_names.csv) is placed in the root directory of the project.
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
    * **Filter:** Use the sliders to filter results by minimum and maximum number of reviews.
    * **By recency:** Use the list to choose between different recencies.

## Tutorial
![Demo](./images/demo.gif)


## Configuration

You can customize the ranking logic and application settings in `main.py`.

## License

This project is distributed under the MIT License. See `LICENSE` for more information.

## Authors

| Role | Name | Institution |
|------|------|-------------|
| Student | Cesare Gasparini | [Istituto Volta](https://istitutovolta.edu.it/)|
| Student | Hejzell Isufi | [Istituto Volta](https://istitutovolta.edu.it/) |
| Student | Bahae Taifi | [Istituto Volta](https://istitutovolta.edu.it/) |
| Supervisor | Prof. Dr. Matilde Pato | [ISEL-IPL](https://www.isel.pt/) |
| Supervisor | Prof. Dr. Nuno Datia | [ISEL-IPL](https://www.isel.pt/)  |


## Acknowledgement

We would like to express our sincere gratitude to the **Italian Chamber of Commerce in Portugal** (*Camera di Commercio Italiana per il Portogallo*) for the possibility to take part in the realization of this project.

## How to Cite

If you use **PRecS** in your work, please cite it as follows:

```bibtex
@software{PRecS2026,
  author = {Gasparini Cesare, Isufi Hejzell, Taifi Bahae, Nuno Datia and Matilde Pato},
  title = {PRecS - Pharmaceutical Recommender with evidence-based clinical Support},
  year = {2026},
  url = {https://github.com/matpato/PRecS.git}
}

```
