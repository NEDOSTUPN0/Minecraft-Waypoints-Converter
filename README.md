# Voxel-To-Xaeros-Converter

This Python script allows you to convert waypoints from the VoxelMap format to the Xaero's Minimap format.

## Usage

1. Download the script from this repository and save it to your computer.
2. Open a terminal or command prompt and navigate to the folder where the script is located.
3. Place the VoxelMap waypoints file in the script folder `.minecraft/voxelmap/WORLDORSERVER.points`
4. Run the script using the command ``` python main.py ```.

After that, the script will create a folder called `output_folder`, which will contain 3 more folders (`dim%0`, `dim%-1`, `dim%1`). Copy all these folders and place them in `.minecraft/XaeroWaypoints/WORLDORSERVER/`
