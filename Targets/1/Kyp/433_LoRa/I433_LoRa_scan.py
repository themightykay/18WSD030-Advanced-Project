#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Sniffing 433 LoRa packets
# Author: KD - 11/2/19
# Description: Sniffing 433 LoRa packets and sending IQ to host
# Generated: Thu Jul 12 12:03:33 2007
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import SimpleXMLRPCServer
import math
import threading
import time


class I433_LoRa_scan(gr.top_block):

    def __init__(self, bw=1*250e3+0*500e3, rx_gain=100, freq=434e6*1+868e6*0):
        gr.top_block.__init__(self, "Sniffing 433 LoRa packets")

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
        self.uhd_usrp_source_0.set_center_freq(freq, 1)
        self.uhd_usrp_source_0.set_gain(rx_gain, 1)
        self.uhd_usrp_source_0.set_antenna("RX2", 1)
        (self.uhd_usrp_source_0).set_max_output_buffer(1000000)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.uhd_usrp_source_0, 0), (self.zeromq_push_sink_0_0_0, 0))    
        self.connect((self.uhd_usrp_source_0, 1), (self.zeromq_push_sink_0_0_0_0, 0))    

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw

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
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset

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
        "", "--rx-gain", dest="rx_gain", type="eng_float", default=eng_notation.num_to_str(100),
        help="Set rx_gain [default=%default]")
    parser.add_option(
        "", "--freq", dest="freq", type="eng_float", default=eng_notation.num_to_str(434e6*1+868e6*0),
        help="Set freq [default=%default]")
    return parser


def main(top_block_cls=I433_LoRa_scan, options=None):
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
