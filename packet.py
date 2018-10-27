import socket, sys, struct, ip

def complement_add(a, b):
	result = (a + b) % 65536
	if (a + b) % 65536 != a + b:
		result += 1
	return result

def icmp():
	#preparing fields
	type_ = 8
	code = 0
	checksum = 0
	id_ = 0
	seq = 0
	data1 = 123
	data2 = 456
	data3 = 789
	data4 = 0xabcd

	# calculating checksum
	checksum = complement_add((type_<<8)+code, id_)
	checksum = complement_add(checksum, seq)
	checksum= complement_add(checksum, data1)
	checksum= complement_add(checksum, data2)
	checksum= complement_add(checksum, data3)
	checksum= complement_add(checksum, data4)

	print(hex(checksum))
	checksum ^= 65535
	print(hex(checksum))
	return struct.pack('!2B7H' , type_, code,checksum, id_, seq, data1, data2,data3,data4) 


s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)


s.sendto(icmp(), ('192.168.1.1' , 0 ))
