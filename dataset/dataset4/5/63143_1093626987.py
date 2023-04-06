
import argparse
import pprint

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)

group.add_argument('--device-get-capabilities',
                   action='store_true',
                   help='Execute GetCapabilities action from ONVIF devicemgmt.wsdl')

group.add_argument('--ptz-absolute-move',
                   nargs=3,
                   metavar=('x', 'y', 'z'),
                   help='Execute AbsoluteMove action from ONVIF ptz.wsdl')

group.add_argument('--ptz-get-status',
                   metavar='MEDIA_PROFILE',
                   default='MediaProfile000',
                   help='Execute GetSatus action from ONVIF ptz.wsdl for a media profile (default=%(default)s)')

pprint.pprint(parser.parse_args(['--ptz-get-status']))
