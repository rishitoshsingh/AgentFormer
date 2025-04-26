

def get_ethucy_stanford_split(dataset):
     seqs = [
          'biwi_eth',
          'biwi_hotel',
          'crowds_zara01',
          'crowds_zara02',
          'crowds_zara03',
          'students001',
          'students003',
          'uni_examples'
     ]

     stanford_seq = [
          "stanford_bookstore",
          "stanford_coupa",
          "stanford_deathCircle",
          "stanford_gates",
          "stanford_hyang",
          "stanford_little",
          "stanford_nexus",
          "stanford_quad",
     ]

     if dataset == 'eth_stanford':
          test = ['biwi_eth']
     elif dataset == 'hotel_stanford':
          test = ['biwi_hotel']
     elif dataset == 'zara1_stanford':
          test = ['crowds_zara01']
     elif dataset == 'zara2_stanford':
          test = ['crowds_zara02']
     elif dataset == 'univ_stanford':
          test = ['students001', 'students003']

     train, val = [], []
     for seq in seqs:
          if seq in test:
               continue
          train.append(f'{seq}_train')
          val.append(f'{seq}_val')
     train += stanford_seq
     return train, val, test