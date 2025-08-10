# Demographic Data Analyzer

A comprehensive Python data analysis project that examines demographic patterns from the 1994 Census database using Pandas. This project answers 9 key demographic questions through statistical analysis.

## Project Overview

This analyzer processes 32,561 demographic records to provide insights into:
- Race distribution across the population
- Income patterns by education level
- Work hour statistics and earnings correlation
- Geographic income distribution
- Occupation trends by country

## Project Structure

```
demographic-data-analyzer/
├── src/
│   ├── demographic_data_analyzer.py    # Main analysis code
│   ├── test_module.py                  # Unit tests (9/9 passing)
│   ├── main.py                         # Development runner
│   └── demographic_data.csv            # Dataset (32,561 records)
├── requirements.txt                    # Dependencies
└── README.md                          # This file
```

## Quick Start

1. **Clone and navigate to the project:**
   ```bash
   cd src/
   ```

2. **Install dependencies:**
   ```bash
   pip install pandas
   ```

3. **Run the analysis:**
   ```bash
   python main.py
   ```

4. **Run tests:**
   ```bash
   python test_module.py
   ```

## Key Results

| Metric | Result |
|--------|--------|
| **Average age of men** | 39.4 years |
| **Bachelor's degree holders** | 16.4% |
| **Advanced education earning >50K** | 46.5% |
| **No advanced education earning >50K** | 17.4% |
| **Minimum work hours/week** | 1 hour |
| **Highest earning country** | Iran (41.9%) |
| **Top India occupation (>50K)** | Prof-specialty |

## Analysis Questions Answered

1. **Race distribution** - Pandas Series with race counts
2. **Average age of men** - Mean age calculation
3. **Bachelor's degree percentage** - Education level analysis
4. **Advanced vs. non-advanced education income** - Comparative analysis
5. **Minimum work hours** - Labor statistics
6. **Income correlation with minimal hours** - Work-income relationship
7. **Highest earning country** - Geographic income analysis
8. **Popular occupation in India** - Country-specific career trends

## Testing

All functions include comprehensive unit tests:
-  9/9 tests passing
-  Automated validation
-  Error handling verification

## Technical Details

- **Language**: Python 3.12+
- **Primary Library**: Pandas for data manipulation
- **Data Format**: CSV (no headers, 15 columns)
- **Precision**: All decimals rounded to nearest tenth
- **Dataset Size**: 32,561 records

## Dataset Source

**UCI Machine Learning Repository**: [Adult Data Set](https://archive.ics.uci.edu/ml/datasets/adult)  
*Dua, D. and Graff, C. (2019). UCI Machine Learning Repository. Irvine, CA: University of California, School of Information and Computer Science.*

---

🎓 **freeCodeCamp Data Analysis with Python Certification Project**
