import os
import re

def rename_tiles(directory, num_tiles_x, num_tiles_y):
    files = sorted(os.listdir(directory))
    pattern = re.compile(r'_x(\d+)_y(\d+)')
    temp_suffix = "_temp"

    # Step 1: Collect all rename operations
    rename_operations = {}
    for file in files:
        old_path = os.path.join(directory, file)
        if os.path.isfile(old_path):
            match = pattern.search(file)
            if match:
                try:
                    tile_x = int(match.group(1))
                    tile_y = int(match.group(2))
                    
                    # Calculating new tile_y for top-right origin
                    new_tile_y = num_tiles_y - 1 - tile_y
                    
                    # Creating the new filename
                    new_filename = pattern.sub(f'_x{tile_x}_y{new_tile_y}', file)
                    new_temp_path = os.path.join(directory, new_filename + temp_suffix)
                    
                    # Collect the rename operation
                    rename_operations[old_path] = new_temp_path
                except Exception as e:
                    print(f"Error processing file {file}: {e}")
            else:
                print(f"Filename pattern not matched: {file}")

    # Step 2: Perform temporary renames to avoid conflicts
    for old_path, temp_path in rename_operations.items():
        if os.path.exists(temp_path):
            os.remove(temp_path)  # Remove if the temp file already exists
        print(f"Temporarily renaming {old_path} to {temp_path}")  # Debug statement
        os.rename(old_path, temp_path)

    # Step 3: Collect final rename operations from temp files to target filenames
    final_rename_operations = {}
    for temp_path in rename_operations.values():
        final_path = temp_path.replace(temp_suffix, '')
        # Handle conflict by adding a suffix if final path already exists
        if os.path.exists(final_path):
            counter = 1
            base, ext = os.path.splitext(final_path)
            while os.path.exists(f"{base}_{counter}{ext}"):
                counter += 1
            final_path = f"{base}_{counter}{ext}"
        final_rename_operations[temp_path] = final_path

    # Step 4: Perform final renames to the target filenames
    for temp_path, final_path in final_rename_operations.items():
        print(f"Final renaming {temp_path} to {final_path}")  # Debug statement
        os.rename(temp_path, final_path)

# Update this line with your directory and the number of tiles
rename_tiles(r'D:\LOTROW\repository\LOTROW\TERRAIN\HEIGHT_64x64', num_tiles_x=6, num_tiles_y=7)
