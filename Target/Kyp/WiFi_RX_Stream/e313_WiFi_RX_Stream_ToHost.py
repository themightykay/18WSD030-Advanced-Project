#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: E313 Wifi Rx Stream Tohost
# Generated: Sat Jul  7 17:46:55 2007
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import gr, blocks
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import SimpleXMLRPCServer
import threading
import time


class e313_WiFi_RX_Stream_ToHost(gr.top_block):

    def __init__(self, bw=1e6, freq=430e6, rx_gain=0):
        gr.top_block.__init__(self, "E313 Wifi Rx Stream Tohost")

        ##################################################
        # Parameters
        ##################################################
        self.bw = bw
        self.freq = freq
        self.rx_gain = rx_gain

        ##################################################
        # Variables
        ##################################################
        self.server_port = server_port = 30000
        self.server_address = server_address = "192.168.10.2"
        self.samp_rate = samp_rate = 1e6

        ##################################################
        # Blocks
        ##################################################
        self.xmlrpc_server_0 = SimpleXMLRPCServer.SimpleXMLRPCServer((str(server_address), int(server_port)), allow_none=True)
        self.xmlrpc_server_0.register_instance(self)
        self.xmlrpc_server_0_thread = threading.Thread(target=self.xmlrpc_server_0.serve_forever)
        self.xmlrpc_server_0_thread.daemon = True
        self.xmlrpc_server_0_thread.start()
        self.uhd_usrp_source_0_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0_0.set_center_freq(freq, 0)
        self.uhd_usrp_source_0_0.set_gain(rx_gain, 0)
        self.uhd_usrp_source_0_0.set_antenna("RX2", 0)
        self.uhd_usrp_source_0_0.set_bandwidth(bw, 0)
        (self.uhd_usrp_source_0_0).set_max_output_buffer(10000000)
        self.blocks_file_meta_sink_0 = blocks.file_meta_sink(gr.sizeof_gr_complex*1, "/home/root/grc_programs/Kyp/data/data_test_ch1.dat", samp_rate, 1, blocks.GR_FILE_FLOAT, True, 1000000, "", True)
        self.blocks_file_meta_sink_0.set_unbuffered(False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.uhd_usrp_source_0_0, 0), (self.blocks_file_meta_sink_0, 0))    

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw
        self.uhd_usrp_source_0_0.set_bandwidth(self.bw, 0)
        self.uhd_usrp_source_0_0.set_bandwidth(self.bw, 1)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.uhd_usrp_source_0_0.set_center_freq(self.freq, 0)
        self.uhd_usrp_source_0_0.set_center_freq(self.freq, 1)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self.uhd_usrp_source_0_0.set_gain(self.rx_gain, 0)
        	
        self.uhd_usrp_source_0_0.set_gain(self.rx_gain, 1)
        	

    def get_server_port(self):
        return self.server_port

    def set_server_port(self, server_port):
        self.server_port = server_port

    def get_server_address(self):
        return self.server_address

    def set_server_address(self, server_address):
        self.server_address = server_address

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0_0.set_samp_rate(self.samp_rate)


def argument_parser():
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option(
        "", "--bw", dest="bw", type="eng_float", default=eng_notation.num_to_str(1e6),
        help="Set bw [default=%default]")
    parser.add_option(
        "", "--freq", dest="freq", type="eng_float", default=eng_notation.num_to_str(430e6),
        help="Set freq [default=%default]")
    parser.add_option(
        "", "--rx-gain", dest="rx_gain", type="eng_float", default=eng_notation.num_to_str(0),
        help="Set rx_gain [default=%default]")
    return parser


def main(top_block_cls=e313_WiFi_RX_Stream_ToHost, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(bw=options.bw, freq=options.freq, rx_gain=options.rx_gain)
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
