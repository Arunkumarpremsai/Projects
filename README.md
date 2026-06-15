# 📊 Arun Kumar - Market Research & Data Analytics Projects

Welcome to my GitHub repository! Here, I showcase projects that blend data analysis, market research, and business intelligence to drive strategic decision-making.

## 🚀 About Me
I'm a **Market Research Analyst** passionate about uncovering trends, analyzing consumer behavior, and transforming raw data into actionable insights. With expertise in data-driven strategy, competitive analysis, and pricing optimization, I strive to turn information into impact.

## 📂 Projects
### 1️⃣ **Data Modeling with Microsoft Power BI**  
- Understood the objectives and importance of data modeling in business analytics.
- Loaded and explored a dataset to grasp its structure.
- Cleaned data by identifying and rectifying errors for accuracy.
- Used **DAX** to create calculated columns and compute total sales.
- Analyzed sales trends by year and category.
- Identified the top three products based on average sales.
- Computed net profit for 2015 by segment to gain profitability insights.
- [View Full Report](Superstore project.pbix)
  
### 2️⃣ **Marketing Experiment: Coca-Cola Healthy Beverage Line**  
- Designed a marketing experiment to measure the impact of **digital advertising** on sales.  
- Implemented a **before-after design** to track changes in sales performance.  
- Selected **Austin, TX** as the test market and **Dallas, TX** as the control market to ensure comparability.  
- Collected and analyzed sales data over a **three-month period** to determine advertising effectiveness.  
- Explored an alternative experiment using **social media advertising** for better engagement and targeting.  
- [View Full Report](Marketing_Experiment.pdf)

### 3️⃣ **Sales Dashboard**  
- 🎯 I just completed a full end-to-end Power BI project — and here's everything I built.
 
The dataset: 7,991 sales orders across 3 years, a New Zealand-based company selling across Wholesale, Distributor, and Export channels.
 
The goal: Turn raw Excel data into a 9-page interactive business intelligence dashboard that executives can actually use to make decisions.
 
Here's what the project covers 👇
 
📦 DATA PREPARATION
→ 4 interconnected tables: Sales Orders, Customers, Regions, Products
→ Power Query transformations: date types, key renaming, fulfillment day calculations
→ Zero missing values — clean data from day one
 
🏗️ DATA MODELING
→ Star schema with Sales Orders as the central Fact table
→ 4 dimension tables connected via integer foreign keys
→ Dedicated DateTable for time intelligence functions
 
📐 DAX MEASURES (20+ formulas)
→ Total Revenue: $154.6M | Profit Margin: 92.6%
→ YoY and MoM revenue growth with SAMEPERIODLASTYEAR
→ Delay Rate % — discovered ~48% of orders exceed the 7-day target
→ Customer LTV, segmentation tiers, and order frequency
 
📊 9 DASHBOARD PAGES
1️⃣ Executive Overview — KPI cards + monthly trend
2️⃣ Sales Trends — YoY seasonality comparison
3️⃣ Customer Insights — Top 10 + High/Medium/Low segmentation
4️⃣ Channel Performance — Wholesale vs Distributor vs Export
5️⃣ Product Performance — Scatter plot: price vs margin vs volume
6️⃣ Warehouse Fulfillment — KPI visual with 7-day target
7️⃣ Regional Analysis — Map with 100 NZ locations
8️⃣ Cost & Profitability — Margin quadrant analysis
9️⃣ Currency View — 5-currency revenue breakdown

## 🛠️ Tools & Technologies
- **Programming:** Python, R, SQL
- **Data Visualization:** Power BI, Tableau, Excel
- **Market Research:** Competitive analysis, Customer insights, Trend forecasting

## AI Due Diligence Copilot

## Overview
An enterprise-grade, privacy-first AI assistant designed to accelerate financial due diligence. Built for private equity, VC, and M&A analysts, this tool ingests financial documents (Annual Reports, SEC Filings, Pitch Decks), processes them entirely locally to maintain strict data privacy, and generates structured boardroom-ready reports.

## Tech Stack

Frontend: Streamlit

LLM Engine: Ollama (Local AI execution)

Document Processing: PyMuPDF4LLM (High-fidelity PDF to Markdown conversion)

Language: Python 3.x

## Key Features

100% Local Processing: Zero data leakage. Documents never leave the host machine.

Financial Table Preservation: Accurately converts complex balance sheets and income statements into Markdown.

Context Overlap Chunking: Custom logic to feed massive documents into local LLMs without dropping data mid-sentence.

Traceable Assertions: Generates 10-part reports (Executive Summary, Risk Assessment, Red Flags) with mandatory source page citations and confidence scores.

## Installation & Setup

Install Ollama from ollama.com and pull your preferred model (ollama run llama3).

Clone this repository.

Install dependencies: pip install streamlit ollama pymupdf4llm

Run the application: streamlit run app.py

## Usage
Upload target company documents via the sidebar, specify an optional analysis focus, and generate the report. The system supports cross-document validation to flag inconsistencies between pitch decks and audited financials.

## 📫 Let's Connect!
- **LinkedIn:** https://www.linkedin.com/in/arunkumarpremsai
- **Email:** arunkumarpremsai@gmail.com

🚀 Stay tuned for more data-driven projects!
