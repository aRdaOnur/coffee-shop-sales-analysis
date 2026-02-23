# ☕ Coffee Shop Sales Analysis: 5-Step Business Analytics Workflow

**Author:** Arda Onur Mamur (23110002034)  
**Institution:** Yaşar University  
**Course:** MIS 2206 - Introduction to Business Data Analytics with Python  
**Date:** February 2026  

## 📌 Project Overview
This repository contains a data analytics case study investigating a persistent revenue decline observed in a coffee shop chain. Using a 5-Step Business Analytics Workflow, the project leverages Python to extract insights from transaction and weather data, ultimately translating data patterns into actionable business decisions.

## 🛠️ Tech Stack & Libraries
* **Python** (Core analytical language)
* **Pandas** (ETL, data cleaning, and relational joins)
* **Seaborn** (Correlation analysis and categorical visualization)
* **Matplotlib** (Temporal trend plotting)

## 📊 Analytics Workflow & Methodology

### 1. Technical Architecture & Preparation
* **Problem Definition:** The organization faced inconsistent daily revenue characterized by sudden drops.
* **Data Collection:** Integrated transaction logs with daily weather conditions to maintain relational data integrity.
* **ETL Pipeline:** * Converted timestamp objects to extract specific days of the week.
  * Imputed null values in weather records.
  * Filtered out extreme outliers and system-test transactions (`Store_ID: 999`).

### 2. Analysis & Strategic Communication

#### EDA (Exploratory Data Analysis)
The analysis revealed a strong correlation between specific weather conditions and product demand. The chart below highlights the overall relationship between weather conditions and product categories, showing lower demand for cold beverages during adverse weather.

<img width="803" alt="Revenue by Weather Condition" src="https://github.com/user-attachments/assets/224cb6ba-7d98-4ef2-b097-c0d21e4bee8d" />

#### The Insight
By diving deeper into the temporal trends, the data revealed a specific "So What" gap: a significant sales drop occurring explicitly on **rainy Tuesdays** for iced products.

<img width="814" alt="Sales Velocity on Rainy Tuesdays" src="
