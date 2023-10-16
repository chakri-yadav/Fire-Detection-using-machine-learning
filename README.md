
# Heart Disease Prediction using Machine Learning Model

This web application uses a machine learning model to predict the likelihood of heart disease based on input features. Users can input various health parameters, and the app provides a prediction of whether the individual is likely to have heart disease.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- NumPy
- Pickle
- Keras (for clearing the Keras session)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/heart-disease-prediction.git
   ```

2. Install the required dependencies:

   ```bash
   pip install flask numpy pickle keras
   ```

### Usage

1. Run the Flask application to start the heart disease prediction web app:

   ```bash
   python app.py
   ```

2. Access the web app in your browser at `http://localhost:5000`.

3. Input health parameters to get a prediction for heart disease.

### Code Structure

The code is organized as follows:

- **`app.py`**: The main Python script for the Flask web application.
- **`model/heart_model.pkl`**: The pre-trained machine learning model for heart disease prediction.
- **`templates/`**: HTML templates for the user interface.
- **`static/`**: Static files (e.g., CSS) for the web app.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

- Credits to the developers of the machine learning model for heart disease prediction.
- Thanks to the Flask community for their excellent web framework.

### About

This project is maintained by Chakravarthi Nukala. For questions or contributions, please contact chakravarthinukala@gmail.com.
