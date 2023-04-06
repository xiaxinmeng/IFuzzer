TLSEXT_INDEX = [
    ...,
    TLSEXT_IDX_server_name,
    ...,
    TLSEXT_IDX_application_layer_protocol_negotiation,
]

for extid in TLSEXT_INDEX:
    if client.has_extension(extid):
        ext = do_stuff(client, extid)
        ext.callback(client)