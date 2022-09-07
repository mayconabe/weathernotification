import smtplib
from re import I
from urllib import request
import requests
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def listToString(s):
    str1 = " "
    return (str1.join(s))

data_emails = requests.get("http://127.0.0.1:8000/emails/")

soup_emails = BeautifulSoup(data_emails.content, "lxml")
informacoes_emails = soup_emails.find('p').text

data = requests.get("https://g1.globo.com/previsao-do-tempo/df/brasilia.ghtml")
data_emails = requests.get("http://127.0.0.1:8000/emails/")

soup = BeautifulSoup(data.content, "lxml")
informacoes_previsao = soup.find_all('p')[0:3]

titulo = ""
for i in informacoes_previsao:
    titulo += f'{i.text}\n'
titulo_dia = listToString(titulo.split(' ')[0:2])
print(listToString(titulo.split('\n')[2:3]))

detalhes = ""
for i in soup.find_all(class_="forecast-today-detail__item-value"):
    detalhes += str(f'{i.text}\n')

dados_gerais = detalhes.split("\n")

me = "weathernotificationsendemail@gmail.com"
recipients = informacoes_emails.split(',')

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Previsão do tempo"
msg['From'] = me
msg['To'] = ", ".join(recipients)

part1_html = """<!doctype html><html ⚡4email data-css-strict><head><meta charset="utf-8"><style amp4email-boilerplate>body{visibility:hidden}</style><script async src="https://cdn.ampproject.org/v0.js"></script><style amp-custom>.es-desk-hidden { display:none; float:left; overflow:hidden; width:0; max-height:0; line-height:0;}.es-button-border:hover a.es-button, .es-button-border:hover button.es-button { background:#000000; border-color:#000000; color:#03AA6F;}.es-button-border:hover { border-color:#03AA6F #03AA6F #03AA6F #03AA6F; background:#000000;}body { width:100%; font-family:arial, "helvetica neue", helvetica, sans-serif;}table { border-collapse:collapse; border-spacing:0px;}table td, body, .es-wrapper { padding:0; Margin:0;}.es-content, .es-header, .es-footer { table-layout:fixed; width:100%;}p, hr { Margin:0;}h1, h2, h3, h4, h5 { Margin:0; line-height:120%; font-family:Righteous, sans-serif;}.es-left { float:left;}.es-right { float:right;}.es-p5 { padding:5px;}.es-p5t { padding-top:5px;}.es-p5b { padding-bottom:5px;}.es-p5l { padding-left:5px;}.es-p5r { padding-right:5px;}.es-p10 { padding:10px;}.es-p10t { padding-top:10px;}.es-p10b { padding-bottom:10px;}.es-p10l { padding-left:10px;}.es-p10r { padding-right:10px;}.es-p15 { padding:15px;}.es-p15t { padding-top:15px;}.es-p15b { padding-bottom:15px;}.es-p15l { padding-left:15px;}.es-p15r { padding-right:15px;}.es-p20 { padding:20px;}.es-p20t { padding-top:20px;}.es-p20b { padding-bottom:20px;}.es-p20l { padding-left:20px;}.es-p20r { padding-right:20px;}.es-p25 { padding:25px;}.es-p25t { padding-top:25px;}.es-p25b { padding-bottom:25px;}.es-p25l { padding-left:25px;}.es-p25r { padding-right:25px;}.es-p30 { padding:30px;}.es-p30t { padding-top:30px;}.es-p30b { padding-bottom:30px;}.es-p30l { padding-left:30px;}.es-p30r { padding-right:30px;}.es-p35 { padding:35px;}.es-p35t { padding-top:35px;}.es-p35b { padding-bottom:35px;}.es-p35l { padding-left:35px;}.es-p35r { padding-right:35px;}.es-p40 { padding:40px;}.es-p40t { padding-top:40px;}.es-p40b { padding-bottom:40px;}.es-p40l { padding-left:40px;}.es-p40r { padding-right:40px;}.es-menu td { border:0;}s { text-decoration:line-through;}p, ul li, ol li { font-family:arial, "helvetica neue", helvetica, sans-serif; line-height:150%;}ul li, ol li { Margin-bottom:15px; margin-left:0;}a { text-decoration:underline;}.es-menu td a { text-decoration:none; display:block; font-family:arial, "helvetica neue", helvetica, sans-serif;}.es-menu img, .es-button img { vertical-align:middle;}.es-wrapper { width:100%; height:100%; background-color:#000000;}.es-wrapper-color { background-color:#000000;}.es-header { background-color:transparent;}.es-header-body { background-color:#000000;}.es-header-body p, .es-header-body ul li, .es-header-body ol li { color:#EFEFEF; font-size:14px;}.es-header-body a { color:#EFEFEF; font-size:14px;}.es-content-body { background-color:#000000;}.es-content-body p, .es-content-body ul li, .es-content-body ol li { color:#EFEFEF; font-size:14px;}.es-content-body a { color:#EFEFEF; font-size:14px;}.es-footer { background-color:transparent;}.es-footer-body { background-color:#000000;}.es-footer-body p, .es-footer-body ul li, .es-footer-body ol li { color:#EFEFEF; font-size:14px;}.es-footer-body a { color:#EFEFEF; font-size:14px;}.es-infoblock, .es-infoblock p, .es-infoblock ul li, .es-infoblock ol li { line-height:120%; font-size:12px; color:#CCCCCC;}.es-infoblock a { font-size:12px; color:#CCCCCC;}h1 { font-size:40px; font-style:normal; font-weight:normal; color:#FFFFFF;}h2 { font-size:24px; font-style:normal; font-weight:normal; color:#FFFFFF;}h3 { font-size:20px; font-style:normal; font-weight:normal; color:#FFFFFF;}.es-header-body h1 a, .es-content-body h1 a, .es-footer-body h1 a { font-size:40px;}.es-header-body h2 a, .es-content-body h2 a, .es-footer-body h2 a { font-size:24px;}.es-header-body h3 a, .es-content-body h3 a, .es-footer-body h3 a { font-size:20px;}a.es-button, button.es-button { border-style:solid; border-color:#000000; border-width:10px 20px 10px 20px; display:inline-block; background:#000000; border-radius:30px; font-size:18px; font-family:arial, "helvetica neue", helvetica, sans-serif; font-weight:bold; font-style:normal; line-height:120%; color:#FFFFFF; text-decoration:none; width:auto; text-align:center;}.es-button-border { border-style:solid solid solid solid; border-color:#FFFFFF #FFFFFF #FFFFFF #FFFFFF; background:#000000; border-width:3px 3px 3px 3px; display:inline-block; border-radius:30px; width:auto;}.es-button img { display:inline-block; vertical-align:middle;}@media only screen and (max-width:600px) {p, ul li, ol li, a { line-height:150% } h1, h2, h3, h1 a, h2 a, h3 a { line-height:120% } h1 { font-size:40px; text-align:center } h2 { font-size:26px; text-align:left } h3 { font-size:20px; text-align:center } .es-header-body h1 a, .es-content-body h1 a, .es-footer-body h1 a { font-size:40px } .es-header-body h2 a, .es-content-body h2 a, .es-footer-body h2 a { font-size:26px; text-align:left } .es-header-body h3 a, .es-content-body h3 a, .es-footer-body h3 a { font-size:20px } .es-menu td a { font-size:12px } .es-header-body p, .es-header-body ul li, .es-header-body ol li, .es-header-body a { font-size:14px } .es-content-body p, .es-content-body ul li, .es-content-body ol li, .es-content-body a { font-size:14px } .es-footer-body p, .es-footer-body ul li, .es-footer-body ol li, .es-footer-body a { font-size:12px } .es-infoblock p, .es-infoblock ul li, .es-infoblock ol li, .es-infoblock a { font-size:12px } *[class="gmail-fix"] { display:none } .es-m-txt-c, .es-m-txt-c h1, .es-m-txt-c h2, .es-m-txt-c h3 { text-align:center } .es-m-txt-r, .es-m-txt-r h1, .es-m-txt-r h2, .es-m-txt-r h3 { text-align:right } .es-m-txt-l, .es-m-txt-l h1, .es-m-txt-l h2, .es-m-txt-l h3 { text-align:left } .es-m-txt-r img { float:right } .es-m-txt-c img { margin:0 auto } .es-m-txt-l img { float:left } .es-button-border { display:inline-block } a.es-button, button.es-button { font-size:16px; display:inline-block } .es-adaptive table, .es-left, .es-right { width:100% } .es-content table, .es-header table, .es-footer table, .es-content, .es-footer, .es-header { width:100%; max-width:600px } .es-adapt-td { display:block; width:100% } .adapt-img { width:100%; height:auto } td.es-m-p0 { padding:0 } td.es-m-p0r { padding-right:0 } td.es-m-p0l { padding-left:0 } td.es-m-p0t { padding-top:0 } td.es-m-p0b { padding-bottom:0 } td.es-m-p20b { padding-bottom:20px } .es-mobile-hidden, .es-hidden { display:none } tr.es-desk-hidden, td.es-desk-hidden, table.es-desk-hidden { width:auto; overflow:visible; float:none; max-height:inherit; line-height:inherit } tr.es-desk-hidden { display:table-row } table.es-desk-hidden { display:table } td.es-desk-menu-hidden { display:table-cell } .es-menu td { width:1% } table.es-table-not-adapt, .esd-block-html table { width:auto } table.es-social { display:inline-block } table.es-social td { display:inline-block } td.es-m-p5 { padding:5px } td.es-m-p5t { padding-top:5px } td.es-m-p5b { padding-bottom:5px } td.es-m-p5r { padding-right:5px } td.es-m-p5l { padding-left:5px } td.es-m-p10 { padding:10px } td.es-m-p10t { padding-top:10px } td.es-m-p10b { padding-bottom:10px } td.es-m-p10r { padding-right:10px } td.es-m-p10l { padding-left:10px } td.es-m-p15 { padding:15px } td.es-m-p15t { padding-top:15px } td.es-m-p15b { padding-bottom:15px } td.es-m-p15r { padding-right:15px } td.es-m-p15l { padding-left:15px } td.es-m-p20 { padding:20px } td.es-m-p20t { padding-top:20px } td.es-m-p20r { padding-right:20px } td.es-m-p20l { padding-left:20px } td.es-m-p25 { padding:25px } td.es-m-p25t { padding-top:25px } td.es-m-p25b { padding-bottom:25px } td.es-m-p25r { padding-right:25px } td.es-m-p25l { padding-left:25px } td.es-m-p30 { padding:30px } td.es-m-p30t { padding-top:30px } td.es-m-p30b { padding-bottom:30px } td.es-m-p30r { padding-right:30px } td.es-m-p30l { padding-left:30px } td.es-m-p35 { padding:35px } td.es-m-p35t { padding-top:35px } td.es-m-p35b { padding-bottom:35px } td.es-m-p35r { padding-right:35px } td.es-m-p35l { padding-left:35px } td.es-m-p40 { padding:40px } td.es-m-p40t { padding-top:40px } td.es-m-p40b { padding-bottom:40px } td.es-m-p40r { padding-right:40px } td.es-m-p40l { padding-left:40px } .es-desk-hidden { display:table-row; width:auto; overflow:visible; max-height:inherit } }</style></head>"""
part2_html = """<body><div class="es-wrapper-color"> <!--[if gte mso 9]><v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t"> <v:fill type="tile" color="#000000"></v:fill> </v:background><![endif]--><table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0"><tr><td valign="top"><table cellpadding="0" cellspacing="0" class="es-header" align="center"><tr><td align="center"><table bgcolor="#ffffff" class="es-header-body" align="center" cellpadding="0" cellspacing="0" width="600"><tr><td class="es-p20t es-p20r es-p20l" align="left"><table cellpadding="0" cellspacing="0" width="100%"><tr><td width="560" class="es-m-p0r" valign="top" align="center"><table cellpadding="0" cellspacing="0" width="100%" bgcolor="#333333" style="background-color: #333333" role="presentation"><tr><td align="center" bgcolor="#050405"><p style="line-height: 54px;font-size: 36px;color: #ffffff">Weather Notification</p></td></tr></table></td></tr></table></td>
</tr></table></td></tr></table>"""
part3_html = """<table class="es-content" cellspacing="0" cellpadding="0" align="center"><tr><td align="center"><table class="es-content-body" style="background-color: #000000" width="600" cellspacing="0" cellpadding="0" bgcolor="#000000" align="center"><tr><td class="es-p20t es-p20r es-p20l" align="left"><table cellpadding="0" cellspacing="0" width="100%"><tr><td width="560" align="center" valign="top"><table cellpadding="0" cellspacing="0" width="100%" role="presentation"><tr><td align="center" style="font-size: 0px"><img class="adapt-img" src="https://vmcrno.stripocdn.email/content/guids/CABINET_2c08af9e46abd212569925b240debe0c/images/44391625818311503.png" alt style="display: block" width="560" height="4" layout="responsive"></img></td></tr></table></td></tr></table></td>
</tr><tr><td class="es-p20" align="left"> <!--[if mso]><table width="560" cellpadding="0" cellspacing="0"><tr><td width="85" valign="top"><![endif]--><table cellpadding="0" cellspacing="0" class="es-left" align="left"><tr><td width="85" class="es-m-p20b" align="left"><table cellpadding="0" cellspacing="0" width="100%" role="presentation"><tr><td align="center" style="font-size: 0px"><img class="adapt-img" src="https://vmcrno.stripocdn.email/content/guids/80f93564-1936-49fa-a510-c847f968ae5b/images/cloudyday.png" alt style="display: block" width="85" height="85" layout="responsive"></img></td></tr></table></td></tr></table> <!--[if mso]></td><td width="20"></td>
<td width="455" valign="top"><![endif]--><table cellpadding="0" cellspacing="0" class="es-right" align="right"><tr><td width="455" align="left"><table cellpadding="0" cellspacing="0" width="100%" role="presentation"><tr><td align="left" class="es-p10t"><h1 style="line-height: 19px;font-family: arial, 'helvetica neue', helvetica, sans-serif;font-size: 16px;color: #ffffff">{0}</h1><p style="font-family: arial, 'helvetica neue', helvetica, sans-serif;font-size: 40px;line-height: 48px;color: #ffffff">{1}</p><br>""".format(listToString(titulo.split('\n')[1:2]), listToString(titulo.split('\n')[0:1]))
part4_html = """<span style="font-size: 16px;line-height: 0px"><p style="font-size: 16px;line-height: 24px">{0}</span></p></td></tr></table></td></tr></table>""".format(listToString(titulo.split('\n')[2:3]))
part5_html = """ </td></tr></table></td></tr></table> <!--[if mso]></td></tr></table><![endif]--></td>
</tr><tr><td class="es-p20b es-p20r es-p20l" align="left"><table width="100%" cellspacing="0" cellpadding="0"><tr><td class="es-m-p0r es-m-p20b" width="560" valign="top" align="center"><table width="100%" cellspacing="0" cellpadding="0" role="presentation"><tr><td align="center" class="es-p20b" style="font-size: 0px"><img class="adapt-img" src="https://vmcrno.stripocdn.email/content/guids/CABINET_2c08af9e46abd212569925b240debe0c/images/44391625818311503.png" alt style="display: block" width="560" height="4" layout="responsive"></img></td></tr></table></td></tr><tr><td class="es-m-p0r es-m-p20b" width="560" valign="top" align="center"><table width="100%" cellspacing="0" cellpadding="0" role="presentation"><tr><td align="center" class="es-p10b"><br><p style="line-height: 24px;font-size: 32px;color: #ffffff"><strong>{0}&nbsp; &nbsp; {1}</strong></p><br><br><p style="line-height: 24px;font-size: 16px;color: #ffffff">Prob. de Chuva: {2}<br><br></p>
<p style="line-height: 24px;font-size: 16px;color: #ffffff">Nascer do Sol: {3}</p><br><p style="line-height: 24px;font-size: 16px;color: #ffffff">Por do sol: {4}</p><br><p style="line-height: 24px;font-size: 16px;color: #ffffff">Vento: {5}<br><br>Raios UV: {6}</p><br><p style="line-height: 24px;font-size: 16px;color: #ffffff">Umidade: {7} {8}</p></td></tr><tr><td align="left" class="es-p40t es-p10b"><h2><br></h2></td></tr></table></td></tr><tr><td class="es-m-p0r es-m-p20b" width="560" valign="top" align="center"><table width="100%" cellspacing="0" cellpadding="0" role="presentation"><tr><td align="center" class="es-p10t es-p10b" style="font-size: 0px"><img class="adapt-img" src="https://vmcrno.stripocdn.email/content/guids/CABINET_2c08af9e46abd212569925b240debe0c/images/44391625818311503.png" alt style="display: block" width="560" height="4" layout="responsive"></img></td></tr></table></td></tr></table></td></tr></table></td></tr></table></td></tr></table></div></body></html>""".format(soup.find(class_="forecast-today__temperature--max").text, soup.find(class_="forecast-today__temperature--min").text, dados_gerais[0], dados_gerais[1], dados_gerais[2], dados_gerais[3], dados_gerais[4], dados_gerais[5], dados_gerais[6])
# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
{0}{1}{2}{3}{4}
""".format(part1_html, part2_html, part3_html, part4_html, part5_html)

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)
# Send the message via local SMTP server.
mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login('weathernotificationsendemail@gmail.com', 'dlkpchtqkeebnmzu')
mail.sendmail(me, recipients, msg.as_string())
mail.quit()