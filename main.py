import os
import glob

def convert_voxelmap_to_xaero(output_folder: str):
    os.makedirs(output_folder, exist_ok=True)
    voxelmap_files = glob.glob('*.points')
    if len(voxelmap_files) > 1:
        print('Внимание: в папке найдено несколько файлов с расширением .points. Продолжение невозможно.')
        return
    elif len(voxelmap_files) == 0:
        print('Внимание: в папке не найдено ни одного файла с расширением .points. Продолжение невозможно.')
        return
    voxelmap_file = voxelmap_files[0]
    dimensions = {'the_nether': 'dim%-1', 'overworld': 'dim%0', 'the_end': 'dim%1'}
    with open(voxelmap_file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith('name:'):
            parts = line.split(',')
            name = parts[0].split(':')[1]
            x = parts[1].split(':')[1]
            z = parts[2].split(':')[1]
            y = parts[3].split(':')[1]
            dimension = parts[-1].split(':')[-1].strip().replace('#', '')
            if dimension in dimensions:
                dimension = dimensions[dimension]
                dimension_folder = os.path.join(output_folder, dimension)
                os.makedirs(dimension_folder, exist_ok=True)
                output_file = os.path.join(dimension_folder, 'mw$default_1.txt')
                with open(output_file, 'a') as f:
                    if f.tell() == 0:
                        f.write('#\n#waypoint:name:initials:x:y:z:color:disabled:type:set:rotate_on_tp:tp_yaw:visibility_type:destination\n#\n')
                    f.write(f'waypoint:{name}::{x}:{y}:{z}:0:false:0:gui.xaero_default:false:0:0:false\n')

convert_voxelmap_to_xaero('output_folder')
