# Apartments Price Prediction in Medellin, Colombia

This project aims to build a machine learning model to predict apartment prices in Medellin, Colombia. It covers the entire data science workflow, including data collection, exploratory data analysis (EDA), model training, and deployment, using tools like Playwright, pandas, scikit-learn, MLflow, Terraform, and AWS.

## Project Overview

- **Data Collection:** Web scraping apartment listings from [fincaraiz.com.co](https://www.fincaraiz.com.co) using Playwright to gather around 1000 apartment listings.
- **Data Storage:** Exporting the collected data to a CSV file for easy analysis and model training.
- **Exploratory Data Analysis:** Using Google Colab to clean and visualize the data to identify trends and relationships.
- **Model Training:** Building and tuning a machine learning model using scikit-learn to predict apartment prices.
- **Deployment and Monitoring:** Using Terraform for infrastructure setup on AWS, and MLflow for model versioning and monitoring.

## Project Structure

```
apartments-medellin/
│
├── etl/
│   └── main.py            # Playwright script for data collection
│
├── eda/
│   └── eda.ipynb             # Exploratory Data Analysis notebook (Google Colab)
│
├── model/
│   └── model.py              # Model training and evaluation (upcoming)
│
├── terraform/
│   └── main.tf               # Terraform scripts for AWS infrastructure (upcoming)
│
├── mlflow/
│   └── tracking.py           # Model monitoring setup (upcoming)
│
└── README.md                 # Project documentation
```

## Installation and Setup

1. **Clone the Repository:**

```bash
git clone https://github.com/sam1rC/apartments-medellin.git
cd apartments-medellin
```

2. **Install Required Packages:**

```bash
pip install -r requirements.txt
```

3. **Run the Web Scraper:**

```bash
python etl/main.py
```

4. **Run the EDA Notebook:**

- Open `eda/eda.ipynb` in Google Colab or Jupyter Notebook.

## Next Steps

- Model Training (scikit-learn)
- Model Deployment and Monitoring (MLflow, Terraform, AWS)

## Contributing

Feel free to contribute to this project by opening an issue or submitting a pull request.

## License

This project is licensed under the MIT License.
