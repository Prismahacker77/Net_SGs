import boto3

def scan_security_groups():
    ec2_client = boto3.client('ec2')
    security_groups = ec2_client.describe_security_groups()['SecurityGroups']

    for sg in security_groups:
        sg_name = sg['GroupName']
        sg_id = sg['GroupId']
        for permission in sg['IpPermissions']:
            for ip_range in permission.get('IpRanges', []):
                if ip_range.get('CidrIp') == '0.0.0.0/0':
                    protocol = permission.get('IpProtocol', 'N/A')
                    from_port = permission.get('FromPort', 'N/A')
                    to_port = permission.get('ToPort', 'N/A')
                    print(f"Security Group: {sg_name} ({sg_id})")
                    print(f"  Protocol: {protocol}")
                    print(f"  Port Range: {from_port} - {to_port}")
                    print(f"  Source: 0.0.0.0/0")
                    print("-" * 60)

if __name__ == "__main__":
    scan_security_groups()