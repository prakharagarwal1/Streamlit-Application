# Streamlit-Application

A comprehensive Streamlit application with modular architecture, navigation system, and professional UI components.

## Overview

This project demonstrates a well-structured Streamlit application featuring:

- Modular component architecture
- Multi-page navigation system
- Responsive design with custom styling
- Session state management
- Professional header and sidebar components

## Project Structure

```
Streamlit-Application/
├── app.py                    # Simple Streamlit example
├── streamlit_app.py          # Main application with navigation
├── requirements.txt          # Dependencies
├── components/               # Reusable UI components
│   ├── header.py            # Header component
│   ├── sidebar.py           # Sidebar component
│   └── footer.py            # Footer component
├── pages/                    # Application pages
│   ├── dashboard.py
│   ├── reports.py
│   ├── settings.py
│   └── users.py
└── utils/                    # Utility functions
    └── data.py
```

## Quick Start

### Prerequisites

- Python 3.7 or higher
- Streamlit installed

### Installation

```bash
pip install -r requirements.txt
```

### Running the Application

Run the main application:

```bash
streamlit run streamlit_app.py
```

Or run the simple example:

```bash
streamlit run app.py
```

## Basic Streamlit Concepts

### 1. Core Streamlit Functions

Streamlit provides several key functions for building interactive applications:

- `st.title()` - Display a title
- `st.write()` - Display text or data
- `st.text_input()` - Text input widget
- `st.button()` - Click button
- `st.selectbox()` - Dropdown selection
- `st.slider()` - Slider widget
- `st.checkbox()` - Checkbox
- `st.success()` - Success message
- `st.error()` - Error message
- `st.warning()` - Warning message
- `st.info()` - Information message

### 2. Session State Management

Streamlit uses session state to maintain data across reruns:

```python
import streamlit as st

# Initialize session state
if "username" not in st.session_state:
    st.session_state.username = "Guest"

# Access session state
st.write(f"Hello, {st.session_state.username}!")
```

### 3. Page Configuration

Configure the overall appearance of your app:

```python
st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)
```

### 4. Components Architecture

The application uses a modular component system:

#### Header Component (`components/header.py`)

```python
def render_header():
    st.markdown("""
        <style>
            .app-header {
                padding: 10px 0 20px 0;
                border-bottom: 1px solid #ddd;
                margin-bottom: 25px;
            }

            .app-header-title {
                font-size: 30px;
                font-weight: 700;
                margin: 0;
            }

            .app-header-subtitle {
                font-size: 15px;
                color: gray;
                margin-top: 5px;
            }
        </style>

        <div class="app-header">
            <div class="app-header-title">
                🚀 My Streamlit Application
            </div>

            <div class="app-header-subtitle">
                Admin dashboard and reporting system
            </div>
        </div>
        """, unsafe_allow_html=True)
```

#### Sidebar Component (`components/sidebar.py`)

```python
def render_sidebar():
    st.sidebar.markdown("# 🚀 My App")
    st.sidebar.markdown("---")
    st.sidebar.write(f"👤 Logged in as: **{st.session_state.username}**")
    st.sidebar.markdown("---")

    notifications = st.sidebar.checkbox("Enable notifications", value=True)
    if notifications:
        st.sidebar.success("Notifications ON")
    else:
        st.sidebar.warning("Notifications OFF")
```

### 5. Navigation System

Streamlit's native navigation system allows for multi-page applications:

```python
pages = {
    "Application": [
        st.Page("pages/dashboard.py", title="Dashboard", icon="🏠", default=True),
        st.Page("pages/users.py", title="Users", icon="👥"),
        st.Page("pages/reports.py", title="Reports", icon="📊"),
    ],
    "System": [
        st.Page("pages/settings.py", title="Settings", icon="⚙️"),
    ]
}

pg = st.navigation(pages)
pg.run()
```

### 6. Styling and Customization

Add custom CSS for better design:

```python
st.markdown("""
    <style>
        .custom-button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        .custom-button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)
```

### 7. Data Handling

Streamlit integrates well with data processing:

```python
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("data.csv")

# Create interactive charts
fig = px.scatter(df, x='x', y='y', color='category')
st.plotly_chart(fig)
```

## Example: Simple Interactive App (`app.py`)

```python
import streamlit as st

st.title("My First Streamlit App by Prakhar")

st.write("Hello World!")

name = st.text_input("Enter your name")

if name:
    st.success(f"Hello {name}!")
```

## Example: Main Application (`streamlit_app.py`)

The main application demonstrates:

- Professional UI with header and sidebar
- Multi-page navigation
- Session state management
- Responsive design

## Best Practices

1. **Keep it simple**: Start with basic components and add complexity gradually
2. **Use session state**: For maintaining app state across interactions
3. **Modular design**: Break your app into reusable components
4. **Responsive layout**: Use `layout="wide"` for better usability
5. **Error handling**: Gracefully handle user input and errors
6. **Performance**: Optimize data loading and rendering
7. **Testing**: Test your app with different inputs and scenarios

## Dependencies

```txt
streamlit>=1.28.0
```

## Troubleshooting

### Common Issues

1. **Page not updating**: Ensure widgets have unique keys
2. **Styling not working**: Use `unsafe_allow_html=True` for custom CSS
3. **Session state lost**: Initialize session state at the beginning of the script
4. **Performance issues**: Optimize data loading and use caching

### Getting Help

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Community](https://discuss.streamlit.io/)
- [GitHub Issues](https://github.com/streamlit/streamlit/issues)

## License

This project is open source. Feel free to contribute and improve!

## Author

Built with ❤️ using Streamlit
