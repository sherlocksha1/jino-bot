class script(object):
    START_TXT = """đ·đŽđ»đŸ {},
đŒđą đđđđ , <a href='https://t.me/Samanth_abot'>đđđđđđđđ</a>, đžđ'đ đđđđą đđđđą đđđđ đđđ đđ đđ đąđđđ đđđđđ đđđ đđđđ đđ đđđđđ, đđđđđ đđđ đž'đđ đđđđđđđ đđđđđđ đđđđđ đż
"""
    HELP_TXT = """đ·đŽđ {}
đđŠđłđŠ đđŽ đđ©đŠ đđŠđ­đ± đđ°đł đđș đđ°đźđźđąđŻđ„đŽ."""
    ABOUT_TXT = """
   đđđąđšđ§ đ đŠđ
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
ââââââ° đđđđđđđđ â±âââ±âÛȘÛȘ
ââ­ââââââââââââââââŁ 
ââŁâȘŒ đŒđ đœđ°đŒđŽ - <a href="https://t.me/Samanth_abot"> đđđđđđđđ </a>
ââŁâȘŒ đČđđŽđ°đđŸđ- <a href="https://t.me/albintko"> đ°đ»đ±đžđœ </a>
ââŁâȘŒ đ»đžđ±đđ°đđ - đżđđđŸđ¶đđ°đŒ
ââŁâȘŒ đ»đ°đœđ¶đđ°đ¶đŽ - đżđđđ·đŸđœ đč
ââŁâȘŒ đłđ°đđ°đ±đ°đđŽ - đŒđŸđœđ¶đŸ đłđ±
ââŁâȘŒ đđŽđđđŽđ -  đ·đŽđđŸđșđ
ââŁâȘŒ đ±đđžđ»đ đđđ°đđ - v1.0.2 [ đ±đŽđđ° ]
ââ°ââââââââââââââââŁ âââââââââââââââââââââ±âÛȘÛȘ"""
    SOURCE_TXT = """<b>NOTE:</b>
- đ° đđ  đ đđđđ đđđđđđ đđđđđđđ. 
- ŐOááááŽ áOáȘáŽ - <a href="https://github.com/Samantha-a/Film-Club"> đđđđđ đđđ„đ </a>
  

<b>DEVS:</b>
- <a href=https://t.me/albintko>đ°đ»đ±đžđœ</a>"""
    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- Give a user details
âą/whois :-give a user full details"""
    FUN_TXT ="""<b>GáŽáŽáŽs</b> 
    
<b>đČ NOTHING MUCH JUST SOME FUN THINGS</b>
tđđ đđđđ đźđđ: 
đŁ. /dice - Roll The Dice 
đ€. /Throw đđ /Dart - đłđ đŹđșđđŸ Drat 
3. /Runs - Jokes 
4. /Goal or /Shoot - To Make A Goal Or Shoot
5. /luck or /cownd - Spin the Lucky"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
âą /filter - <code>add a filter in chat</code>
âą /filters - <code>list all the filters of a chat</code>
âą /del - <code>delete a specific filter in chat</code>
âą /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    SONG_TXT = """<b>đŒSong DownloadđŒ</b>
Song Download Module, For Those Who Love Music

<b>đ Command đ</b>

- /song [Song Name] - To Download Music đ

<b>đUsageđ</b>
- Can Be Used By Everyone
- Works in bot pm

Made By @albintko"""
    PIN_TXT ="""<b>PIN MODULE</b>
<b>Pin :</b>

<b>All The Pin Related Commands Can Be Found Here; Keep Your Chat Up To Date On The Latest News With A Simple Pinned Message!</b>

<b>đ Commands & Usage:</b>

â /pin :- Pin The Message You Replied To Message To Send A Notification To Group Members
â /unpin :- Unpin The Current Pinned Message. If Used As A Reply, Unpins The Replied To Message"""
    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>

âą /paste [text] - paste the given text on Pasty

<b>NOTE:</b>

âą These commands works on both pm and group.
âą These commands can be used by any group member."""
    GTRANS_TXT = """Help: <b> TTS đ€ module:</b>

Translate text to speech

<b>Commands and Usage:</b>

âą /tts <text> : convert text to speech

