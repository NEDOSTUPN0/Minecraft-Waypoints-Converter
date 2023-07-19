# Minecraft Waypoints Converter

This Python script allows you to convert waypoints from the VoxelMap format to the Xaero's Minimap format.

## Usage

1. Download the script from this repository and save it to your computer.
2. Open a terminal or command prompt and navigate to the folder where the script is located.
3. Place the VoxelMap waypoints file, or Xaero's waypoints folders (dim%0, dim%1, dim%-1) in the script folder `.minecraft/voxelmap/WORLDORSERVER.points` or `.minecraft/XaeroWaypoints/`
4. Run the script using the command ``` python main.py ```.

After running, the script will ask where to convert labels from.

If the conversion is from VoxelMap, the script will create 3 more folders in the `output_folder` folder (`dim%0`, `dim%-1`, `dim%1`). Copy all these folders and place them in `.minecraft/XaeroWaypoints/WORLDORSERVER/`.

If you are converting from Xaero's Minimap, the script will create a converted.points file in the output_folder, rename it to the name of your world or server IP, e.g. "mc.exampleip.com.points", then copy it to `.minecraft/voxelmap`.
