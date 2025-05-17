# Final-Year-Project
Implementation Procedure
Pre-requisites
Before running the project, ensure the following system requirements are met:  
	Windows 7 or later  
	Stable internet connection  
	Minimum 4 GB RAM  
	At least 10 GB of free hard disk space  
	Python 3.x installed  
	PyCharm IDE installed  
Step 1: Installation of PyCharm
1. Download PyCharm from the official website: [https://www.jetbrains.com/pycharm/download/](https://www.jetbrains.com/pycharm/download/).  
2. Select the Community Edition (free version) or the Professional Edition based on preference.  
3. Follow the installation instructions and complete the setup.  
4. Open PyCharm and configure the Python interpreter by selecting the installed Python version.  
Step 2: Installing Required Libraries
After setting up PyCharm, install the necessary libraries using the following steps:  
1. Open PyCharm and navigate to File > Settings > Project > Python Interpreter.  
2. Click on the + (Add) button and search for the required libraries.  
3. Install each library individually, or use the terminal in PyCharm and run the following commands:  
"bash
pip install numpy matplotlib pandas scipy scikit-learn seaborn opencv-python"
Alternatively, install individual packages:  
Library  Installation Command
NumPy  'pip install numpy' 
Matplotlib  'pip install matplotlib' 
Pandas  'pip install pandas' 
SciPy  'pip install scipy' 
Scikit-Learn  'pip install scikit-learn' 
Seaborn  'pip install seaborn' 
OpenCV  'pip install opencv-python' 
TensorFlow  'pip install tensorflow' 
Step 3: Running the Project
1. Open PyCharm and navigate to File > Open, then select the project folder.  
2. Open the main script or Jupyter Notebook file (e.g., 'Leaf_Disease_Prediction.py').  
3. Ensure that the dataset path in the script is correctly set.  
4. Run the python file by clicking the Run button or using the terminal command:  
 "app.py".
5. The system will open the website.  
6. They navigate through available options like Admin, Farmer, and New Farmer.  
7. Admin logs in to manage the system, oversee activities, and perform updates, then logs out.  
8. Farmer registers/logs in, uploads a leaf image for disease prediction, reviews the result, and logs out.  
9. Remedies system provides disease predictions with suggested prevention tips and treatment solutions for the farmer to take action.
10.After analysis, close the project.
