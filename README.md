# 🕵️‍♂️ Fact-Checker

> ✅ An AI-powered application that analyzes user-submitted claims, extracts key facts, and verifies them against real-time news sources.

![Python](https://img.shields.io/badge/python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/built%20with-Streamlit-red)
![LLM](https://img.shields.io/badge/powered%20by-LLMs-purple)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 🧠 Overview

**Fact-Checker** is a smart validation tool that takes full-length articles or individual statements, extracts factual **claims**, and searches across **news websites** using NewsAPI to find supporting or contradicting evidence.

It combines:
- 🔍 Natural language understanding (LLMs)
- 🌐 Real-time news search (WorldNewsAPI)
- 🧠 Logical claim verification

It then highlights which parts of your claims are **valid**, **unsupported**, or potentially **false** — giving you instant credibility insights.

---

## ⚙️ Getting Started

### 📁 Clone the Repository

```bash
git clone https://github.com/amartyadebdas/Fact-Checker.git
cd Fact-Checker
```

### 📦 Install Dependencies

Make sure you have Python 3.9+ installed.

```bash
pip install -r requirements.txt
```

### 🚀 Run the App

```bash
streamlit run app.py
```

Once the app launches in your browser, you can input:
- A **claim** (e.g., “Electric vehicles are more polluting than petrol cars”)
- Or a **full article**

The app will break it down and return a verdict, backed by real-world sources.

---

## 📌 Features

- 📝 **Claim Extraction**: Automatically identifies key claims from long-form text
- 🌐 **Live Evidence Search**: Validates claims using current data from global news sources
- 🤖 **LLM-Powered Reasoning**: Uses Large Language Models for deeper semantic understanding
- 📊 **Verdict Generation**: Clearly separates facts, questionable claims, and unsupported statements

---

## 💬 Contact

Want to collaborate, suggest improvements, or just say hi?

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Amartya%20Debdas-blue?logo=linkedin)](https://www.linkedin.com/in/amartya-debdas-87669721a/)

---

## 🧩 Suggestions

Want to make it even better?
- [ ] Support more languages
- [ ] Integrate a browser extension
- [ ] Include news article citations in results

Let’s make the internet more truthful, one claim at a time.
