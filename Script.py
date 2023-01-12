class script(object):

    START_TXT = """<b>Hᴇʟʟᴏ 👋 {}
 I'ᴍ A Sɪᴍᴘʟᴇ Tᴇʟᴇɢʀᴀᴍ Fɪʟᴇ & Vɪᴅᴇᴏ Rᴇɴᴀᴍᴇ Bᴏᴛ Wɪᴛʜ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ᴀɴᴅ Pᴇʀᴍᴀɴᴇɴᴛ Tʜᴜᴍʙɴᴀɪʟ Sᴜᴘᴘᴏʀᴛ.</b>"""


    DEV_TXT = """<b>➥ <a href=https://github.com/Devil-Botz>『Dᴇᴠɪʟ࿐Tɢ』</a>
➥ <a href=https://github.com/Joelkb>  Jᴏᴇʟ ᠰ TɢX</a></b>"""

    ABOUT_TXT = """<b>➥ ᴍʏ ɴᴀᴍᴇ : {}

➥ ᴏᴡɴᴇʀ : <a href=https://t.me/COLD_ONEZ>Ꮯᴏʟᴅ_Ꮻɴᴇᴢ</a></b>"""

    
    HELP_TXT = """🎆<b><u> HOW TO SET THUMBNAIL </u></b>🎆
  
» /start A bot and send any picture to automatically set thumbnail.
» /delthumb Use this command and delete your old thumbnile.
» /viewthumb Use this command view your current thumbnile.

 <b><u>📝 HOW TO RENAME A FILE 📝</u></b>

» send any file and click Rename option and type new file name and select [ document] or [video]

 <b><u>📝 HOW TO SET CUSTOM CAPTION 📝</u></b>

» /set_caption - set a custom caption
» /see_caption - see your custom caption
» /del_caption - delete custom caption

<b><u>📝 FILLINGS 📝</u></b>
» File Name: {filename}
» Size: {filesize}
» Duration: {duration}"""


    PRGS_BAR = """\n <b>
╭•━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━━━〄
┃
┣➣ 📚 ᴛᴏᴛᴀʟ : {1} | {2}
┃
┣➣ ♾️ ᴘᴇʀᴄᴇɴᴛᴀɢᴇ : {0}%
┃
┣➣ 🚀 sᴘᴇᴇᴅ : {3}/s
┃
┣➣ ⏰ ᴛɪᴍᴇ : {4}
┃
╰•━━━━━━━━━━━━━━━〄 </b> """


    CUST_THUM_DEL = """𝐂𝐮𝐬𝐭𝐨𝐦 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐃𝐞𝐥𝐞𝐭𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 🗑️"""

    CUST_THUM_SAV = """𝐘𝐨𝐮𝐫 𝐂𝐮𝐬𝐭𝐨𝐦 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐒𝐚𝐯𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅"""

    EMPTY_CUST = """𝐘𝐨𝐮 𝐝𝐨𝐧𝐭 𝐡𝐚𝐯𝐞 𝐚𝐧𝐲 𝐜𝐮𝐬𝐭𝐨𝐦 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥"""

    TT_DOWN = """𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳..."""

    TT_UPLD = """𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝚄𝙿𝙻𝙾𝙰𝙳..."""

    PLZ_ETR_NFIL = """𝐏𝐥𝐞𝐚𝐬𝐞 𝐞𝐧𝐭𝐞𝐫 𝐭𝐡𝐞 𝐧𝐞𝐰 𝐟𝐢𝐥𝐞𝐧𝐚𝐦𝐞..."""

    FSUB_MSG = """𝐒𝐎𝐑𝐑𝐘 𝐁𝐑𝐎 𝐘𝐎𝐔 𝐀𝐑𝐄 𝐍𝐎𝐓 𝐉𝐎𝐈𝐍𝐄𝐃 𝐌𝐘 𝐔𝐏𝐃𝐀𝐓𝐄 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 . 𝐏𝐋𝐄𝐀𝐒𝐄  𝐉𝐎𝐈𝐍 𝐀𝐍𝐃 𝐔𝐒𝐄 𝐓𝐇𝐈𝐒 𝐁𝐎𝐓"""

    DEL_CAP = """𝙔𝙤𝙪𝙧 𝙘𝙖𝙥𝙩𝙞𝙤𝙣 𝙨𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮 𝙙𝙚𝙡𝙚𝙩𝙚𝙙"""

    EMPTY_CAP = """𝙔𝙤𝙪 𝙙𝙤𝙣𝙩 𝙝𝙖𝙫𝙚 𝙖𝙣𝙮 𝙘𝙖𝙥𝙩𝙞𝙤𝙣"""

    SAV_CAP = """𝗬𝗼𝘂𝗿 𝗰𝗮𝗽𝘁𝗶𝗼𝗻 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝘀𝗮𝘃𝗲𝗱"""

    GIV_CAP = """𝙂𝙞𝙫𝙚 𝙢𝙚 𝙖 𝙘𝙖𝙥𝙩𝙞𝙤𝙣 𝙩𝙤 𝙨𝙚𝙩. 
𝙀𝙭𝙖𝙢𝙥𝙡𝙚 :- /𝙨𝙚𝙩_𝙘𝙖𝙥𝙩𝙞𝙤𝙣: {filename} 𝙎𝙞𝙯𝙚: {filesize} 𝘿𝙪𝙧𝙖𝙩𝙞𝙤𝙣: {duration}"""
