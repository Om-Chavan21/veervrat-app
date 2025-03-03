# # # # import requests
# # # # from typing import Dict

# # # # # Define the main virtues data
# # # # main_virtues_data = [
# # # #     {
# # # #         "item_code": "1.0.0",
# # # #         "name": {"en": "Self-Dependence", "mr": "स्वावलंबन"},
# # # #     },
# # # #     {
# # # #         "item_code": "2.0.0",
# # # #         "name": {"en": "Leadership", "mr": "नेतृत्व"},
# # # #     },
# # # #     {
# # # #         "item_code": "3.0.0",
# # # #         "name": {"en": "Industriousness", "mr": "उद्यमशीलता"},
# # # #     },
# # # #     {
# # # #         "item_code": "4.0.0",
# # # #         "name": {"en": "Righteous conflict", "mr": "संघर्ष"},
# # # #     },
# # # #     {
# # # #         "item_code": "5.0.0",
# # # #         "name": {"en": "Goal-motivation", "mr": "ध्येयप्रेरणा"},
# # # #     },
# # # #     {
# # # #         "item_code": "6.0.0",
# # # #         "name": {"en": "Reflection and Flexibility", "mr": "आत्मनिवेदन व लवचिकता"},
# # # #     },
# # # # ]

# # # # # Define the API endpoint URL
# # # # api_url = "http://192.168.31.52:8000/api/main-virtues/"


# # # # # Function to post data to the API
# # # # def post_main_virtue(data: Dict):
# # # #     try:
# # # #         response = requests.post(api_url, json=data)
# # # #         response.raise_for_status()  # Raise an exception for HTTP errors
# # # #         print(f"Main virtue created: {response.json()}")
# # # #     except requests.RequestException as e:
# # # #         print(f"Error creating main virtue: {e}")


# # # # # Post each main virtue to the API
# # # # for virtue in main_virtues_data:
# # # #     post_main_virtue(virtue)

# # #########################################################################################################################

# # # import requests

# # # # Define the API endpoint URL
# # # url = "http://localhost:8000/api/subvirtues/"  # Replace with your actual API URL

