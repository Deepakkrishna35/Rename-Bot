class Translation(object):
    START_TEXT = """<b>👋 HELLO {} 🥰, \n\nI'M A SIMPLE RENAMER + FILE TO VIDEO CONVERTER BOT WITH PERMENENT THUMBNAIL AND COSTUME CAPTION SUPPORT 🤩 \n\nSENT ANY TELEGRAM FILE OR VIDEO TO USE ME 📩</b>"""

    BANNED_USER_TEXT = "<b>SORRY! YOU ARE BANNED FROM USING THIS BOT 🚫. CONTACT @TitterBuck [ADMIN] FOR DETAILS...👨‍💻</b>" 
    DOWNLOAD_START = "<b>📥 DOWNLOADING TO MY SERVER ▣▣▣□□ PLEASE WAIT 🕛</b>"
    UPLOAD_START = "<b>✅ DOWNLOADING COMPLETED. 📤 UPLOADING TO TELEGRAM ▣▣▣□□</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG = "<b>THANKYOU FOR USING ME 💞. HAVE A NICE DAY 🥰 \n\n@Cinemagram_Links</b>"
    SAVED_CUSTOM_THUMB_NAIL = "<b>YOUR PERMENENT THUMBANAIL SAVED SUCCESSFULLY ✅️</b>"
    DEL_ETED_CUSTOM_THUMB_NAIL = "YOUR THUMBANAIL DELETED SUCCESSFULLY 🚮"
    SAVED_RECVD_DOC_FILE = "<b>FILE DOWNLOADED SUCCESSFULLY ✅️</b>"
    REPLY_TO_DOC_FOR_RENAME_FILE = "<b>PLEASE REPLY TO AN FILE WITH /rename FIL NAME EXTENSION TO RENAME A FILE 🔰</b>"
    REPLY_TO_FILE_FOR_CONVERT = "<b>PLEASE REPLY TO AN FILE WITH /c2v TO CONVERT IT INTO STREAMABLE VIDEO FILE 🔰</b>"
    CUSTOM_CAPTION_UL_FILE = " "
    NO_THUMB_FOUND = "<b>NO THUMBANAIL FOUND 🧐. PLEASE SENT ME A IMAGE FOR YOUR PERMENENT THUMBANAIL 📩</b>"
    IFLONG_FILE_NAME = """<b>😳 PLEASE DECREASE THE NUMBER OF LETTERS 🤯</b>"""
    ABOUT_ME = """<b>
➣ MY NAME : CMG RENAME BOT
➣ CREATOR : <a href='https://t.me/TitterBuck'>☬ 𝔻𝔼𝔼ℙ𝔸𝕂 ☬</a>
➣ LANGUAGE : <a href='https://www.python.org/'>PYTHON-3</a>
➣ LIBRARY : <a href='https://docs.pyrogram.org/'>PYROGRAM</a>
➣ SERVER : <a href='https://dashboard.heroku.com/'>HEROKU</a>
➣ SOURCE : <a href='https://github.com/TitterBuck/CMGRENAMERBOT'>𝖳𝗁𝗂𝗌 𝖯𝖾𝗋𝗌𝗈𝗇</a>
</b>"""
    HELP_USER = """Checkout The Available Commands Here \n\n If you Like Me Support Us @DK_BOTx❤️"""
    RENAME_HELP = """Here are The Available Commands In Reanme \n\n\n▪️ <code>/rename</code> : Reply To An File/video With <code>/rename Filename.extension</code> For Renaming"""
    C2V_HELP = """Here Are The Available Commands In File To Video \n\n\n ▪️<code>/c2v</code> : Reply To An File With /c2v To Convert It Into Video"""
    THUMBNAIL_HELP = """Here Are The Available Commands In Custom Thumbnail \n\n\n ▪️ Send A Photo To Set The Custom Thumbnail \n▪️ <code>/showthumb</code> : For Checking The Current Thumbnail \n▪️<code>/delthumb</code> : For Deleting The Current Saved Thumbnail"""
    CCAPTION_HELP = """Here Are The Available Commands In Custom Caption \n\n\n ▪️<code>/scaption</code> Use This Command To Save Your Custom Caption \n<b>Usage:</b> <code>/scaption your caption text</code> \n\n<b>[You Can Use</b> <code>{filename}</code> <b>For showing new file name in the caption]</b> """
