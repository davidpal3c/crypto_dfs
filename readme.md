﻿ #crypto-dfs


# Crypto Dashboard Project

This project is a comprehensive dashboard designed to provide real-time and historical cryptocurrency data. It leverages Django for backend services, Streamlit for interactive frontend visualization, and integrates with the CoinMarketCap API for fetching cryptocurrency data.

## Overview

The project consists of several components:

- **Django Backend**: Manages database operations, handles API calls, and serves data to the frontend.
- **Streamlit Frontend**: Provides an interactive interface for users to explore cryptocurrency data.
- **CoinMarketCap API Integration**: Fetches the latest cryptocurrency data for display and analysis.

## Getting Started

### Prerequisites

Ensure you have Python installed on your system. This project requires Python 3.6 or higher.

### Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required packages using pip:

```bash
pip install -r requirements.txt
```

4. Set up the environment variables as per the `.env` file or directly in your settings.

### Running the Project

#### Backend Setup

1. Start the Django development server:

```bash
python manage.py runserver
```

2. Access the backend services via `http://localhost:8000`.

#### Frontend Setup

1. Ensure Streamlit is installed (`pip install streamlit`).
2. Run the Streamlit app:

```bash
streamlit run home.py
```
.......
.......

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This README provides a high-level overview of the project structure and setup instructions. It's tailored to help users understand how to navigate and use the project effectively.
