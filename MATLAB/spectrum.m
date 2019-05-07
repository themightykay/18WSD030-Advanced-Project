function [frequency,power] = spectrum(complex_signal,f_carrier,bandwidth,disp,figure_title)
%Spectrum function creates the spectrum of a complex signal
%   The spectrum function take as input a complex signal a frequency and a 
%   bandwith. With these inputs it creates a new frequency base (x-axis)
%   and a spectrum of the input signal (y-axis)
y = fft(complex_signal); % fft of the complex signal
x = fftshift(y); % shift zero-frequency component to center of spectrum
frequency=linspace(f_carrier-(bandwidth/2),f_carrier+(bandwidth/2),length(x));

power = 20*log10(abs(x));


if disp
    % Display code
    figure
    plot(frequency/10^6,power-110) % plots f and power of singal with normilisation of 110 dB
    grid on
    grid minor
    xlabel('Frequency (MHz)')
    ylabel('Power')
    title(figure_title)
    ylim([-140 -40]) % limits y-axis from -140 dB to -40 dB
end

end