# # # # Define the data to be posted
# # # data_to_post = [
# # #     {
# # #         "item_code": "1.1.0",
# # #         "name": {"en": "Self-dependence in Thought", "mr": "वैचारिक स्वावलंबन"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f15",
# # #     },
# # #     {
# # #         "item_code": "1.1.1",
# # #         "name": {"en": "Root-Cause Orientation", "mr": "मुळातून शोध घेण्याची वृत्ती"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f15",
# # #     },
# # #     {
# # #         "item_code": "1.1.2",
# # #         "name": {"en": "Questioning Skills", "mr": "प्रश्नाभिमुखता"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f15",
# # #     },
# # #     {
# # #         "item_code": "1.2.0",
# # #         "name": {"en": "Financial Self-Dependence", "mr": "आर्थिक स्वावलंबन"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f15",
# # #     },
# # #     {
# # #         "item_code": "1.3.0",
# # #         "name": {"en": "Self-Dependence in gaining Skills", "mr": "कौशल्य स्वावलंबन"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f15",
# # #     },
# # #     {
# # #         "item_code": "1.4.0",
# # #         "name": {"en": "Emotional Self-dependence", "mr": "भावनिक स्वावलंबन"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f15",
# # #     },
# # #     {
# # #         "item_code": "1.4.1",
# # #         "name": {"en": "Not present in the list", "mr": "कार्यवाहीच्या वेळी निश्चळता"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f15",
# # #     },
# # #     {
# # #         "item_code": "1.4.2",
# # #         "name": {"en": "Not present in the list", "mr": "कार्यवाहीच्या वेळी दक्षता"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f15",
# # #     },
# # #     {
# # #         "item_code": "1.5.0",
# # #         "name": {"en": "Physical Self-Dependence", "mr": "शारीरिक स्वावलंबन"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f15",
# # #     },
# # #     {
# # #         "item_code": "2.1.0",
# # #         "name": {"en": "Communication skills", "mr": "संवादकौशल्य"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f16",
# # #     },
# # #     {
# # #         "item_code": "2.2.0",
# # #         "name": {"en": "Accountability / Responsibility", "mr": "उत्तरदायित्व"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f16",
# # #     },
# # #     {
# # #         "item_code": "2.3.0",
# # #         "name": {"en": "Organizational orientation", "mr": "संघटनाभिमुखता"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f16",
# # #     },
# # #     {
# # #         "item_code": "2.4.0",
# # #         "name": {"en": "Team/Group-building", "mr": "गटबांधणी"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f16",
# # #     },
# # #     {
# # #         "item_code": "3.1.0",
# # #         "name": {"en": "Planning Skills", "mr": "नियोजन कौशल्य"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f17",
# # #     },
# # #     {
# # #         "item_code": "3.2.0",
# # #         "name": {"en": "Execution Skills", "mr": "कार्यवाही कौशल्य"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f17",
# # #     },
# # #     {
# # #         "item_code": "3.3.0",
# # #         "name": {"en": "Resourcefulness", "mr": "हिकमतीपणा"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f17",
# # #     },
# # #     {
# # #         "item_code": "3.4.0",
# # #         "name": {"en": "Initiative/Enthusiasm", "mr": "उत्स्फूर्तीसंपन्नता"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f17",
# # #     },
# # #     {
# # #         "item_code": "3.5.0",
# # #         "name": {"en": "Multi-tasking", "mr": "अष्टावधानीपण"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f17",
# # #     },
# # #     {
# # #         "item_code": "3.6.0",
# # #         "name": {"en": "Novelty", "mr": "नाविन्य"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f17",
# # #     },
# # #     {
# # #         "item_code": "3.7.0",
# # #         "name": {"en": "Creativity", "mr": "प्रतिभा"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f17",
# # #     },
# # #     {
# # #         "item_code": "3.8.0",
# # #         "name": {"en": "Ambition", "mr": "महत्त्वाकांक्षा/भव्यता"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f17",
# # #     },
# # #     {
# # #         "item_code": "4.1.0",
# # #         "name": {"en": "Anger towards injustice", "mr": "अन्यायाची चीड"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f18",
# # #     },
# # #     {
# # #         "item_code": "4.2.0",
# # #         "name": {"en": "Social Welfare", "mr": "समाजहित जपणे"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f18",
# # #     },
# # #     {
# # #         "item_code": "4.3.0",
# # #         "name": {"en": "Resoluteness", "mr": "निर्धारशक्ति"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f18",
# # #     },
# # #     {
# # #         "item_code": "5.1.0",
# # #         "name": {"en": "Goal-orientation", "mr": "ध्येयाभिमुखता"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f19",
# # #     },
# # #     {
# # #         "item_code": "5.2.0",
# # #         "name": {"en": "Futuristic Thinking Skills", "mr": "भविष्यवेध कौशल्य"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f19",
# # #     },
# # #     {
# # #         "item_code": "5.3.0",
# # #         "name": {"en": "Steadfastedness", "mr": "सातत्य"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f19",
# # #     },
# # #     {
# # #         "item_code": "5.4.0",
# # #         "name": {"en": "Concern", "mr": "आस्था"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f19",
# # #     },
# # #     {
# # #         "item_code": "5.5.0",
# # #         "name": {"en": "Social Orientation", "mr": "समाजाभिमुखता"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f19",
# # #     },
# # #     {
# # #         "item_code": "5.6.0",
# # #         "name": {"en": "Conquering Mindset", "mr": "विजिगीषा"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f19",
# # #     },
# # #     {
# # #         "item_code": "6.1.0",
# # #         "name": {"en": "Self-reflection", "mr": "आत्मपरीक्षण"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f1a",
# # #     },
# # #     {
# # #         "item_code": "6.2.0",
# # #         "name": {"en": "Flexibility", "mr": "लवचिकता"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f1a",
# # #     },
# # #     {
# # #         "item_code": "6.3.0",
# # #         "name": {"en": "Upaasana", "mr": "उपासना"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f1a",
# # #     },
# # #     {
# # #         "item_code": "6.4.0",
# # #         "name": {"en": "Adaptability", "mr": "अनुकूलनवृत्ती"},
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f1a",
# # #     },
# # #     {
# # #         "item_code": "6.5.0",
# # #         "name": {
# # #             "en": "Self-detachment from decisions",
# # #             "mr": "निर्णयांपासून 'स्व' वेगळा काढता येणे",
# # #         },
# # #         "main_virtue_id": "67c35ab5e29cb45d8d2a7f1a",
# # #     },
# # # ]


