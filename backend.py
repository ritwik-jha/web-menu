#!/usr/bin/python3

import subprocess as sp
import cgi

print('content-type: text/html')
print()

data = cgi.FieldStorage()
a = data.getvalue('a')
x = data.getvalue('x')



if a=='linux-1':
	output = sp.getoutput('mkdir {}'.format(x))
elif a == 'linux-2':
	output = sp.getoutput('ls')
	print(output)
elif a == 'linux-3':
	output = sp.getoutput('touch {}'.format(x))
elif a == 'linux-4':
	output = sp.getoutput('cat {}'.format(x))
elif a == 'linux-5':
	output = sp.getoutput('useradd {}'.format(x))
	print(output)
elif a == 'linux-6':
	output = sp.getoutput('passwd {}'.format(x))
	print(output)
elif a == 'linux-7':
	output = sp.getoutput('free -m')
	print(output)
elif a == 'linux-8':
	output = sp.getoutput('df -hT')
	print(output)
elif a == 'linux-9':
	output = sp.getoutput('rpm -q {}'.format(x))
	print(output)
elif a == 'linux-10':
	output = sp.getoutput('rpm -e {}'.format(x))
	print(output)
elif a == 'linux-11':
	output = sp.getoutput('ifconfig enp0s3')
	print(output)
elif a == 'linux-12':
	output = sp.getoutput('jps')
	print(output)
elif a == 'linux-13':
	output = sp.getoutput('lscpu')
	print(output)
elif a == 'linux-14':
	output = sp.getoutput('ps -aux')
	print(output)
elif a == 'linux-15':
	output = sp.getoutput('uptime')
	print(output)
elif a == 'linux-16':
	output = sp.getoutput('echo 3 > /proc/sys/vm/drop_caches')
	print(output)
elif a == 'linux-17':
	output = sp.getoutput('yum whatprovides {}'.format(x))
	print(output)
elif a == 'linux-18':
	output = sp.getoutput('ping {}'.format(x))
	print(output)
elif a == 'linux-19':
	y = data.getoutput('y')
	output = sp.getoutput('useradd -s {} {}'.format(x,y))
	print(output)
elif a == 'aws-1':
	output = sp.getoutput('aws configure')
	print(output)
elif a == 'aws-2':
	output = sp.getoutput('aws ec2 create-key-pair --key-name {}'.format(x))
	print(output)
elif a == 'aws-3':
	output = sp.getoutput('aws ec2 create-security-group --group-name {}'.format(x))
	print(output)
elif a == 'aws-4':
	y = data.getoutput('y')
	z = data.getoutput('z')
	b = data.getoutput('b')
	c = data.getoutput('c')
	d = data.getoutput('d')
	output = sp.getoutput('aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --key-name {} --security-group-ids {}'.format(x,y,z,b,c,d))
	print(output)
elif a == 'aws-5':
	y = data.getoutput('y')
	output = sp.getoutput('aws ec2 create-volume --availability-zone {} --no-encrypted --size {}'.format(x,y))
	print(output)
elif a == 'aws-6':
	y = data.getoutput('y')
	output = sp.getoutput('aws ec2 attach-volume --instance-id {} --volume-id {} --device xvdh'.format(x,y))
	print(output)
elif a == 'aws-7':
	y = data.getoutput('y')
	output = sp.getoutput('aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}'.format(x,y,y))
	print(output)


