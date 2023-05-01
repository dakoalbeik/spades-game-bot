import graphviz
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.tree import export_graphviz


# Function to load the data from a CSV file
def load_data(csv_file):
    data = pd.read_csv(csv_file)
    return data


# Function to split the data into training and testing sets
def split_data(data, features, target, test_size=0.2, random_state=42):
    X = data[features]
    y = data[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test


# Function to apply the Random Forest Classifier
def apply_random_forest(X_train, y_train, n_estimators=100, random_state=42):
    classifier = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
    classifier.fit(X_train, y_train)
    return classifier


# Function to evaluate the classifier
def evaluate_classifier(classifier, X_test, y_test):
    y_pred = classifier.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))


# Function to visualize a single decision tree from the Random Forest
def visualize_tree(tree, feature_names, class_names, out_file=None):
    dot_data = export_graphviz(tree, out_file=out_file, filled=True, rounded=True,
                               feature_names=feature_names, class_names=class_names,
                               special_characters=True)
    graph = graphviz.Source(dot_data)
    return graph


def main():
    data = load_data("C:\\Users\\brand\\Desktop\\avg_tricks_won.csv")

    # Specify the feature columns and the target column
    features = ['num_spades', 'sum_spades_values', 'num_nt_aces', 'num_nt_kings', 'num_void_suits']
    target = 'avg_num_tricks_won'  # Replace with your target column name

    X_train, X_test, y_train, y_test = split_data(data, features, target)

    classifier = apply_random_forest(X_train, y_train)

    print("\nRandom Forest Classifier Results:")
    evaluate_classifier(classifier, X_test, y_test)

    unique_classes = np.unique(y_train)
    class_names = [str(cls) for cls in unique_classes]

    # Visualize a single decision tree from the Random Forest
    tree = classifier.estimators_[0]  # Choose a tree index (0 to n_estimators - 1)
    graph = visualize_tree(tree, features, class_names=class_names)
    graph.render("decision_tree", format='png', cleanup=True)
    graph.view()


if __name__ == "__main__":
    main()
