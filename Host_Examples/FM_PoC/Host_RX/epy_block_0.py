"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='SC Block',   # will show up in GRC
            in_sig=[np.float32,np.float32],
            out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        #self.sc = sc

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        for i in range(len(input_items[0])):
            if input_items[0][i]>=input_items[1][i]:
                output_items[0][i] = True
            else:
                output_items[0][i] = False
        return len(output_items[0])
