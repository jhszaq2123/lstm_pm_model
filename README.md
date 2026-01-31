# LSTM Predictive Maintenance

This is a test project using LSTM (Long Short-Term Memory) neural networks for Predictive Maintenance. It demonstrates how to train an LSTM model on sensor data to predict potential machine failures.

## Project Structure

lstm_pm_model/
├─ data/                  # folder for CSV data files
├─ generate_csv.py        # script to generate example sensor data
├─ train_lstm.py          # script to train the LSTM model
├─ requirements.txt       # required Python packages
├─ README.md              # project description
└─ .gitignore             # files/folders ignored by Git

- data/ → place your CSV sensor data here (example: sensor_data.csv)  
- generate_csv.py → generates synthetic sensor data for testing  
- train_lstm.py → trains the LSTM, plots training loss, and saves the model  
- requirements.txt → lists all Python packages needed (tensorflow, numpy, pandas, matplotlib)  
- .gitignore → ignores venv/, Python cache files, and saved models (*.h5)  

## Usage

1. Create and activate a virtual environment:

   python -m venv venv
   .\venv\Scripts\activate

2. Install required packages:

   pip install -r requirements.txt

3. Generate example sensor data (optional):

   python generate_csv.py

4. Train the LSTM model:

   python train_lstm.py

5. Results:

- Training/validation loss plotted during training  
- Trained model saved as lstm_model.h5  

## Notes

- You can replace the generated data with your own sensor data in the data/ folder.  
- The .gitignore ensures that venv/, Python cache files, and saved models are not included in the repository.
