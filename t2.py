import pandas as pd


# Load initial data from CSV
def load_initial_data(csv_file_path):
    try:
        df_initial = pd.read_csv(csv_file_path)
        return df_initial
    except Exception as e:
        print(f"Failed to load CSV: {e}")
        return None


# Load subvirtues data
def load_subvirtues_data(subvirtues_data):
    df_subvirtues = pd.DataFrame(subvirtues_data)
    return df_subvirtues


# Update Subvirtue IDs
def update_subvirtue_ids(df_initial, df_subvirtues):
    # Create a dictionary mapping item_code to _id for efficient lookup
    subvirtue_id_map = df_subvirtues.set_index("item_code")["_id"].to_dict()

    # Update the 'Subvirtue id' column in the initial DataFrame
    df_initial["Subvirtue id"] = df_initial["Subvirtue id"].apply(
        lambda x: subvirtue_id_map.get(x)
    )

    return df_initial


# Save updated DataFrame to CSV
def save_to_csv(df, csv_file_path):
    try:
        df.to_csv(csv_file_path, index=False)
        print("CSV updated successfully.")
    except Exception as e:
        print(f"Failed to save CSV: {e}")


# Main function
def main():
    csv_file_path = "temp.csv"  # Replace with your CSV file path
    # Subvirtues data
    subvirtues_data = [
        {
            "_id": "67c3fc274b66c21fff706773",
            "item_code": "1.1.0",
            "name": {"en": "Self-dependence in Thought", "mr": "वैचारिक स्वावलंबन"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f15",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f15",
                "item_code": "1.0.0",
                "name": {"en": "Self-Dependence", "mr": "स्वावलंबन"},
            },
        },
        {
            "_id": "67c3fc274b66c21fff706774",
            "item_code": "1.1.1",
            "name": {"en": "Root-Cause Orientation", "mr": "मुळातून शोध घेण्याची वृत्ती"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f15",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f15",
                "item_code": "1.0.0",
                "name": {"en": "Self-Dependence", "mr": "स्वावलंबन"},
            },
        },
        {
            "_id": "67c3fc284b66c21fff706775",
            "item_code": "1.1.2",
            "name": {"en": "Questioning Skills", "mr": "प्रश्नाभिमुखता"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f15",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f15",
                "item_code": "1.0.0",
                "name": {"en": "Self-Dependence", "mr": "स्वावलंबन"},
            },
        },
        {
            "_id": "67c3fc294b66c21fff706776",
            "item_code": "1.2.0",
            "name": {"en": "Financial Self-Dependence", "mr": "आर्थिक स्वावलंबन"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f15",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f15",
                "item_code": "1.0.0",
                "name": {"en": "Self-Dependence", "mr": "स्वावलंबन"},
            },
        },
        {
            "_id": "67c3fc294b66c21fff706777",
            "item_code": "1.3.0",
            "name": {"en": "Self-Dependence in gaining Skills", "mr": "कौशल्य स्वावलंबन"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f15",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f15",
                "item_code": "1.0.0",
                "name": {"en": "Self-Dependence", "mr": "स्वावलंबन"},
            },
        },
        {
            "_id": "67c3fc2a4b66c21fff706778",
            "item_code": "1.4.0",
            "name": {"en": "Emotional Self-dependence", "mr": "भावनिक स्वावलंबन"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f15",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f15",
                "item_code": "1.0.0",
                "name": {"en": "Self-Dependence", "mr": "स्वावलंबन"},
            },
        },
        {
            "_id": "67c3fc2a4b66c21fff706779",
            "item_code": "1.4.1",
            "name": {"en": "Not present in the list", "mr": "कार्यवाहीच्या वेळी निश्चळता"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f15",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f15",
                "item_code": "1.0.0",
                "name": {"en": "Self-Dependence", "mr": "स्वावलंबन"},
            },
        },
        {
            "_id": "67c3fc2b4b66c21fff70677a",
            "item_code": "1.4.2",
            "name": {"en": "Not present in the list", "mr": "कार्यवाहीच्या वेळी दक्षता"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f15",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f15",
                "item_code": "1.0.0",
                "name": {"en": "Self-Dependence", "mr": "स्वावलंबन"},
            },
        },
        {
            "_id": "67c3fc2c4b66c21fff70677b",
            "item_code": "1.5.0",
            "name": {"en": "Physical Self-Dependence", "mr": "शारीरिक स्वावलंबन"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f15",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f15",
                "item_code": "1.0.0",
                "name": {"en": "Self-Dependence", "mr": "स्वावलंबन"},
            },
        },
        {
            "_id": "67c3fc2c4b66c21fff70677c",
            "item_code": "2.1.0",
            "name": {"en": "Communication skills", "mr": "संवादकौशल्य"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f16",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f16",
                "item_code": "2.0.0",
                "name": {"en": "Leadership", "mr": "नेतृत्व"},
            },
        },
        {
            "_id": "67c3fc2d4b66c21fff70677d",
            "item_code": "2.2.0",
            "name": {"en": "Accountability / Responsibility", "mr": "उत्तरदायित्व"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f16",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f16",
                "item_code": "2.0.0",
                "name": {"en": "Leadership", "mr": "नेतृत्व"},
            },
        },
        {
            "_id": "67c3fc2d4b66c21fff70677e",
            "item_code": "2.3.0",
            "name": {"en": "Organizational orientation", "mr": "संघटनाभिमुखता"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f16",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f16",
                "item_code": "2.0.0",
                "name": {"en": "Leadership", "mr": "नेतृत्व"},
            },
        },
        {
            "_id": "67c3fc2e4b66c21fff70677f",
            "item_code": "2.4.0",
            "name": {"en": "Team/Group-building", "mr": "गटबांधणी"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f16",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f16",
                "item_code": "2.0.0",
                "name": {"en": "Leadership", "mr": "नेतृत्व"},
            },
        },
        {
            "_id": "67c3fc2f4b66c21fff706780",
            "item_code": "3.1.0",
            "name": {"en": "Planning Skills", "mr": "नियोजन कौशल्य"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f17",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f17",
                "item_code": "3.0.0",
                "name": {"en": "Industriousness", "mr": "उद्यमशीलता"},
            },
        },
        {
            "_id": "67c3fc2f4b66c21fff706781",
            "item_code": "3.2.0",
            "name": {"en": "Execution Skills", "mr": "कार्यवाही कौशल्य"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f17",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f17",
                "item_code": "3.0.0",
                "name": {"en": "Industriousness", "mr": "उद्यमशीलता"},
            },
        },
        {
            "_id": "67c3fc304b66c21fff706782",
            "item_code": "3.3.0",
            "name": {"en": "Resourcefulness", "mr": "हिकमतीपणा"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f17",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f17",
                "item_code": "3.0.0",
                "name": {"en": "Industriousness", "mr": "उद्यमशीलता"},
            },
        },
        {
            "_id": "67c3fc314b66c21fff706783",
            "item_code": "3.4.0",
            "name": {"en": "Initiative/Enthusiasm", "mr": "उत्स्फूर्तीसंपन्नता"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f17",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f17",
                "item_code": "3.0.0",
                "name": {"en": "Industriousness", "mr": "उद्यमशीलता"},
            },
        },
        {
            "_id": "67c3fc314b66c21fff706784",
            "item_code": "3.5.0",
            "name": {"en": "Multi-tasking", "mr": "अष्टावधानीपण"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f17",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f17",
                "item_code": "3.0.0",
                "name": {"en": "Industriousness", "mr": "उद्यमशीलता"},
            },
        },
        {
            "_id": "67c3fc324b66c21fff706785",
            "item_code": "3.6.0",
            "name": {"en": "Novelty", "mr": "नाविन्य"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f17",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f17",
                "item_code": "3.0.0",
                "name": {"en": "Industriousness", "mr": "उद्यमशीलता"},
            },
        },
        {
            "_id": "67c3fc334b66c21fff706786",
            "item_code": "3.7.0",
            "name": {"en": "Creativity", "mr": "प्रतिभा"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f17",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f17",
                "item_code": "3.0.0",
                "name": {"en": "Industriousness", "mr": "उद्यमशीलता"},
            },
        },
        {
            "_id": "67c3fc334b66c21fff706787",
            "item_code": "3.8.0",
            "name": {"en": "Ambition", "mr": "महत्त्वाकांक्षा/भव्यता"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f17",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f17",
                "item_code": "3.0.0",
                "name": {"en": "Industriousness", "mr": "उद्यमशीलता"},
            },
        },
        {
            "_id": "67c3fc344b66c21fff706788",
            "item_code": "4.1.0",
            "name": {"en": "Anger towards injustice", "mr": "अन्यायाची चीड"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f18",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f18",
                "item_code": "4.0.0",
                "name": {"en": "Righteous conflict", "mr": "संघर्ष"},
            },
        },
        {
            "_id": "67c3fc344b66c21fff706789",
            "item_code": "4.2.0",
            "name": {"en": "Social Welfare", "mr": "समाजहित जपणे"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f18",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f18",
                "item_code": "4.0.0",
                "name": {"en": "Righteous conflict", "mr": "संघर्ष"},
            },
        },
        {
            "_id": "67c3fc354b66c21fff70678a",
            "item_code": "4.3.0",
            "name": {"en": "Resoluteness", "mr": "निर्धारशक्ति"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f18",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f18",
                "item_code": "4.0.0",
                "name": {"en": "Righteous conflict", "mr": "संघर्ष"},
            },
        },
        {
            "_id": "67c3fc364b66c21fff70678b",
            "item_code": "5.1.0",
            "name": {"en": "Goal-orientation", "mr": "ध्येयाभिमुखता"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f19",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f19",
                "item_code": "5.0.0",
                "name": {"en": "Goal-motivation", "mr": "ध्येयप्रेरणा"},
            },
        },
        {
            "_id": "67c3fc364b66c21fff70678c",
            "item_code": "5.2.0",
            "name": {"en": "Futuristic Thinking Skills", "mr": "भविष्यवेध कौशल्य"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f19",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f19",
                "item_code": "5.0.0",
                "name": {"en": "Goal-motivation", "mr": "ध्येयप्रेरणा"},
            },
        },
        {
            "_id": "67c3fc374b66c21fff70678d",
            "item_code": "5.3.0",
            "name": {"en": "Steadfastedness", "mr": "सातत्य"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f19",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f19",
                "item_code": "5.0.0",
                "name": {"en": "Goal-motivation", "mr": "ध्येयप्रेरणा"},
            },
        },
        {
            "_id": "67c3fc374b66c21fff70678e",
            "item_code": "5.4.0",
            "name": {"en": "Concern", "mr": "आस्था"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f19",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f19",
                "item_code": "5.0.0",
                "name": {"en": "Goal-motivation", "mr": "ध्येयप्रेरणा"},
            },
        },
        {
            "_id": "67c3fc384b66c21fff70678f",
            "item_code": "5.5.0",
            "name": {"en": "Social Orientation", "mr": "समाजाभिमुखता"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f19",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f19",
                "item_code": "5.0.0",
                "name": {"en": "Goal-motivation", "mr": "ध्येयप्रेरणा"},
            },
        },
        {
            "_id": "67c3fc394b66c21fff706790",
            "item_code": "5.6.0",
            "name": {"en": "Conquering Mindset", "mr": "विजिगीषा"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f19",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f19",
                "item_code": "5.0.0",
                "name": {"en": "Goal-motivation", "mr": "ध्येयप्रेरणा"},
            },
        },
        {
            "_id": "67c3fc394b66c21fff706791",
            "item_code": "6.1.0",
            "name": {"en": "Self-reflection", "mr": "आत्मपरीक्षण"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f1a",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f1a",
                "item_code": "6.0.0",
                "name": {
                    "en": "Reflection and Flexibility",
                    "mr": "आत्मनिवेदन व लवचिकता",
                },
            },
        },
        {
            "_id": "67c3fc3a4b66c21fff706792",
            "item_code": "6.2.0",
            "name": {"en": "Flexibility", "mr": "लवचिकता"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f1a",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f1a",
                "item_code": "6.0.0",
                "name": {
                    "en": "Reflection and Flexibility",
                    "mr": "आत्मनिवेदन व लवचिकता",
                },
            },
        },
        {
            "_id": "67c3fc3a4b66c21fff706793",
            "item_code": "6.3.0",
            "name": {"en": "Upaasana", "mr": "उपासना"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f1a",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f1a",
                "item_code": "6.0.0",
                "name": {
                    "en": "Reflection and Flexibility",
                    "mr": "आत्मनिवेदन व लवचिकता",
                },
            },
        },
        {
            "_id": "67c3fc3b4b66c21fff706794",
            "item_code": "6.4.0",
            "name": {"en": "Adaptability", "mr": "अनुकूलनवृत्ती"},
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f1a",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f1a",
                "item_code": "6.0.0",
                "name": {
                    "en": "Reflection and Flexibility",
                    "mr": "आत्मनिवेदन व लवचिकता",
                },
            },
        },
        {
            "_id": "67c3fc3b4b66c21fff706795",
            "item_code": "6.5.0",
            "name": {
                "en": "Self-detachment from decisions",
                "mr": "निर्णयांपासून 'स्व' वेगळा काढता येणे",
            },
            "main_virtue_id": "67c35ab5e29cb45d8d2a7f1a",
            "main_virtue": {
                "_id": "67c35ab5e29cb45d8d2a7f1a",
                "item_code": "6.0.0",
                "name": {
                    "en": "Reflection and Flexibility",
                    "mr": "आत्मनिवेदन व लवचिकता",
                },
            },
        },
    ]

    df_initial = load_initial_data(csv_file_path)
    if df_initial is not None:
        df_subvirtues = load_subvirtues_data(subvirtues_data)
        df_updated = update_subvirtue_ids(df_initial, df_subvirtues)
        save_to_csv(df_updated, csv_file_path)


if __name__ == "__main__":
    main()
