class script(object):
    START_TXT = """Hᴇʟʟᴏ👋 {}, Mʏ Nᴀᴍᴇ Is <a href='https://t.me/MovieTime02_Bot'>Mᴏᴠɪᴇ Tɪᴍᴇ Bᴏᴛ</a> I Cᴀɴ Pʀᴏᴠɪᴅᴇ Mᴏᴠɪᴇs , Jᴜsᴛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ Aɴᴅ Eɴjᴏʏ..😎"""
    HELP_TXT = """Hᴇʟʟᴏ👋{}
 I Cᴀɴ Gᴜɪᴅᴇ Yᴏᴜ Tʜʀᴏᴜɢʜ Aʟʟ Oғ <a href='https://t.me/MovieTime02_Bot'>Mᴏᴠɪᴇ Tɪᴍᴇ Bᴏᴛ</a>  Cᴏᴏʟ Fᴇᴀᴛᴜʀᴇs Aɴᴅ Hᴏᴡ Tᴏ Pʀᴏᴘᴇʀʟʏ Usᴇ Tʜᴇᴍ. Usᴇ Tʜᴇ Bᴜᴛᴛᴏɴs Bᴇʟᴏᴡ Tᴏ Nᴀᴠɪɢᴀᴛᴇ Tʜʀᴏᴜɢʜ Aʟʟ Oғ Tʜᴇ Mᴏᴅᴜʟᴇs.."""
    ABOUT_TXT = """✯ Mʏ Nᴀᴍᴇ : Mᴏᴠɪᴇ Tɪᴍᴇ Bᴏᴛ 𝟸.𝟶
✯ Mʏ Cʀᴇᴀᴛᴏʀ : Aʟʟᴜ Aʀɪᴜɴ
✯ Mʏ Lᴀɴɢᴜᴀɢᴇ : Pʏᴛʜᴏɴ 𝟹
✯ Mʏ Lɪʙʀᴀʀʏ : Pʏʀᴏɢʀᴀᴍ
✯ Mʏ Dᴀᴛᴀʙᴀsᴇ : MᴏɴɢᴏDB
✯ Mʏ Sᴇʀᴠᴇʀ : Hᴇʀᴏᴋᴜ
✯ Mʏ Vᴇʀsɪᴏɴ : ᴠ𝟷.𝟶.𝟷 [Bᴇᴛᴀ]"""
    SOURCE_TXT = """<b>Movie Time Bot :</b>
~ Mᴏᴠɪᴇ Tɪᴍᴇ Bᴏᴛ Is A Nᴏᴛ Oᴘᴇɴ Sᴏᴜʀᴄᴇ Pʀᴏɪᴇᴄᴛ.."""
    MANUELFILTER_TXT = """Help: <b>Filters :</b>

- Fɪʟᴛᴇʀ Is Tʜᴇ Fᴇᴀᴛᴜʀᴇ Wᴇʀᴇ Usᴇʀs Cᴀɴ Sᴇᴛ Aᴜᴛᴏᴍᴀᴛᴇᴅ Rᴇᴘʟɪᴇs Fᴏʀ A Pᴀʀᴛɪᴄᴜʟᴀʀ Kᴇʏᴡᴏʀᴅ Aɴᴅ Tᴇssᴀ Wɪʟʟ Rᴇsᴘᴏɴᴅ Wʜᴇɴᴇᴠᴇʀ A Kᴇʏᴡᴏʀᴅ Is Fᴏᴜɴᴅ Tʜᴇ Mᴇssᴀɢᴇ..
<b>NOTE :</b>
𝟷. MovieTime02_Bot Sʜᴏᴜʟᴅ Hᴀᴠᴇ Aᴅᴍɪɴ Pʀɪᴠɪʟʟᴀɢᴇ.
𝟸. Oɴʟʏ Aᴅᴍɪɴs Cᴀɴ Aᴅᴅ Fɪʟᴛᴇʀs Iɴ A Cʜᴀᴛ.
𝟹. Aʟᴇʀᴛ Bᴜᴛᴛᴏɴs Hᴀᴠᴇ A Lɪᴍɪᴛ Oғ 𝟼𝟺 Cʜᴀʀᴀᴄᴛᴇʀs.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

~ MovieTime02_Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. MovieTime02_Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/MovieTime02_Bot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of tessa

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information..</code>
• /search  - <code>get the film information..</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
🎙️Group = {}(<code>{}</code>)
👥 Total Members = <code>{}</code>
 👤 Added By - {}
"""
    LOG_TEXT_P = """#NewUser
 -🆔 <code>{}</code>
👤 UserName - {}
"""