<b>NOTE:</b>

âą IMDb should have admin privillage.
âą These commands works on both pm and group.
âą IMDb can translate texts to 200+ languages."""
    PINGS_TXT ="""<b>đ Ping:</b>

Helps you to know your ping đ¶đŒââïž

<b>Commands:</b>

âą /alive - To check you are alive.
âą /help - To get help 
âą /ping - To get your ping 
âą /repo - Source Code. 

<b>đčUsageđč :</b>

âą This commands can be used in pms and groups
âą This commands can be used buy everyone in the groups and bots pm
âą Share us for more features"""
    TELE_TXT = """<b>â«ïžHELP: TelegraphâȘïž</b>

Do as you wish with telegra.ph module!

</b>USAGE:</b>

đ€§ /telegraph - Send me Picture or Vide Under (5MB)

<b>NOTE:</b>

âą This Command Is Available in goups and pms
âą This Command Can be used by everyone"""
    JSON_TXT ="""<b>JSON:</b>

Bot returns json for all replied messages with /json

<b>Features:</b>

Message Editting JSON
Pm Support
Group Support

<b>Note:</b>

Everyone can use this command , if spaming happens bot will automatically ban you from the group."""
    PURGE_TXT = """<b>đŁPurgeđŁ</b>
    
Delete A Lot Of Messages From Groups! 
    
 <b>ADMIN</b> 

