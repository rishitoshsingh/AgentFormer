import glob
import os


def get_waymo_pred_split(data_root):
     split_data = []
     for split in ['train', 'val', 'test']:
          files = sorted(glob.glob(f'{data_root}/label/{split}/scene*.txt'))
          if split == 'test':
               files = [f for f in files if os.path.basename(f).split('-')[1].split('.')[0].isdigit()]
          scenes = [os.path.splitext(os.path.basename(x))[0] for x in files]
          split_data.append(scenes)
     return split_data