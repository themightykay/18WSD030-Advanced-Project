function [combined_signal] = egc(channel_1_power,channel_2_power)
%Equal gain combining function combines two signals by adding their
%magnitudes and then dividing them by the number of signals.
%   The equal gain combining takes two input signals and combines them by
%   adding their magnitudes and then dividing them by the number of
%   signals. The new combined signal is then passed as an output argument.
a = zeros(1,length(channel_1_power)); % preallocating memory for variable a
combined_signal = zeros(1,length(channel_1_power)); % preallocating memory for variable a1

channel_1_mag = db2mag(channel_1_power); % converting from power (dB) to magnitudes
channel_2_mag = db2mag(channel_2_power); % converting from power (dB) to magnitudes

i=1:1:length(channel_1_power); % generating index vector

a(i) = (channel_1_mag(i)+channel_2_mag(i))/sqrt(nargin);
combined_signal(i) = mag2db(a(i)); % convert all data back to power (dB)
end