# # # # Post each item in the data list
# # # for item in data_to_post:
# # #     try:
# # #         response = requests.post(url, json=item)
# # #         if response.status_code == 200:
# # #             print(
# # #                 f"Successfully posted item with code {item['item_code']}. Response: {response.text}"
# # #             )
# # #         else:
# # #             print(
# # #                 f"Failed to post item with code {item['item_code']}. Status code: {response.status_code}. Response: {response.text}"
# # #             )
# # #     except Exception as e:
# # #         print(
# # #             f"An error occurred while posting item with code {item['item_code']}: {e}"
# # #         )

# # #########################################################################################################################


# # # import csv
# # # import requests

# # # # Define the API endpoint URL
# # # url = "http://localhost:8000/api/questions/"

# # # # Define the CSV file path
# # # csv_file_path = "temp.csv"  # Replace with your actual CSV file path

# # # # Read the CSV file and POST each row to the API
# # # with open(csv_file_path, "r", encoding="utf-8") as file:
# # #     reader = csv.DictReader(file)
# # #     for row in reader:
# # #         try:
# # #             # Create the request body
# # #             data = {
# # #                 "item_code": row["Item code"],
# # #                 "content": {"en": row["en"], "mr": row["mr"]},
# # #                 "subvirtue_id": row["Subvirtue id"],
# # #             }

# # #             # POST the data to the API
# # #             response = requests.post(url, json=data)

# # #             if response.status_code == 200:
# # #                 print(
# # #                     f"Successfully posted question with code {row['Item code']}. Response: {response.text}"
# # #                 )
# # #             else:
# # #                 print(
# # #                     f"Failed to post question with code {row['Item code']}. Status code: {response.status_code}. Response: {response.text}"
# # #                 )
# # #         except Exception as e:
# # #             print(
# # #                 f"An error occurred while posting question with code {row['Item code']}: {e}"
# # #             )
# # #########################################################################################################################
# # import pandas as pd


# # # Load initial data from CSV
# # def load_initial_data(csv_file_path):
# #     try:
# #         df_initial = pd.read_csv(csv_file_path)
# #         return df_initial
# #     except Exception as e:
# #         print(f"Failed to load CSV: {e}")
# #         return None


# # # Load subvirtues data
# # def load_subvirtues_data(subvirtues_data):
# #     df_subvirtues = pd.DataFrame(subvirtues_data)
# #     return df_subvirtues


# # # Update Subvirtue IDs
# # def update_subvirtue_ids(df_initial, df_subvirtues):
# #     # Create a dictionary mapping item_code to _id for efficient lookup
# #     subvirtue_id_map = df_subvirtues.set_index("item_code")["_id"].to_dict()

# #     # Function to update a single list of IDs
# #     def update_ids(id_list):
# #         ids = [id.strip() for id in id_list.split(",")]
# #         updated_ids = [subvirtue_id_map.get(id) for id in ids if id in subvirtue_id_map]
# #         return ", ".join(updated_ids)

# #     # Update the 'subvirtue_id' column in the initial DataFrame
# #     df_initial["subvirtue_id"] = df_initial["subvirtue_id"].apply(update_ids)

# #     return df_initial


# # # Save updated DataFrame to CSV
# # def save_to_csv(df, csv_file_path):
# #     try:
# #         df.to_csv(csv_file_path, index=False)
# #         print("CSV updated successfully.")
# #     except Exception as e:
# #         print(f"Failed to save CSV: {e}")


