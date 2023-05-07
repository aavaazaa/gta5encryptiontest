import uuid
import base64
import time
import datetime

import uvicorn
import xml.etree.ElementTree as ET
from wsgiref.handlers import format_date_time
from clienttorosencprovider import ClientToRosEncProvider
from rostoclientencprovider import RosToClientEncProvider
from io import BytesIO


async def app(scope, receive, send):
    assert scope['type'] == 'http'

    body = ClientToRosEncProvider().decrypt(await read_body(receive))
    print('Received body: ' + str(body))

    now = datetime.datetime.now()
    stamp = time.mktime(now.timetuple())

    xml = craft_xml()
    print('Sending reply: ' + xml.decode('utf-8'))
    xml_response = RosToClientEncProvider().encrypt(xml)

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'Cache-Control', b'private, max-age=0'],
            [b'Content-Type', b'text/xml; charset=utf-8'],
            [b'Server', b'Microsoft-IIS/10.0'],
            [b'SCS-RequestId', str(uuid.uuid4())],
            [b'Date', format_date_time(stamp).encode()],
            [b'Content-Length', str(len(xml_response)).encode()]
        ],
    })

    await send({
        'type': 'http.response.body',
        'body': xml_response,
    })


async def read_body(receive):
    body = b''
    more_body = True

    while more_body:
        message = await receive()
        body += message.get('body', b'')
        more_body = message.get('more_body', False)

    return body


def craft_xml():
    response = ET.Element('Response')
    #response.set('xmlns:xsd', 'http://www.w3.org/2001/XMLSchema')
    #response.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
    response.set('ms', '30')
    response.set('xmlns', 'CreateTicketResponse')

    status = ET.SubElement(response, 'Status')
    status.text = '1'

    status = ET.SubElement(response, 'Ticket')
    status.text = 'YWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFh'

    d = datetime.datetime.now()
    status = ET.SubElement(response, 'PosixTime')
    status.text = str(int(time.mktime(d.timetuple())))

    secs_until_expiration = ET.SubElement(response, 'SecsUntilExpiration')
    secs_until_expiration.text = '86399'

    region = ET.SubElement(response, 'Region')
    region.text = 'US'

    player_account_id = ET.SubElement(response, 'PlayerAccountId')
    player_account_id.text = '262922018'

    services = ET.SubElement(response, 'Services')

    count = ET.SubElement(response, 'Count')
    count.text = '0'

    public_ip = ET.SubElement(response, 'PublicIp')
    public_ip.text = '127.0.0.1'

    session_id = ET.SubElement(response, 'SessionId')
    session_id.text = '5'

    session_key = ET.SubElement(response, 'SessionKey')
    session_key.text = 'MDEyMzQ1Njc4OWFiY2RlZg=='

    session_ticket = ET.SubElement(response, 'SessionTicket')
    session_ticket.text = 'vhASmPR0NnA7MZsdVCTCV/3XFABWGa9duCEscmAM0kcCDVEa7YR/rQ4kfHs2HIPIttq08TcxIzuwyPWbaEllvQ=='

    cloud_key = ET.SubElement(response, 'CloudKey')
    cloud_key.text = '8G8S9JuEPa3kp74FNQWxnJ5BXJXZN1NFCiaRRNWaAUR='

    rockstar_account = ET.SubElement(response, 'RockstarAccount')

    rockstar_id = ET.SubElement(rockstar_account, 'RockstarId')
    rockstar_id.text = '262922018'

    avatar_url = ET.SubElement(rockstar_account, 'AvatarUrl')
    avatar_url.text = 'Bully/b20.png'

    country_code = ET.SubElement(rockstar_account, 'CountryCode')
    country_code.text = 'US'

    email = ET.SubElement(rockstar_account, 'Email')
    email.text = 'example@example.com'

    language_code = ET.SubElement(rockstar_account, 'LanguageCode')
    language_code.text = 'en'

    nickname = ET.SubElement(rockstar_account, 'Nickname')
    nickname.text = 'TEST'

    zip_code = ET.SubElement(rockstar_account, 'ZipCode')
    zip_code.text = '90001'

    privileges = ET.SubElement(response, 'Privileges')
    privileges.text = '1,2,3,4,5,6,8,9,10,11,14,15,16,17,18,19,21,22'

    privs = ET.SubElement(response, 'Privs')

    p = ET.SubElement(privs, 'p')
    p.set('id', '22')
    p.set('g', 'True')

    tree = ET.ElementTree(response)

    f = open('test.xml', 'wb')
    tree.write(f, encoding='utf-8', xml_declaration=True)
    f.close()

    f = BytesIO()
    tree.write(f, encoding='utf-8', xml_declaration=True)
    return f.getvalue().replace(b"\'", b"\"")


if __name__ == "__main__":
    uvicorn.run("testserver:app", host='0.0.0.0', port=80, log_level="info", server_header=False, date_header=False)