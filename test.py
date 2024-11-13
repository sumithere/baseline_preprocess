import os

csv_path = "F:\\vit_fmow\\SatMAE\\data\\processed_images_metadata_train.csv"

if not os.path.exists(csv_path):
    print(f"File not found: {csv_path}")
else:
    print(f"File exists: {csv_path}")
    
    

current_path = os.getcwd()
print("Current directory:", current_path)