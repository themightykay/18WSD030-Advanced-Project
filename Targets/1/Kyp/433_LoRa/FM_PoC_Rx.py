#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: FM audio PoC RX
# Author: KD - 6/12/18
# Description: FM audio file Rx at 430MHz
# Generated: Tue Jul 17 11:10:07 2007
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from optparse import OptionParser
import SimpleXMLRPCServer
import math
import threading
import time


class FM_PoC_Rx(gr.top_block):

    def __init__(self, bw=1*250e3+0*500e3, rx_gain=10, freq=923.3e6*0+433e6+919.750e6*0):
        gr.top_block.__init__(self, "FM audio PoC RX")

        ##################################################
        # Parameters
        ##################################################
        self.bw = bw
        self.rx_gain = rx_gain
        self.freq = freq

        ##################################################
        # Variables
        ##################################################
        self.server_port = server_port = 30000
        self.server_address = server_address = "192.168.10.2"
        self.samp_rate = samp_rate = 1e6
        self.offset = offset = -250e3
        self.lpf_decim = lpf_decim = 4

        ##################################################
        # Blocks
        ##################################################
        self.zeromq_push_sink_0_0_0_0 = zeromq.push_sink(gr.sizeof_gr_complex, 1, "tcp://*:9995", 100, False)
        self.zeromq_push_sink_0_0_0 = zeromq.push_sink(gr.sizeof_gr_complex, 1, "tcp://*:9999", 100, False)
        self.xmlrpc_server_0 = SimpleXMLRPCServer.SimpleXMLRPCServer((str(server_address), int(server_port)), allow_none=True)
        self.xmlrpc_server_0.register_instance(self)
        self.xmlrpc_server_0_thread = threading.Thread(target=self.xmlrpc_server_0.serve_forever)
        self.xmlrpc_server_0_thread.daemon = True
        self.xmlrpc_server_0_thread.start()
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(2),
        	),
        )
        self.uhd_usrp_source_0.set_subdev_spec("A:A A:B", 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(freq, 0)
        self.uhd_usrp_source_0.set_gain(rx_gain, 0)
        self.uhd_usrp_source_0.set_antenna("RX2", 0)
        self.uhd_usrp_source_0.set_bandwidth(200e3, 0)
        self.uhd_usrp_source_0.set_center_freq(freq, 1)
        self.uhd_usrp_source_0.set_gain(rx_gain, 1)
        self.uhd_usrp_source_0.set_antenna("RX2", 1)
        self.uhd_usrp_source_0.set_bandwidth(200e3, 1)
        (self.uhd_usrp_source_0).set_max_output_buffer(1000000)
        self.pfb_arb_resampler_xxx_0_0 = pfb.arb_resampler_ccf(
        	  bw/samp_rate,
                  taps=None,
        	  flt_size=32)
        self.pfb_arb_resampler_xxx_0_0.declare_sample_delay(0)
        	
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
        	  bw/samp_rate,
                  taps=None,
        	  flt_size=32)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)
        	
        self.blocks_rotator_cc_0_0 = blocks.rotator_cc((2 * math.pi * offset) / samp_rate)
        self.blocks_rotator_cc_0 = blocks.rotator_cc((2 * math.pi * offset) / samp_rate)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_rotator_cc_0, 0), (self.pfb_arb_resampler_xxx_0, 0))    
        self.connect((self.blocks_rotator_cc_0_0, 0), (self.pfb_arb_resampler_xxx_0_0, 0))    
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.zeromq_push_sink_0_0_0, 0))    
        self.connect((self.pfb_arb_resampler_xxx_0_0, 0), (self.zeromq_push_sink_0_0_0_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_rotator_cc_0, 0))    
        self.connect((self.uhd_usrp_source_0, 1), (self.blocks_rotator_cc_0_0, 0))    

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw
        self.pfb_arb_resampler_xxx_0.set_rate(self.bw/self.samp_rate)
        self.pfb_arb_resampler_xxx_0_0.set_rate(self.bw/self.samp_rate)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self.uhd_usrp_source_0.set_gain(self.rx_gain, 0)
        	
        self.uhd_usrp_source_0.set_gain(self.rx_gain, 1)
        	

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.uhd_usrp_source_0.set_center_freq(self.freq, 0)
        self.uhd_usrp_source_0.set_center_freq(self.freq, 1)

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
        self.blocks_rotator_cc_0.set_phase_inc((2 * math.pi * self.offset) / self.samp_rate)
        self.blocks_rotator_cc_0_0.set_phase_inc((2 * math.pi * self.offset) / self.samp_rate)
        self.pfb_arb_resampler_xxx_0.set_rate(self.bw/self.samp_rate)
        self.pfb_arb_resampler_xxx_0_0.set_rate(self.bw/self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        self.blocks_rotator_cc_0.set_phase_inc((2 * math.pi * self.offset) / self.samp_rate)
        self.blocks_rotator_cc_0_0.set_phase_inc((2 * math.pi * self.offset) / self.samp_rate)

    def get_lpf_decim(self):
        return self.lpf_decim

    def set_lpf_decim(self, lpf_decim):
        self.lpf_decim = lpf_decim


def argument_parser():
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option(
        "", "--bw", dest="bw", type="eng_float", default=eng_notation.num_to_str(1*250e3+0*500e3),
        help="Set bw [default=%default]")
    parser.add_option(
        "", "--rx-gain", dest="rx_gain", type="eng_float", default=eng_notation.num_to_str(10),
        help="Set rx_gain [default=%default]")
    parser.add_option(
        "", "--freq", dest="freq", type="eng_float", default=eng_notation.num_to_str(923.3e6*0+433e6+919.750e6*0),
        help="Set freq [default=%default]")
    return parser


def main(top_block_cls=FM_PoC_Rx, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(bw=options.bw, rx_gain=options.rx_gain, freq=options.freq)
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
