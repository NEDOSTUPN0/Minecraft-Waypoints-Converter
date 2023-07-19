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

def convert_xaero_to_voxelmap(output_folder: str):
    os.makedirs(output_folder, exist_ok=True)
    xaero_files = glob.glob('**/mw$default_1.txt', recursive=True)
    if len(xaero_files) == 0:
        print('Внимание: в папке не найдено ни одного файла с именем mw$default_1.txt. Продолжение невозможно.')
        return
    dimensions = {'dim%-1': 'the_nether', 'dim%0': 'overworld', 'dim%1': 'the_end'}
    output_file = os.path.join(output_folder, 'converted.points')
    with open(output_file, 'w') as f:
        f.write('subworlds:\noldNorthWorlds:\nseeds:\n')
        for xaero_file in xaero_files:
            dimension_folder = os.path.dirname(xaero_file)
            dimension = os.path.basename(dimension_folder)
            if dimension in dimensions:
                dimension = dimensions[dimension]
                with open(xaero_file, 'r') as f2:
                    lines = f2.readlines()
                for line in lines:
                    if line.startswith('waypoint:'):
                        parts = line.split(':')
                        name = parts[1]
                        x = parts[3]
                        y = parts[4]
                        z = parts[5]
                        f.write(f'name:{name},x:{x},z:{z},y:{y},enabled:true,red:0.058490813,green:0.89992464,blue:0.60238135,suffix:,world:,dimensions:{dimension}#\n')

direction = input('Введите 1 для конвертации из VoxelMap в Xaero\'s Minimap или 2 для конвертации из Xaero\'s Minimap в VoxelMap (по умолчанию 1): ')
if direction == '2':
    convert_xaero_to_voxelmap('output_folder')
else:
    convert_voxelmap_to_xaero('output_folder')