# # # Main function
# # def main():
# #     csv_file_path = "Weaknesses_data.csv"  # Replace with your CSV file path
# #     subvirtues_data = [
# #         {
# #             "_id": "67c3fc274b66c21fff706773",
# #             "item_code": "1.1.0",
# #             "name": {"en": "Self-dependence in Thought", "mr": "वैचारिक स्वावलंबन"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f15",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f15",
# #                 "item_code": "1.0.0",
# #                 "name": {"en": "Self-Dependence", "mr": "स्वावलंबन"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc274b66c21fff706774",
# #             "item_code": "1.1.1",
# #             "name": {"en": "Root-Cause Orientation", "mr": "मुळातून शोध घेण्याची वृत्ती"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f15",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f15",
# #                 "item_code": "1.0.0",
# #                 "name": {"en": "Self-Dependence", "mr": "स्वावलंबन"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc284b66c21fff706775",
# #             "item_code": "1.1.2",
# #             "name": {"en": "Questioning Skills", "mr": "प्रश्नाभिमुखता"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f15",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f15",
# #                 "item_code": "1.0.0",
# #                 "name": {"en": "Self-Dependence", "mr": "स्वावलंबन"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc294b66c21fff706776",
# #             "item_code": "1.2.0",
# #             "name": {"en": "Financial Self-Dependence", "mr": "आर्थिक स्वावलंबन"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f15",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f15",
# #                 "item_code": "1.0.0",
# #                 "name": {"en": "Self-Dependence", "mr": "स्वावलंबन"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc294b66c21fff706777",
# #             "item_code": "1.3.0",
# #             "name": {"en": "Self-Dependence in gaining Skills", "mr": "कौशल्य स्वावलंबन"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f15",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f15",
# #                 "item_code": "1.0.0",
# #                 "name": {"en": "Self-Dependence", "mr": "स्वावलंबन"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc2a4b66c21fff706778",
# #             "item_code": "1.4.0",
# #             "name": {"en": "Emotional Self-dependence", "mr": "भावनिक स्वावलंबन"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f15",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f15",
# #                 "item_code": "1.0.0",
# #                 "name": {"en": "Self-Dependence", "mr": "स्वावलंबन"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc2a4b66c21fff706779",
# #             "item_code": "1.4.1",
# #             "name": {"en": "Not present in the list", "mr": "कार्यवाहीच्या वेळी निश्चळता"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f15",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f15",
# #                 "item_code": "1.0.0",
# #                 "name": {"en": "Self-Dependence", "mr": "स्वावलंबन"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc2b4b66c21fff70677a",
# #             "item_code": "1.4.2",
# #             "name": {"en": "Not present in the list", "mr": "कार्यवाहीच्या वेळी दक्षता"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f15",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f15",
# #                 "item_code": "1.0.0",
# #                 "name": {"en": "Self-Dependence", "mr": "स्वावलंबन"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc2c4b66c21fff70677b",
# #             "item_code": "1.5.0",
# #             "name": {"en": "Physical Self-Dependence", "mr": "शारीरिक स्वावलंबन"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f15",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f15",
# #                 "item_code": "1.0.0",
# #                 "name": {"en": "Self-Dependence", "mr": "स्वावलंबन"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc2c4b66c21fff70677c",
# #             "item_code": "2.1.0",
# #             "name": {"en": "Communication skills", "mr": "संवादकौशल्य"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f16",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f16",
# #                 "item_code": "2.0.0",
# #                 "name": {"en": "Leadership", "mr": "नेतृत्व"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc2d4b66c21fff70677d",
# #             "item_code": "2.2.0",
# #             "name": {"en": "Accountability / Responsibility", "mr": "उत्तरदायित्व"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f16",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f16",
# #                 "item_code": "2.0.0",
# #                 "name": {"en": "Leadership", "mr": "नेतृत्व"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc2d4b66c21fff70677e",
# #             "item_code": "2.3.0",
# #             "name": {"en": "Organizational orientation", "mr": "संघटनाभिमुखता"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f16",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f16",
# #                 "item_code": "2.0.0",
# #                 "name": {"en": "Leadership", "mr": "नेतृत्व"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc2e4b66c21fff70677f",
# #             "item_code": "2.4.0",
# #             "name": {"en": "Team/Group-building", "mr": "गटबांधणी"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f16",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f16",
# #                 "item_code": "2.0.0",
# #                 "name": {"en": "Leadership", "mr": "नेतृत्व"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc2f4b66c21fff706780",
# #             "item_code": "3.1.0",
# #             "name": {"en": "Planning Skills", "mr": "नियोजन कौशल्य"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f17",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f17",
# #                 "item_code": "3.0.0",
# #                 "name": {"en": "Industriousness", "mr": "उद्यमशीलता"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc2f4b66c21fff706781",
# #             "item_code": "3.2.0",
# #             "name": {"en": "Execution Skills", "mr": "कार्यवाही कौशल्य"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f17",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f17",
# #                 "item_code": "3.0.0",
# #                 "name": {"en": "Industriousness", "mr": "उद्यमशीलता"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc304b66c21fff706782",
# #             "item_code": "3.3.0",
# #             "name": {"en": "Resourcefulness", "mr": "हिकमतीपणा"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f17",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f17",
# #                 "item_code": "3.0.0",
# #                 "name": {"en": "Industriousness", "mr": "उद्यमशीलता"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc314b66c21fff706783",
# #             "item_code": "3.4.0",
# #             "name": {"en": "Initiative/Enthusiasm", "mr": "उत्स्फूर्तीसंपन्नता"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f17",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f17",
# #                 "item_code": "3.0.0",
# #                 "name": {"en": "Industriousness", "mr": "उद्यमशीलता"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc314b66c21fff706784",
# #             "item_code": "3.5.0",
# #             "name": {"en": "Multi-tasking", "mr": "अष्टावधानीपण"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f17",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f17",
# #                 "item_code": "3.0.0",
# #                 "name": {"en": "Industriousness", "mr": "उद्यमशीलता"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc324b66c21fff706785",
# #             "item_code": "3.6.0",
# #             "name": {"en": "Novelty", "mr": "नाविन्य"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f17",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f17",
# #                 "item_code": "3.0.0",
# #                 "name": {"en": "Industriousness", "mr": "उद्यमशीलता"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc334b66c21fff706786",
# #             "item_code": "3.7.0",
# #             "name": {"en": "Creativity", "mr": "प्रतिभा"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f17",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f17",
# #                 "item_code": "3.0.0",
# #                 "name": {"en": "Industriousness", "mr": "उद्यमशीलता"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc334b66c21fff706787",
# #             "item_code": "3.8.0",
# #             "name": {"en": "Ambition", "mr": "महत्त्वाकांक्षा/भव्यता"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f17",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f17",
# #                 "item_code": "3.0.0",
# #                 "name": {"en": "Industriousness", "mr": "उद्यमशीलता"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc344b66c21fff706788",
# #             "item_code": "4.1.0",
# #             "name": {"en": "Anger towards injustice", "mr": "अन्यायाची चीड"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f18",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f18",
# #                 "item_code": "4.0.0",
# #                 "name": {"en": "Righteous conflict", "mr": "संघर्ष"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc344b66c21fff706789",
# #             "item_code": "4.2.0",
# #             "name": {"en": "Social Welfare", "mr": "समाजहित जपणे"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f18",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f18",
# #                 "item_code": "4.0.0",
# #                 "name": {"en": "Righteous conflict", "mr": "संघर्ष"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc354b66c21fff70678a",
# #             "item_code": "4.3.0",
# #             "name": {"en": "Resoluteness", "mr": "निर्धारशक्ति"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f18",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f18",
# #                 "item_code": "4.0.0",
# #                 "name": {"en": "Righteous conflict", "mr": "संघर्ष"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc364b66c21fff70678b",
# #             "item_code": "5.1.0",
# #             "name": {"en": "Goal-orientation", "mr": "ध्येयाभिमुखता"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f19",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f19",
# #                 "item_code": "5.0.0",
# #                 "name": {"en": "Goal-motivation", "mr": "ध्येयप्रेरणा"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc364b66c21fff70678c",
# #             "item_code": "5.2.0",
# #             "name": {"en": "Futuristic Thinking Skills", "mr": "भविष्यवेध कौशल्य"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f19",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f19",
# #                 "item_code": "5.0.0",
# #                 "name": {"en": "Goal-motivation", "mr": "ध्येयप्रेरणा"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc374b66c21fff70678d",
# #             "item_code": "5.3.0",
# #             "name": {"en": "Steadfastedness", "mr": "सातत्य"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f19",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f19",
# #                 "item_code": "5.0.0",
# #                 "name": {"en": "Goal-motivation", "mr": "ध्येयप्रेरणा"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc374b66c21fff70678e",
# #             "item_code": "5.4.0",
# #             "name": {"en": "Concern", "mr": "आस्था"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f19",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f19",
# #                 "item_code": "5.0.0",
# #                 "name": {"en": "Goal-motivation", "mr": "ध्येयप्रेरणा"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc384b66c21fff70678f",
# #             "item_code": "5.5.0",
# #             "name": {"en": "Social Orientation", "mr": "समाजाभिमुखता"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f19",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f19",
# #                 "item_code": "5.0.0",
# #                 "name": {"en": "Goal-motivation", "mr": "ध्येयप्रेरणा"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc394b66c21fff706790",
# #             "item_code": "5.6.0",
# #             "name": {"en": "Conquering Mindset", "mr": "विजिगीषा"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f19",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f19",
# #                 "item_code": "5.0.0",
# #                 "name": {"en": "Goal-motivation", "mr": "ध्येयप्रेरणा"},
# #             },
# #         },
# #         {
# #             "_id": "67c3fc394b66c21fff706791",
# #             "item_code": "6.1.0",
# #             "name": {"en": "Self-reflection", "mr": "आत्मपरीक्षण"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f1a",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f1a",
# #                 "item_code": "6.0.0",
# #                 "name": {
# #                     "en": "Reflection and Flexibility",
# #                     "mr": "आत्मनिवेदन व लवचिकता",
# #                 },
# #             },
# #         },
# #         {
# #             "_id": "67c3fc3a4b66c21fff706792",
# #             "item_code": "6.2.0",
# #             "name": {"en": "Flexibility", "mr": "लवचिकता"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f1a",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f1a",
# #                 "item_code": "6.0.0",
# #                 "name": {
# #                     "en": "Reflection and Flexibility",
# #                     "mr": "आत्मनिवेदन व लवचिकता",
# #                 },
# #             },
# #         },
# #         {
# #             "_id": "67c3fc3a4b66c21fff706793",
# #             "item_code": "6.3.0",
# #             "name": {"en": "Upaasana", "mr": "उपासना"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f1a",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f1a",
# #                 "item_code": "6.0.0",
# #                 "name": {
# #                     "en": "Reflection and Flexibility",
# #                     "mr": "आत्मनिवेदन व लवचिकता",
# #                 },
# #             },
# #         },
# #         {
# #             "_id": "67c3fc3b4b66c21fff706794",
# #             "item_code": "6.4.0",
# #             "name": {"en": "Adaptability", "mr": "अनुकूलनवृत्ती"},
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f1a",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f1a",
# #                 "item_code": "6.0.0",
# #                 "name": {
# #                     "en": "Reflection and Flexibility",
# #                     "mr": "आत्मनिवेदन व लवचिकता",
# #                 },
# #             },
# #         },
# #         {
# #             "_id": "67c3fc3b4b66c21fff706795",
# #             "item_code": "6.5.0",
# #             "name": {
# #                 "en": "Self-detachment from decisions",
# #                 "mr": "निर्णयांपासून 'स्व' वेगळा काढता येणे",
# #             },
# #             "main_virtue_id": "67c35ab5e29cb45d8d2a7f1a",
# #             "main_virtue": {
# #                 "_id": "67c35ab5e29cb45d8d2a7f1a",
# #                 "item_code": "6.0.0",
# #                 "name": {
# #                     "en": "Reflection and Flexibility",
# #                     "mr": "आत्मनिवेदन व लवचिकता",
# #                 },
# #             },
# #         },
# #     ]

