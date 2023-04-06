# Parse RTSP Transport headers like
# Transport: RTP/AVP/TCP;interleaved=0-1, RTP/AVP;unicast;client_port=5004
for value in header_list(self.headers, "Transport"):  # Splits at commas
    header = email.message.Message()
    # Default get_params() header is Content-Type
    header["Content-Type"] = value
    [transport, _] = header.get_params()[0]  # Gets the RTP/AVP part
    
    mode = header.get_param("mode", "PLAY")
    channel = header.get_param("interleaved")
    if header.get_param("unicast") is not None:
        port = header.get_param("client_port")
    ...