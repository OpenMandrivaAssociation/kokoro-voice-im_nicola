Name:		kokoro-voice-im_nicola
Version:	1.0
Release:	1
Summary:	Italian male Kokoro voice im_nicola
URL:		https://huggingface.co/hexgrad/Kokoro-82M/tree/main/voices
License:	Apache-2.0
BuildArch:	noarch
Group:		System/Multimedia
Provides:	kokoro-voice
Provides:	kokoro-voice-it
Requires:	kokoro-model >= 1.0

%sourcelist
https://huggingface.co/hexgrad/Kokoro-82M/resolve/main/voices/im_nicola.pt

%description
%{summary}.
Uses the shared checkpoint in kokoro-model.
Pronunciation uses espeak-ng.
Select it with: kokoro -m im_nicola

%install
mkdir -p %{buildroot}%{_datadir}/kokoro/voices
install -c -m 644 %{S:0} %{buildroot}%{_datadir}/kokoro/voices/im_nicola.pt

%files
%{_datadir}/kokoro/voices/im_nicola.pt