# #     df_initial = load_initial_data(csv_file_path)
# #     if df_initial is not None:
# #         df_subvirtues = load_subvirtues_data(subvirtues_data)
# #         df_updated = update_subvirtue_ids(df_initial, df_subvirtues)
# #         save_to_csv(df_updated, csv_file_path)


# # if __name__ == "__main__":
# #     main()


# ############

# import csv
# import json
# import requests


# def csv_to_json(csv_file_path):
#     data = []
#     with open(csv_file_path, encoding="utf-8") as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         for row in csv_reader:
#             item = {
#                 "item_code": row["Item code"],
#                 "name": {"en": row["en"], "mr": row["mr"]},
#                 "group": row["Group"],
#                 "suggested_subvirtue_ids": row["subvirtue_id"].split(", "),
#             }
#             data.append(item)
#     return data


# def post_to_api(json_data):
#     url = "http://localhost:8000/api/weaknesses"
#     for item in json_data:
#         response = requests.post(url, json=item)
#         print(f"Response for item {item['item_code']}: {response.status_code}")


# # Main execution
# csv_file_path = "Weaknesses_data.csv"  # Replace with your CSV file path
# json_data = csv_to_json(csv_file_path)
# post_to_api(json_data)

####################

import requests
from typing import Dict

# Define the API endpoint URL
api_url = "http://localhost:8000/api/dals/"  # Replace with your actual API URL