â /purge :- Delete All Messages From The Replied To Message, To The Current Message"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Samantha supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

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
âą /connect  - <code>connect a particular chat to your PM</code>
âą /disconnect  - <code>disconnect from a chat</code>
âą /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
âą /id - <code>get id of a specifed user.</code>
âą /info  - <code>get information about a user.</code>
âą /imdb  - <code>get the film information from IMDb source.</code>
âą /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
âą /logs - <code>to get the rescent errors</code>
âą /stats - <code>to get status of files in db.</code>
âą /delete - <code>to delete a specific file from db.</code>
âą /users - <code>to get list of my users and ids.</code>
âą /chats - <code>to get list of the my chats and ids </code>
âą /leave  - <code>to leave from a chat.</code>
âą /disable  -  <code>do disable a chat.</code>
âą /ban_user  - <code>to ban a user.</code>
âą /unban_user  - <code>to unban a user.</code>
âą /channel - <code>to get list of total connected channels</code>
âą /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """â đđŸđđ°đ» đ”đžđ»đŽđ: <code>{}</code>
â đđŸđđ°đ» đđđŽđđ: <code>{}</code>
â đđŸđđ°đ» đČđ·đ°đđ: <code>{}</code>
â đđđŽđł đđđŸđđ°đ¶đŽ: <code>{}</code> đŒđđ±
â đ”đđŽđŽ đđđŸđđ°đ¶đŽ: <code>{}</code> đŒđđ±"""
    LOG_TEXT_G = """#đđđ°đđ«đšđźđ©
âź đđ«đšđźđ© âșâș {}(<code>{}</code>)
âź đđšđ­đđ„ đđđŠđđđ«đŹ âșâș <code>{}</code>
âź đđđđđ đđČ âșâș {}
"""
    LOG_TEXT_P = """#đđđ°đđŹđđ«
âź đđ âșâș <code>{}</code>
âź đđđŠđ âșâș {}
"""
    REPORT_TXT = """â€ đđđ„đ©: RáŽáŽáŽÊáŽ â ïž

đđđđ đđđđđđđ đđđđđ đąđđ đđ đđđđđđ đ đđđđđđđ đđ đ đđđđ đđ đđđ đđđđđđ đđ đđđ đđđđđđđđđđ đđđđđ. đłđđ'đ đđđđđđ đđđđ đđđđđđđ.

â€ đđšđŠđŠđđ§đđŹ đđ§đ đđŹđđ đ:

âȘ/report đđ @admins - đłđ đđŸđđđđ đș đđđŸđ đđ đđđŸ đșđœđđđđ (đđŸđđđ đđ đș đđŸđđđșđđŸ)."""

    CORONA_TXT = """â€ đđđ„đ©: đąđđđđœđŸ

đđđđ đČđđđđđđ đđđđđ đąđđ đđ đđđđ  đđđąđđ đđđđđđđđđđđ đđđđđ đđđđđđ

â€ đđšđŠđŠđđ§đđŹ đđ§đ đđŹđđ đ:

âȘ /covid - đđđŸ đđđđ đŒđđđđșđđœ đđđđ đđđđ đŒđđđđđđ đđșđđŸ đđ đđŸđ đŒđđđđœđŸ đđđżđđđđșđđđđ

âđ€đđșđđđđŸ:
/covid đšđđœđđș"""

    URLSHORT_TXT = """â€ đđđ„đ©: đŽđđ đđđđđđđŸđ

đđđđ đđđđđđđ đđđđđ đąđđ đđ đđđđđ đ đđđ 

â€ đđšđŠđŠđđ§đđŹ đđ§đ đđŹđđ đ:

âȘ /short: đđđŸ đđđđ đŒđđđđșđđœ đđđđ đđđđ đđđđ đđ đđŸđ đđđđđđŸđœ đđđđđ

âđ€đđșđđđđŸ:
/short https://t.me/albintko"""

    VIDEO_TXT ="""đđđĄđ„ đđ€đ§ đżđ€đŹđŁđĄđ€đđ đŒđŁđź đđđđđ€ đđ§đ€đą đđ.

âą đđŽđąđšđŠ
đ đ°đ¶ đđąđŻ đđ°đžđŻđ­đ°đąđ„ đđŻđș đđȘđ„đŠđ° đđłđ°đź đ đ°đ¶đ”đ¶đŁđŠ

đđ€đŹ đđ€ đđšđ
âą đđșđ±đŠ /video or /mp4 đđŻđ„ (đđȘđ„đŠđ° Link)
âą đđčđąđźđ±đ­đŠ:
/đźđ±4 https://youtu.be/Your Link"""

    ZOMBIES_TXT = """đđđĄđ„ đđ€đ§ đđđđ 

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
âą /inkick - command with required arguments and i will kick members from group.
âą /instatus - to check current status of chat member from group.
âą /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
âą /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
âą /dkick - to kick deleted accounts."""

    IMAGE_TXT = """â€ đđđ„đ©: IáŽáŽÉąáŽ

đđđđ đđđđđđđ đđđđđ đąđđ đđ đđđđ đđđđđ đđđđą đđđđđđą 

â€ đđšđŠđŠđđ§đđŹ đđ§đ đđŹđđ đ:

âȘ đ©đđđ đđŸđđœ đđŸ đș đđđșđđŸ đđ đŸđœđđ âš

đŹđșđœđŸ đ»đ @Devil"""

    STICKER_TXT = """đđđĄđ„ đđ€đ§ đđ©đđđ đđ§ đđ
âą đđšđđđ
To Get Sticker ID
  â­ đđ€đŹ đđ€ đđšđ
â Reply To Any Sticker [/stickerid]"""

    YTTHUMB_TXT = """đđđĄđ„ đđ€đ§ đżđ€đŹđŁđĄđ€đđ đđ€đȘđ©đȘđđ đđđđđ€ đđđȘđąđđŁđđđĄ
â­đđ€đŹ đđ€ đđšđ
đđșđ±đŠ /ytthumb đđŻđ„ đđȘđ„đŠđ° đđȘđŻđŹ

âą đđčđąđźđ±đ­đŠ
/ytthumb https://youtu.be/yourlink"""

    ABOOK_TXT = """â€ đđđ„đ©: đ đđœđđđ»đđđ

đđđ đđđ đđđđđđđ đ đżđłđ” đđđđ đđ đ đđđđđ đđđđ đ đđđ đđđđ đđđđđđđ âŻ

â€ đđšđŠđŠđđ§đđŹ đđ§đ đđŹđđ đ:

âȘ /audiobook: đ±đŸđđđ đđđđ đŒđđđđșđđœ đđ đșđđ đŻđŁđ„ đđ đđŸđđŸđđșđđŸ đđđŸ đșđđœđđ"""

    FILE_TXT = """â€ đđđ„đ©: đ„đđđŸ đČđđđđŸ

đđđđ đđđđ đđđđđđđ đ đđđ đđđđđ đđđđđ đđđ đđđđ đąđđ đ đđđđđđđđđ đđđđ đ đđđ đđđđ đđđđ đ đđđ đđđđđ đđđđ đđđđđ đąđđ đđđđ đđ đđđđ đđđą đđđđđđđ đ đđđđđđ đđđđđđ đđ

â€ đđšđŠđŠđđ§đđŹ đđ§đ đđŹđđ đ:

âȘ /plink - đ±đŸđđđ đđ đșđđ đđŸđœđđș đđ đđŸđ đđđđ
âȘ /pbatch - đŽđđŸ đđđđ đđșđœđđș đđđđ đđđđ đđđđ đŒđđđđșđđœ
âȘ /batch - To create link for multiple post
âđ€đđșđđđđŸ:
/pbatch <code>https://t.me/Sflix2k/497 https://t.me/Sflix2k/498</code>"""

    GTRANS_TXT = """â€ đđđ„đ©: đŠđđđđđŸ đłđđșđđđđșđđŸđ

đđđđ đđđđđđđ đđđđđ đąđđ đđ đđđđđđđđđ đ đđđĄđ đđ đșđđ đđđđđđđđđ đąđđ đ đđđ. đđđđ đđđđđđđ đ đđđđ đđ đđđđ đđ đđđ đđđđđ âŻ

â€ đđšđŠđŠđđ§đđŹ đđ§đ đđŹđđ đ:

âȘ/tr - đłđ đđđșđđđđșđđŸđ đđŸđđđ đđ đș đđđŸđŒđđżđŒ đđșđđđđșđđŸ

â€ đ­đđđŸ:
đ¶đđđđŸ đđđđđ /tr đđđ đđđđđđœ đđđŸđŒđđżđ đđđŸ đđșđđđđșđđŸ đŒđđœđŸ

âđ€đđșđđđđŸ: /đđ đđ
âą đŸđ = đ€đđđđđđ
âą đđ = đŹđșđđșđđșđđșđ
âą đđ = đ§đđđœđ"""

    RESTRIC_TXT = """â€ đđđ„đ©: MáŽáŽáŽ đ«

đđđđđ đđđ đđđ đđđđđđđđ đ đđđđđ đđđđđ đđđ đđđ đđ đđđđđđ đđđđđ đđđđđ đđđđ đđđđđđđđđđđą.

âȘ/ban: đłđ đ»đșđ đș đđđŸđ đżđđđ đđđŸ đđđđđ.
âȘ/unban: đłđ đđđ»đșđ đș đđđŸđ đđ đđđŸ đđđđđ.
âȘ/tban: đłđ đđŸđđđđđșđđđđ đ»đșđ đș đđđŸđ.
âȘ/mute: đłđ đđđđŸ đș đđđŸđ đđ đđđŸ đđđđđ.
âȘ/unmute: đłđ đđđđđđŸ đș đđđŸđ đđ đđđŸ đđđđđ.
âȘ/tmute: đłđ đđŸđđđđđșđđđđ đđđđŸ đș đđđŸđ.

â€ đ­đđđŸ:
đ¶đđđđŸ đđđđđ /tmute đđ /tban đđđ đđđđđđœ đđđŸđŒđđżđ đđđŸ đđđđŸ đđđđđ.

âđ€đđșđđđđŸ: /đđ»đșđ 2đœ đđ /đđđđđŸ 2đœ.
đžđđ đŒđșđ đđđŸ đđșđđđŸđ: đ/đ/đœ. 
 âą đ = đđđđđđŸđ
 âą đ = đđđđđ
 âą đœ = đœđșđđ"""
    CREATOR_REQUIRED = """â<b>You have To Be The Group Creator To Do That.</b>"""
      
    INPUT_REQUIRED = "â **Arguments Required**"
      
    KICKED = """âïž Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """đź Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """â<b>I Am Not An Admin Here\n__Leaving This Chat, Add Me Again As Admin With Ban User Permission.</b>"""
      
    DKICK = """âïž Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>Collecting Users Information...</b>"""
      
    STATUS = """{}\n<b>Chat Member Status</b>**\n\n```<i>Recently``` - {}\n```Within Week``` - {}\n```Within Month``` - {}\n```Long Time Ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}</i>
"""
