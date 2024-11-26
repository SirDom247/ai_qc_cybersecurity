# AI Integration in Quantum Computing for Crytanalysis
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Generate Hypothetical Data
data = {
    "RSA_Key_Size": [15, 21, 35, 39, 77, 91],
    "Qubit_Count": [5, 5, 9, 9, 27, 27],
    "Backend_Latency_ms": [120, 110, 250, 240, 800, 780],
    "Noise_Level": [0.02, 0.03, 0.05, 0.05, 0.1, 0.1],
    "Success_Rate": [1, 1, 0, 0, 0, 0],  # Binary: 1=Success, 0=Fail
}
df = pd.DataFrame(data)

# Step 2: Data Preprocessing
X = df[["RSA_Key_Size", "Qubit_Count", "Backend_Latency_ms", "Noise_Level"]]
y = df["Success_Rate"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Logistic Regression Model
log_model = LogisticRegression()
log_model.fit(X_train, y_train)
log_preds = log_model.predict(X_test)

# Step 4: Neural Network Model
nn_model = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=1000, random_state=42)
nn_model.fit(X_train, y_train)
nn_preds = nn_model.predict(X_test)

# Step 5: Model Evaluation
print("Logistic Regression Accuracy:", accuracy_score(y_test, log_preds))
print("Neural Network Accuracy:", accuracy_score(y_test, nn_preds))
print("\nLogistic Regression Report:")
print(classification_report(y_test, log_preds))
print("\nNeural Network Report:")
print(classification_report(y_test, nn_preds))

# Step 6: Visualization
# Plot success rate trends
plt.figure(figsize=(10, 6))
sns.barplot(x="RSA_Key_Size", y="Success_Rate", hue="Qubit_Count", data=df, palette="viridis")
plt.title("Success Rates by RSA Key Size and Qubit Count")
plt.ylabel("Success Rate")
plt.xlabel("RSA Key Size")
plt.show()

# Plot backend performance
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x="Backend_Latency_ms", y="Noise_Level", hue="Success_Rate", size="Qubit_Count", data=df, palette="cool", sizes=(50, 200)
)
plt.title("Backend Latency vs Noise Level")
plt.xlabel("Backend Latency (ms)")
plt.ylabel("Noise Level")
plt.legend(title="Success Rate")
plt.show()

