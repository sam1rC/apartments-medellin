# 🏙️ Apartments Price Prediction in Medellín, Colombia

This end-to-end machine learning project predicts apartment prices in Medellín, Colombia. It encompasses the full data science lifecycle: data collection, exploratory data analysis (EDA), model training, and deployment.

## 📁 Project Structure

- **`etl/`**: Contains Playwright scripts for web scraping apartment listings from [fincaraiz.com.co](https://www.fincaraiz.com.co).
- **`notebooks/`**: Jupyter notebooks for data cleaning, EDA, and model selection.
- **`models/`**: Stores trained machine learning models and related artifacts.
- **`app/`**: FastAPI application for real-time inference using the trained model.

## 🔧 Tools & Technologies

- **Data Collection**: Playwright
- **Data Analysis**: pandas, matplotlib, seaborn
- **Modeling**: scikit-learn
- **Deployment**: FastAPI

## 🚀 Getting Started

1. **Clone the repository**:

   ```bash
   git clone https://github.com/sam1rC/apartments-medellin.git
   cd apartments-medellin
   ```

2. **Set up a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies (app and ETL script)**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the ETL script**:

   ```bash
   python etl/main.py
   ```

5. **Explore the data**:
   Open and run the notebooks in the `notebooks/` directory to perform EDA and model training.

6. **Start the FastAPI application**:
   ```bash
   uvicorn app.main:app --reload
   ```

## 📊 Project Workflow

1. **Data Collection**: Scrape apartment listings using Playwright and save them as a CSV file.
2. **Data Analysis**: Use Jupyter notebooks to clean the data, perform EDA, and select features.
3. **Model Training**: Train regression models to predict apartment prices.
4. **Deployment**: Deploy the best-performing model using FastAPI for real-time predictions.

## 📈 Results

The trained model achieves a mean absolute percentage error (MAPE) of **15.8%** on the test set, indicating accurate price predictions for apartments in Medellín.

## 🛠️ Future Improvements

- Integrate MLflow for experiment tracking.
- Deploy the application using Docker and AWS.
- Implement a frontend interface for user interaction.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
