''' My caffe helper'''
class CaffeSolver:
    
    """
    Caffesolver is a class for creating a solver.prototxt file. It sets default
    values and can export a solver parameter file.
    Note that all parameters are stored as strings. Strings variables are
    stored as strings in strings.
    """

    def __init__(self, debug=False):

        self.sp = {}
        self.testnet_prototxt_path="testnet.prototxt"
        self.trainnet_prototxt_path="trainnet.prototxt"
        
        # critical:
        self.sp['base_lr'] = '0.001'
        self.sp['momentum'] = '0.9'

        # speed:
        self.sp['test_iter'] = '100'
        self.sp['test_interval'] = '250'

        # looks:
        self.sp['display'] = '25'
        self.sp['snapshot'] = '2500'
        self.sp['snapshot_prefix'] = '"snapshot"'  # string withing a string!

        # learning rate policy
        self.sp['lr_policy'] = '"fixed"'

        # important, but rare:
        self.sp['gamma'] = '0.1'
        self.sp['weight_decay'] = '0.0005'
        self.sp['train_net'] = '"' + self.trainnet_prototxt_path + '"'
        self.sp['test_net'] = '"' + self.testnet_prototxt_path + '"'

        # pretty much never change these.
        self.sp['max_iter'] = '100000'
        self.sp['test_initialization'] = 'false'
        self.sp['average_loss'] = '25'  # this has to do with the display.
        self.sp['iter_size'] = '1'  # this is for accumulating gradients

        if (debug):
            self.sp['max_iter'] = '12'
            self.sp['test_iter'] = '1'
            self.sp['test_interval'] = '4'
            self.sp['display'] = '1'

    def add_from_file(self, filepath):
        """
        Reads a caffe solver prototxt file and updates the Caffesolver
        instance parameters.
        """
        with open(filepath, 'r') as f:
            for line in f:
                if line[0] == '#':
                    continue
                splitLine = line.split(':')
                self.sp[splitLine[0].strip()] = splitLine[1].strip()

    def write(self, filepath):
        """
        Export solver parameters to INPUT "filepath". Sorted alphabetically.
        """
        f = open(filepath, 'w')
        for key, value in sorted(self.sp.items()):
            if not(type(value) is str):
                raise TypeError('All solver parameters must be strings')
            f.write('%s: %s\n' % (key, value))
