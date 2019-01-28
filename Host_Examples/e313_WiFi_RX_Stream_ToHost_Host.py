#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: E313 Wifi Rx Stream Tohost Host
# Generated: Thu Dec  6 17:25:06 2018
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys
import xmlrpclib
from gnuradio import qtgui


class e313_WiFi_RX_Stream_ToHost_Host(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "E313 Wifi Rx Stream Tohost Host")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("E313 Wifi Rx Stream Tohost Host")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "e313_WiFi_RX_Stream_ToHost_Host")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 48000
        self.rx_gain = rx_gain = 0
        self.freq = freq = 430e6
        self.bw = bw = 1e6

        ##################################################
        # Blocks
        ##################################################
        self._freq_range = Range(70e6, 3000e6, 10e6, 430e6, 200)
        self._freq_win = RangeWidget(self._freq_range, self.set_freq, 'Frequency (Hz)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._freq_win, 0, 0, 1, 2)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(0,1)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(0,2)]
        self._bw_range = Range(100e3, 50e6, 100e3, 1e6, 200)
        self._bw_win = RangeWidget(self._bw_range, self.set_bw, 'BandWidth', "counter_slider", float)
        self.top_grid_layout.addWidget(self._bw_win, 2, 0, 1, 2)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(2,3)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(0,2)]
        self.xmlrpc_client0_0 = xmlrpclib.Server('http://192.168.10.2:30000')
        self.xmlrpc_client0 = xmlrpclib.Server('http://192.168.10.2:30000')
        self.xmlrpc_client = xmlrpclib.Server('http://192.168.10.2:30000')
        self._rx_gain_range = Range(0, 70, 1, 0, 200)
        self._rx_gain_win = RangeWidget(self._rx_gain_range, self.set_rx_gain, 'RF Gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rx_gain_win, 1, 0, 1, 2)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(1,2)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(0,2)]
        self.qtgui_sink_x_0_0_0_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq, #fc
        	bw, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0_0_0_0.set_update_time(1.0/100)
        self._qtgui_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_0_0_0_win, 3, 1, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(3,4)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(1,2)]

        self.qtgui_sink_x_0_0_0_0.enable_rf_freq(True)



        self.qtgui_sink_x_0_0_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq, #fc
        	bw, #bw
        	"Channel 1", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0_0_0.set_update_time(1.0/100)
        self._qtgui_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_0_0_win, 3, 0, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(3,4)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(0,1)]

        self.qtgui_sink_x_0_0_0.enable_rf_freq(True)



        self.channel_2_stream_pull = zeromq.pull_source(gr.sizeof_gr_complex, 1, 'tcp://192.168.10.2:9999', 100, False, -1)
        self.channel_1_stream_pull = zeromq.pull_source(gr.sizeof_gr_complex, 1, 'tcp://192.168.10.2:9995', 100, False, -1)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_sink_x_0_0_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.qtgui_sink_x_0_0_0_0, 0))
        self.connect((self.channel_1_stream_pull, 0), (self.blocks_throttle_0, 0))
        self.connect((self.channel_2_stream_pull, 0), (self.blocks_throttle_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "e313_WiFi_RX_Stream_ToHost_Host")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self.xmlrpc_client0.set_rx_gain(self.rx_gain)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.xmlrpc_client.set_freq(self.freq)
        self.qtgui_sink_x_0_0_0_0.set_frequency_range(self.freq, self.bw)
        self.qtgui_sink_x_0_0_0.set_frequency_range(self.freq, self.bw)

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw
        self.xmlrpc_client0_0.set_bw(self.bw)
        self.qtgui_sink_x_0_0_0_0.set_frequency_range(self.freq, self.bw)
        self.qtgui_sink_x_0_0_0.set_frequency_range(self.freq, self.bw)


def main(top_block_cls=e313_WiFi_RX_Stream_ToHost_Host, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