# Define the data to post
dals_data = [
    {
        "item_code": "D001",
        "name": {
            "en": "Sena Sarkhel Kanhoji Angre Dal",
            "mr": "सेना सरखेल कान्होजी आंग्रे दल",
        },
        "short_name": {"en": "Angre Dal", "mr": "आंग्रे दल"},
        "type": {"en": "Krida Dal", "mr": "क्रीडा दल"},
        "email": "angre.dal@jnanaprabodhini.org",
    },
    {
        "item_code": "D002",
        "name": {"en": "Chandrashekhar Azad Dal", "mr": "चंद्रशेखर आझाद दल"},
        "short_name": {"en": "Azad Dal", "mr": "आझाद दल"},
        "type": {"en": "Krida Dal", "mr": "क्रीडा दल"},
        "email": "azad.dal@jnanaprabodhini.org",
    },
    {
        "item_code": "D003",
        "name": {"en": "Dr. Homi Jehangir Bhabha Dal", "mr": "डॉ. होमी जहांगीर भाभा दल"},
        "short_name": {"en": "Bhabha Dal", "mr": "भाभा दल"},
        "type": {"en": "Vijnana Dal", "mr": "विज्ञान दल"},
        "email": "bhabha.dal@jnanaprabodhini.org",
    },
    {
        "item_code": "D004",
        "name": {
            "en": "Netaji Subhash Chandra Bose Dal",
            "mr": "नेताजी सुभाष चंद्र बोस दल",
        },
        "short_name": {"en": "Bose Dal", "mr": "बोस दल"},
        "type": {"en": "Krida Dal", "mr": "क्रीडा दल"},
        "email": "bose.dal@jnanaprabodhini.org",
    },
    {
        "item_code": "D005",
        "name": {"en": "Dr. Vikram Sarabhai Dal", "mr": "डॉ. विक्रम साराभाई दल"},
        "short_name": {"en": "Sarabhai Dal", "mr": "साराभाई दल"},
        "type": {"en": "Vijnana Dal", "mr": "विज्ञान दल"},
        "email": "sarabhai.dal@jnanaprabodhini.org",
    },
    {
        "item_code": "D006",
        "name": {
            "en": "Bharatratna Lal Bahadur Shastri Dal",
            "mr": "भारतरत्न लाल बहादूर शास्त्री दल",
        },
        "short_name": {"en": "Shastri Dal", "mr": "शास्त्री दल"},
        "type": {"en": "Krida Dal", "mr": "क्रीडा दल"},
        "email": "shastri.dal@jnanaprabodhini.org",
    },
    {
        "item_code": "D007",
        "name": {
            "en": "Lokmanya Bal Gangadhar Tilak Dal",
            "mr": "लोकमान्य बाळ गंगाधर टिळक दल",
        },
        "short_name": {"en": "Tilak Dal", "mr": "टिळक दल"},
        "type": {"en": "Krida Dal", "mr": "क्रीडा दल"},
        "email": "tilak.dal@jnanaprabodhini.org",
    },
    {
        "item_code": "D008",
        "name": {
            "en": "Bharatratna Mokshagundam Visvesvaraya Dal",
            "mr": "भारतरत्न मोक्षगुंडम विश्वेश्वरय्या दल",
        },
        "short_name": {"en": "Visvesvaraya Dal", "mr": "विश्वेश्वरया दल"},
        "type": {"en": "Vijnana Dal", "mr": "विज्ञान दल"},
        "email": "visvesvaraya.dal@jnanaprabodhini.org",
    },
]


def post_dal(data: Dict):
    try:
        response = requests.post(api_url, json=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(f"Successfully posted {data['item_code']}")
    except requests.exceptions.RequestException as e:
        print(f"Error posting {data['item_code']}: {e}")


# Post each item
for dal in dals_data:
    post_dal(dal)
