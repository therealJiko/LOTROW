import cv2
import os

def process_images(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.png'):  # Adjust based on your image format
            img_path = os.path.join(input_dir, filename)
            try:
                img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)  # Read image as-is
                if img is None:
                    continue

                # Process your image here, e.g., resize, save, etc.
                # Example resizing:
                resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)
                
                # Save the resized image
                output_path = os.path.join(output_dir, filename)
                cv2.imwrite(output_path, resized_img)
                print(f"Processed and saved: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Example usage
input_directory = r'D:\LOTROW\repository\LOTROW\TERRAIN\height'
output_directory = r'D:\LOTROW\repository\LOTROW\TERRAIN\height_ue'
new_width, new_height = 4033, 4033  # Desired size (width, height)

process_images(input_directory, output_directory)