# PicoCTF 2017 - Level 2 - Just Keyp Trying

**Category:** Forensics **Points:** 80

**Description:**

> Here's an interesting capture of some data. But what exactly is this data? Take a look:
> data.pcap

This challenge is fun. We have a pcap file that has a series of USB capture data. We are
given the USB documentation in the hints and looking through there we can map the
values in the pcap data to the keyboard.

We can parse this in Python using the PyShark library. Here is the script I wrote, which
maps the usb key codes to their values. 

```
import pyshark

usb_keyboard_dict = {'04': 'A',
						'05': 'B',
						'06': 'C',
						'07': 'D',
						'08': 'E',
						'09': 'F',
						'0a': 'G',
						'0b': 'H',
						'0c': 'I',
						'0d': 'J',
						'0e': 'K',
						'0f': 'L',
						'10': 'M',
						'11': 'N',
						'12': 'O',
						'13': 'P',
						'14': 'Q',
						'15': 'R',
						'16': 'S',
						'17': 'T',
						'18': 'U',
						'19': 'V',
						'1a': 'W',
						'1b': 'X',
						'1c': 'Y',
						'1d': 'Z',
						'1e': '1',
						'1f': '2',
						'20': '3',
						'21': '4',
						'22': '5',
						'23': '6',
						'24': '7',
						'25': '8',
						'26': '9',
						'27': '0',
						'28': '\n',
						'2c': ' ',
						'2d': '-',
						'2e': '=',
						'2f': '{',
						'30': '}'}

cap = pyshark.FileCapture('data.pcap')
flag = ""
for pkt in cap:
	data = pkt.layers[1].usb_capdata
	data2 = data.split(":")
	if (data2[2] in usb_keyboard_dict):
		print(usb_keyboard_dict[data2[2]], end='')
			
```

FLAG{PR355-0NWARDS-A2FEE6E0}