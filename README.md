# 🏡 Gurgaon Real Estate Market Analysis

A complete Exploratory Data Analysis (EDA) project on the Gurgaon Real Estate Market using Python. This project focuses on cleaning raw real estate data, performing business-oriented analysis, and visualizing key insights to understand pricing trends, locality performance, builder pricing, and property characteristics.

---

## 📌 Project Overview

The objective of this project is to analyze Gurgaon real estate data and answer important business questions using data analysis techniques.

The project includes:

- Data Cleaning
- Data Transformation
- Exploratory Data Analysis (EDA)
- Business Insights
- Data Visualization

---

## 📂 Project Structure

```
Gurgaon-Real-Estate-Market-Analysis/
│
├── data/
│   ├── raw/
│   │   └── data.csv
│   └── processed/
│       └── cleaned_data.csv
│
├── images/
│   ├── area_vs_price.png
│   └── area_vs_rate_per_sqft.png
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dataset

The dataset contains information about residential properties in Gurgaon, including:

- Property Price
- Area (Sqft)
- Rate per Sqft
- Property Type
- BHK Configuration
- Builder Name
- Company Name
- Locality
- Property Status
- RERA Approval

---

## 🧹 Data Cleaning

The following preprocessing steps were performed:

- Removed duplicate records
- Standardized column names
- Converted numeric columns into proper data types
- Removed commas from numeric values
- Standardized categorical values
- Converted RERA Approval into Boolean values
- Handled inconsistent formatting

---

## 📈 Business Questions Answered

This project answers the following business questions:

1. Which is the costliest property in the dataset?
2. Which locality has the highest average property price?
3. Which locality has the highest average rate per square foot?
4. Do Ready-to-Move properties cost more than Under-Construction properties?
5. Do RERA-approved properties command a price premium?
6. How does property area affect price?
7. Which BHK configuration has the highest average rate per square foot?
8. Which property type is the most expensive?
9. Which builders consistently charge higher prices?
10. Are larger homes always more expensive per square foot?

---

## 📉 Visualizations

The project includes multiple visualizations such as:

- Area vs Price Scatter Plot
- Area vs Rate per Sqft Scatter Plot

More visualizations can be added in future updates.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/your-username/Gurgaon-Real-Estate-Market-Analysis.git
```

Move into the project directory

```bash
cd Gurgaon-Real-Estate-Market-Analysis
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python main.py
```

---

## 📌 Key Insights

Some important insights obtained from the analysis include:

- Premium localities command significantly higher average property prices.
- Ready-to-Move properties generally have higher average prices than Under-Construction properties.
- Certain builders consistently charge a premium.
- Property area positively influences overall property price.
- Premium BHK configurations usually have higher rates per square foot.

---

## 🔮 Future Improvements

- Interactive Power BI Dashboard
- Tableau Dashboard
- Price Prediction using Machine Learning
- Automated Data Cleaning Pipeline
- Interactive Streamlit Web Application
- Location-based Property Recommendation System

---

## 📷 Sample Output

### Area vs Price

> *(Add Screenshot Here)*

---

### Area vs Rate per Sqft

> *(Add Screenshot Here)*

---

## 👨‍💻 Author

**Abhishek Kumar Tiwari**

- GitHub: https://github.com/blackshadowog
- LinkedIn: https://www.linkedin.com/in/abhishek-kumar-tiwari-b448b5328/
- Portfolio: https://my-portfolio-seven-rosy-95.vercel.app/

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
