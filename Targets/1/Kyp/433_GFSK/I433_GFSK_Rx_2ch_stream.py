#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: GFSK 2 channel Rx with stream to host
# Author: KD - 15/2/19
# Description: GFSK 2 channel Rx with stream to host
# Generated: Fri Jul 13 12:48:43 2007
##################################################

from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio import vocoder
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import SimpleXMLRPCServer
import threading
import time


class I433_GFSK_Rx_2ch_stream(gr.top_block):

    def __init__(self, freq=434e6, rx_gain=100):
        gr.top_block.__init__(self, "GFSK 2 channel Rx with stream to host")

        ##################################################
        # Parameters
        ##################################################
        self.freq = freq
        self.rx_gain = rx_gain

        ##################################################
        # Variables
        ##################################################
        self.server_port = server_port = 30000
        self.server_address = server_address = "192.168.10.2"
        self.samp_rate = samp_rate = 1e6
        self.lpf_decim = lpf_decim = 4
        self.audio_samp_rate = audio_samp_rate = 44.1e3

        ##################################################
        # Blocks
        ##################################################
        self.zeromq_push_sink_0_0_0_0 = zeromq.push_sink(gr.sizeof_gr_complex, 1, "tcp://*:9995", 100, False)
        self.zeromq_push_sink_0_0_0 = zeromq.push_sink(gr.sizeof_gr_complex, 1, "tcp://*:9999", 100, False)
        self.zeromq_push_sink_0_0 = zeromq.push_sink(gr.sizeof_float, 1, "tcp://*:9993", 100, False)
        self.zeromq_push_sink_0 = zeromq.push_sink(gr.sizeof_float, 1, "tcp://*:9997", 100, False)
        self.xmlrpc_server_0 = SimpleXMLRPCServer.SimpleXMLRPCServer((str(server_address), int(server_port)), allow_none=True)
        self.xmlrpc_server_0.register_instance(self)
        self.xmlrpc_server_0_thread = threading.Thread(target=self.xmlrpc_server_0.serve_forever)
        self.xmlrpc_server_0_thread.daemon = True
        self.xmlrpc_server_0_thread.start()
        self.vocoder_cvsd_decode_bf_1 = vocoder.cvsd_decode_bf(1,0.5)
        self.vocoder_cvsd_decode_bf_0 = vocoder.cvsd_decode_bf(1,0.5)
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
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=44100,
                decimation=250000,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=44100,
                decimation=250000,
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(4, firdes.low_pass(
        	1, samp_rate, 7e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(4, firdes.low_pass(
        	1, samp_rate, 7e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.digital_gfsk_demod_1_0 = digital.gfsk_demod(
        	samples_per_symbol=2,
        	sensitivity=(3.141592653589793/2)/2,
        	gain_mu=0.125,
        	mu=0.5,
        	omega_relative_limit=0.005,
        	freq_error=0.0,
        	verbose=False,
        	log=False,
        )
        self.digital_gfsk_demod_1 = digital.gfsk_demod(
        	samples_per_symbol=2,
        	sensitivity=(3.141592653589793/2)/2,
        	gain_mu=0.125,
        	mu=0.5,
        	omega_relative_limit=0.005,
        	freq_error=0.0,
        	verbose=False,
        	log=False,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.digital_gfsk_demod_1, 0), (self.vocoder_cvsd_decode_bf_1, 0))    
        self.connect((self.digital_gfsk_demod_1_0, 0), (self.vocoder_cvsd_decode_bf_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.digital_gfsk_demod_1, 0))    
        self.connect((self.low_pass_filter_0_0, 0), (self.digital_gfsk_demod_1_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.zeromq_push_sink_0_0, 0))    
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.zeromq_push_sink_0, 0))    
        self.connect((self.uhd_usrp_source_0, 1), (self.low_pass_filter_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.low_pass_filter_0_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.zeromq_push_sink_0_0_0, 0))    
        self.connect((self.uhd_usrp_source_0, 1), (self.zeromq_push_sink_0_0_0_0, 0))    
        self.connect((self.vocoder_cvsd_decode_bf_0, 0), (self.rational_resampler_xxx_0_0, 0))    
        self.connect((self.vocoder_cvsd_decode_bf_1, 0), (self.rational_resampler_xxx_0, 0))    

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.uhd_usrp_source_0.set_center_freq(self.freq, 0)
        self.uhd_usrp_source_0.set_center_freq(self.freq, 1)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self.uhd_usrp_source_0.set_gain(self.rx_gain, 0)
        	
        self.uhd_usrp_source_0.set_gain(self.rx_gain, 1)
        	

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
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 7e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 7e3, 1e3, firdes.WIN_HAMMING, 6.76))

    def get_lpf_decim(self):
        return self.lpf_decim

    def set_lpf_decim(self, lpf_decim):
        self.lpf_decim = lpf_decim

    def get_audio_samp_rate(self):
        return self.audio_samp_rate

    def set_audio_samp_rate(self, audio_samp_rate):
        self.audio_samp_rate = audio_samp_rate


def argument_parser():
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option(
        "", "--freq", dest="freq", type="eng_float", default=eng_notation.num_to_str(434e6),
        help="Set freq [default=%default]")
    parser.add_option(
        "", "--rx-gain", dest="rx_gain", type="eng_float", default=eng_notation.num_to_str(100),
        help="Set rx_gain [default=%default]")
    return parser


def main(top_block_cls=I433_GFSK_Rx_2ch_stream, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(freq=options.freq, rx_gain=options.rx_gain)
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
