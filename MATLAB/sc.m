function [combined_signal] = sc(channel_1_power,channel_2_power)
%Selection combining function combines two signals by selecting the one
%with the best SNR.
%   The selection combining function takes two input signals and combines
%   them by selecting the signal with the best SNR. The new combined
%   signal is then passed as an output argument.
a = zeros(1,length(channel_1_power)); % preallocating memory for variable a

channel_1_mag = db2mag(channel_1_power); % converting from power (dB) to magnitudes
channel_2_mag = db2mag(channel_2_power); % converting from power (dB) to magnitudes

for i=1:1:length(channel_1_power)
    if channel_1_mag(i) > channel_2_mag(i) % if ch1 is larger than ch2
        a(i) = channel_1_mag(i); % select ch1
    elseif channel_1_mag(i) <= channel_2_mag(i)
        a(i) = channel_2_mag(i); % select ch2
    end
end

combined_signal = mag2db(a); % convert all data back to power (dB)
end

