expected_output = {
      'id': {
            '1': {
                  'state': 'active',
                  'type': 'tcp-connect',
                  'destination': '123.23.213.32',
                  'rtt_in_milliseconds': '44',
                  'return_code': 'OK',
                  'last_run': '21 seconds ago',
            },
            '2': {
                  'state': 'active',
                  'type': 'dns',
                  'destination': '11.121.2.123',
                  'rtt_in_milliseconds': '-',
                  'return_code': 'Timeout',
                  'last_run': '7 seconds ago',
            },
            '3': {
                  'state': 'active',
                  'type': 'udp-jitter',
                  'destination': '121.32.11.1',
                  'rtt_in_milliseconds': '1',
                  'return_code': 'OK',
                  'last_run': '54 seconds ago',
            },
            '4': {
                  'state': 'active',
                  'type': 'udp-jitter',
                  'destination': '12.223.33.3',
                  'rtt_in_milliseconds': '1',
                  'return_code': 'OK',
                  'last_run': '15 seconds ago',
            },
            '5': {
                  'state': 'active',
                  'type': 'udp-jitter',
                  'destination': '13.132.32.2',
                  'rtt_in_milliseconds': '1',
                  'return_code': 'OK',
                  'last_run': '8 seconds ago',
            },
            '6': {
                  'state': 'active',
                  'type': 'udp-jitter',
                  'destination': '11.311.31.2',
                  'rtt_in_milliseconds': '1',
                  'return_code': 'OK',
                  'last_run': '40 seconds ago',
            },
            '7': {
                  'state': 'active',
                  'type': 'icmp-echo',
                  'destination': '131.31.11.1',
                  'rtt_in_milliseconds': '1',
                  'return_code': 'OK',
                  'last_run': '2 seconds ago',
            }
      }
}
