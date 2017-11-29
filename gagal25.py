# -*- coding: utf-8 -*-

import TOBY
import requests
from TOBY.lib.curve.ttypes import *
from datetime import datetime
# https://kaijento.github.io/2017/05/19/web-scraping-youtube.com/
# from imgurpython import ImgurClient
import time,random,sys,json,codecs,threading,glob,re

cl = TOBY.LINE()
cl.login(token="EnbuP9B7OVGuH9cArLS5.WNg9GMfzJ2PUNEo6MWpIDq.z0OXlg1VwyHdZFnlb6oFNy1xhRrXudgNCFxzlH7SJ9Y=")
cl.loginResult
print("AramelBOT")
print("mid -> " + cl.mid)
#print("name -> " + cl.getProfile())
print("authToken -> " + cl.authToken)
print("cert -> " + cl.cert if cl.cert is not None else "")

ki = TOBY.LINE()
ki.login(token="EmkbU91Xd96k5ggJanu3.kjVcuvbf52Xt7Rtrvm2xaW.+yG7Pna69tibWmut3ddEjKnhTqC8EDLxi6M1bo4BxUI=")
ki.loginResult
print("AramelBOT")
print("mid -> " + ki.mid)
#print("name -> " + contact.displayName)
print("authToken -> " + ki.authToken)
print("cert -> " + ki.cert if ki.cert is not None else "")

kk = TOBY.LINE()
kk.login(token="Emmrdsq9gV07HXoC2ZS9.e7J8ohFOuN6VJsWG8nlDUq.0snD8rbh0JYU7neGAdF1yR7qBjpvcHiR+649NmhRCaw=")
kk.loginResult
print("AramelBOT")
print("mid -> " + kk.mid)
#print("name -> " + contact.displayName)
print("authToken -> " + kk.authToken)
print("cert -> " + kk.cert if kk.cert is not None else "")

kc= TOBY.LINE()
kc.login(token="EmbT6xHk69M9n1bwbaq7.z30tt8NBUGVxWXaefeOfzW.RgzW786fVpxgwSJM02kZpBUN/czyIZzWmPBbVO4BeyY=")
kc.loginResult
print("AramelBOT")
print("mid -> " + kc.mid)
#print("name -> " + contact.displayName)
print("authToken -> " + kc.authToken)
print("cert -> " + kc.cert if kc.cert is not None else "")

ks = TOBY.LINE()
ks.login(token="EmhL6KpoWOZ8ZRHPmPX1.0fEXCoMNRL9G62t3FFQzGq.7AgZh41NyM6FqwxXXqfZZ/m8XtP2MjPWraK9NOZ0Fpo=")
ks.loginResult
print("AramelBOT")
print("mid -> " + ks.mid)
#print("name -> " + contact.displayName)
print("authToken -> " + ks.authToken)
print("cert -> " + ks.cert if ks.cert is not None else "")

satpam= TOBY.LINE()
satpam.login(token="EmEEbYNRVgRJD8uLwbg1.LLLjtExV6NJ2o7fP7VrAOq.+J6cEBk9IqF6QdOIw4KjOgmyA+hf1y1m7LnkjRXds2M=")
satpam.loginResult
print("AramelBOT")
print("mid -> " + satpam.mid)
#print("name -> " + contact.displayName)
print("authToken -> " + satpam.authToken)
print("cert -> " + satpam.cert if satpam.cert is not None else "")

#ki = TOBY.LINE()
#ki.login(qr=True)
#ki.loginResult

#kk = TOBY.LINE()
#kk.login(qr=True)
#kk.loginResult

#kc = TOBY.LINE()
#kc.login(qr=True)
#kc.loginResult

#ks = TOBY.LINE()
#ks.login(qr=True)
#ks.loginResult

#satpam = TOBY.LINE() # Login Pake Akun Utama Kalian(Gunanya Supaya Akun Utama Ke Kick bisa Terima Undangan dari Bot Otomatis)
#satpam.login(qr=True)
#satpam.loginResult()

#client_id = ''
#client_secret = ''
#access_token = ''
#refresh_token = ''

# client = ImgurClient(client_id, client_secret, access_token, refresh_token)


#ki = kk = kc = cl 

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

album = None
image_path = 'tmp/tmp.jpg'

helpMessage =""" DuduL BOT Menu 􀔃􀄆red check mark􏿿
==============
⇨command member
⇨command creator
⇨command admin
⇨command mimic
⇨command protect
⇨command kicker
⇨command chat
⇨command sticker
==============
BOT : duduL
Aogiri Cyber Line
=============="""

commandmember =""" DuduL BOT Menu 􀔃􀄆red check mark􏿿
==============
    ⇨member
==============
☫ Gcreator
☫ Creator
☫ duduL say
☫ .music
☫ .Youtube
==============
BOT : duduL
Aogiri Cyber Line
=============="""

commandcreator =""" DuduL BOT Menu 􀔃􀄆red check mark􏿿
==============
    ⇨creator
==============
☫ Admin add @
☫ Admin remove @
☫ Adminlist
☫ Bot Add @
☫ Bot out
☫ GL Id
☫ Glist
☫ InviteMeTo:
==============
BOT : duduL
Aogiri Cyber Line
=============="""

commandadmin =""" DuduL BOT Menu 􀔃􀄆red check mark􏿿
==============
    ⇨admin
==============
☫ Id
☫ Mid
☫ aramel1 mid
☫ aramel2 mid
☫ aramel3 mid
☫ Mid @
☫ Me
☫ aramel1
☫ aramel2
☫ aramel3
☫ Cury PP
☫ Ginfo
☫ Gn
☫ aramel1 gn
☫ aramel2 gn
☫ aramel3 gn
☫ Cname:
☫ Cname2:
☫ Cname3:
☫ Cname4:
☫ Cname5:
☫ Cstatus:
☫ Gcreator:inv
☫ Cn
☫ aramel1 rename
☫ aramel2 rename
☫ Respon
☫ Tagall
☫ Apakah
☫ Rate
☫ Spam:
☫ Check > Nyimak
☫ Steal [Mid]
☫ Steal @
☫ Bot like
☫ Like temen
☫ Speed
☫ random:
☫ fakecat
☫ Group id
☫ Status
☫ Add comment
☫ Comment
☫ Comment:
☫ Message add:
☫ Message change
☫ Mayhem
☫ album remove at
==============
BOT : duduL
Aogiri Cyber Line
=============="""

commandmimic =""" DuduL BOT Menu 􀔃􀄆red check mark􏿿
==============
    ⇨mimic
==============
☫ Mimic:on
☫ Mimic:add: @
☫ Mimic:del: @
☫ ListTarget
==============
BOT : duduL
Aogiri Cyber Line
=============="""

commandprotect =""" DuduL BOT Menu 􀔃􀄆red check mark􏿿
==============
    ⇨protect
==============
☫ Share on
☫ Share off
☫ contact on 
☫ contact off
☫ mad on
☫ mad off
☫ Comment on
☫ Comment off
☫ Jam on
☫ Jam off
☫ joinn on
☫ joinn off
☫ Add on
☫ Add off
☫ Join on
☫ Join off
☫ Gname on
☫ Gname off
☫ Qr on
☫ Qr off
☫ guest on
☫ guest off
☫ Leave on
☫ Leave off
☫ Urlon
☫ Urloff
☫ Status
☫ Protect On
☫ Protect Off
==============
BOT : duduL
Aogiri Cyber Line
=============="""

commandchat =""" DuduL BOT Menu 􀔃􀄆red check mark􏿿
==============
    ⇨chat
==============
☫ Respon
☫ bunda aramel
☫ duduL say
☫ Test
☫ hmm
☫ wkwkwk
☫ bunda
☫ welcome
==============
BOT : duduL
Aogiri Cyber Line
=============="""

commandkicker =""" DuduL BOT Menu 􀔃􀄆red check mark􏿿
==============
    ⇨kicker
==============
☫ Blasklist @
☫ Kick [mid]
☫ Nk @
☫ Vk @
☫ Unban [kontak]
☫ Ban [kontak]
☫ Cek ban
☫ Banlist
☫ Cleanse
☫ aramel cancel
☫ Cancel
☫ Clear
☫ Cancellall
☫ Out
☫ left
☫ left all
☫ Bye aramel1
☫ Bye aramel2
☫ Bye aramel3
☫ aramel in
☫ aramel2 in
☫ aramel3 in
☫ aramel4 in
☫ aramel join
☫ aramel1 join
☫ aramel2 join
☫ aramel3 join
☫ Gurl
☫ aramel1 gurl
☫ aramel2 gurl
☫ aramel3 gurl
☫ Kick [mid]
☫ aramel1 kick [mid]
☫ aramel2 kick [mid]
☫ aramel3 kick [mid]
☫ Invite [mid]
☫ aramel1 invite [mid]
☫ aramel2 invite [mid]
☫ aramel3 invite [mid]
☫ aramel1 ourl
☫ aramel2 ourl
☫ aramel3 ourl
☫ jointicket
☫ aramel1 curl
☫ aramel2 curl
☫ aramel3 curl
☫ Invite
☫ Ban @ 
☫ Unban @
☫ Kill Ban
☫ Kill @
☫ Gcancel:
==============
BOT : duduL
Aogiri Cyber Line
=============="""

commandsticker =""" DuduL BOT Menu 􀔃􀄆red check mark􏿿
==============
    ⇨sticker
==============
☫ Hmmm
☫ Wc
☫ Lol
☫ Haaa
☫ Please
☫ Hadeuh
☫ You
☫ Galon
☫ Hehehe
☫ Wkwk
☫ Gift
☫ aramel1 gift
☫ aramel2 gift
☫ aramel3 gift
☫ All gift
==============
BOT : duduL
Aogiri Cyber Line
=============="""


KAC=[cl,ki,kk,kc,ks]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = ks.getProfile().mid
Smid = satpam.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid,Dmid,Smid,"u5efaf24f5f7cdf8b3aa30960bf4f9c52"]
admin=["u5efaf24f5f7cdf8b3aa30960bf4f9c52","u31b521fe93c9530357936576ba4a8f3d","uc271bd8261598f6a6e9de3ba9b03e275","u677d134fc9dbba0bd7c31004144a0567","u13b8fc3877e8527eaf8d2c20f0d2ddb9","u289bc2515045e76c53eeb4d154cd9703","ud057b170e9a7ae5f60eb64f77dfa9981","u9659494de5efea78f63bb169eef45aa1"]
creator=["u31b521fe93c9530357936576ba4a8f3d"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoJoin2':True,
    'autoJoin3':True,
    'autoJoin4':True,
    'autoJoin5':True,
    'autoCancel':{"on":True,"members":1},
    'autoCancel2':{"on":True,"members":1},
    'autoCancel3':{"on":True,"members":1},
    'autoCancel4':{"on":True,"members":1},
    'autoCancel5':{"on":True,"members":1},
    'leaveRoom':True,
    'leaveRoom2':True,
    'leaveRoom3':True,
    'leaveRoom4':True,
    'leaveRoom5':True,
    'timeline':True,
    'autoAdd':False,
    'message':"✒ AcL一�:緑\n\n✒ Http://line.me/ti/p/~4r4m3l \n✒ line://ti/p/~adinda_pratiwie",
    "lang":"JP",
    "comment":"Auto Like By✒ AcL一�:緑\n\n✒ Http://line.me/ti/p/~4r4m3l \n✒ line://ti/p/~adinda_pratiwie",
    "commentOn":False,
    "likeOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "MemberJoin":False,
    "MemberLeft":False,
    "clock":False,
    "cName":"Tetsu ",
    "cName2":"Akashi ",
    "cName3":"Aomine ",
    "cName4":"Taiga ",
	"cName5":"Kise ",
	#"cName6":"Atsusi ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectguest":False,
	"Protectjoin":False,
    "Protectcancel":False,
    "ProtectGroup":False,
    "Protectgroupname":False,
    "Protectpicture":False,
    "ProtectQR":False,
    "Protectmember":False,
    "Protectadmin":False,
    "Protectcreator":False,
    "Protectdisplayname":False,
    "Protectbmo":False,
    "Protectbmo2":False,	
    "protectionOn":True,
    "atjointicket":True,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    "winvite":{},
    'setTime':{},
    'ROM':{},
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
backup = ki.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kk.getProfile()
backup3 = kk.getProfile()
backup3.displayName = contact.displayName
backup3.statusMessage = contact.statusMessage
backup3.pictureStatus = contact.pictureStatus

contact = kc.getProfile()
backup4 = kc.getProfile()
backup4.displayName = contact.displayName
backup4.statusMessage = contact.statusMessage
backup4.pictureStatus = contact.pictureStatus

contact = ks.getProfile()
backup5 = ks.getProfile()
backup5.displayName = contact.displayName
backup5.statusMessage = contact.statusMessage
backup5.pictureStatus = contact.pictureStatus

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def upload_tempimage(client):
     '''
         #Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendImage(self, to_, path):
      M = Message(to=to_,contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M_id = self.Talk.client.sendMessage(0,M).id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e
 
def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n�9�9" + Name
                wait2['ROM'][op.param1][op.param2] = "�9�9" + Name
        else:
            pass
    except:
        pass

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            cl.acceptGroupInvitation(op.param1)
            print "cl done masuk grup"
        if op.type == 13:
            ki.acceptGroupInvitation(op.param1)
            print "ki done masuk grup"
        if op.type == 13:
            kk.acceptGroupInvitation(op.param1)
            print "kk done masuk grup"
        if op.type == 13:
            kc.acceptGroupInvitation(op.param1)
            print "kc done masuk group"
        if op.type == 13:
            ks.acceptGroupInvitation(op.param1)
            print "ks done masuk grup"
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        #if op.type == 10:
           #if wait["ProtectQR"] == True:
               #if op.param2 not in Bots:
                   #G = cl.getGroup(op.param1)
                   #G = ki.getGroup(op.param1)
                   #G.preventJoinByTicket = True
                   #ki.kickoutFromGroup(op.param1,[op.param2])
                   #cl.updateGroup(G)
#---------------------------- PROTECT QR ----------------------------------				   
        if op.type == 11:
           if wait["ProtectQR"] == True:
               if op.param2 not in Bots and admin:
                   G = random.choice(KAC).getGroup(op.param1)
                   G.preventJoinByTicket = True
                   random.choice(KAC).updateGroup(G)
                   G.preventJoinByTicket = False
                   random.choice(KAC).updateGroup(G)
                   Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                   satpam.acceptGroupInvitationByTicket(op.param1,Ticket)
                   satpam.kickoutFromGroup(op.param1,[op.param2])
                   G.preventJoinByTicket = True
                   random.choice(KAC).updateGroup(G)
                   satpam.updateGroup(G)
                   satpam.leaveGroup(op.param1)
                   random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + " jangan buka tutup qr, ganti nama, maupun cover grup")	
                   wait["blacklist"][op.param2] = True
                   print "kicked open close qr"
               else:
                   pass
#-----------------------------------------------------------------------------
#---------------------------- PROTECT GNAME ----------------------------------					   
        if op.type == 11:
           if wait["Protectgroupname"] == True:
               if op.param2 not in Bots and admin:
                   X = random.choice(KAC).getGroup(op.param1)
                   X.name = True
                   random.choice(KAC).updateGroup(X)
                   X.preventJoinByTicket = False
                   random.choice(KAC).updateGroup(X)
                   Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                   satpam.acceptGroupInvitationByTicket(op.param1,Ticket)
                   satpam.kickoutFromGroup(op.param1,[op.param2])
                   X.preventJoinByTicket = True
                   random.choice(KAC).updateGroup(X)
                   satpam.updateGroup(X)
                   satpam.leaveGroup(op.param1)	
                   random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + " jangan buka tutup qr, ganti nama, maupun cover grup")	
                   wait["blacklist"][op.param2] = True
                   print "kicked change name"
               else:
                   pass
#-----------------------------------------------------------------------------
#---------------------------- PROTECT IMAGE ----------------------------------				   
        if op.type == 11:
           if wait["Protectpicture"] == True:
               if op.param2 not in Bots and admin:
                   Y = random.choice(KAC).getGroup(op.param1)
                   Y.picture = True
                   random.choice(KAC).updateGroup(Y)
                   Y.preventJoinByTicket = False
                   random.choice(KAC).updateGroup(Y)
                   Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                   satpam.acceptGroupInvitationByTicket(op.param1,Ticket)
                   satpam.kickoutFromGroup(op.param1,[op.param2])
                   Y.preventJoinByTicket = True
                   random.choice(KAC).updateGroup(Y)
                   satpam.updateGroup(Y)
                   satpam.leaveGroup(op.param1)
                   random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + " jangan buka tutup qr, ganti nama, maupun cover grup")	
                   wait["blacklist"][op.param2] = True
                   print "kicked change cover group"
               else:
                   pass
#-----------------------------------------------------------------------------
#---------------------------- PROTECT DIPLAYNAME -----------------------------			   
        if op.type == 11:
           if wait["Protectdisplayname"] == True:
               if op.param2 not in Bots and admin:
                   Z = random.choice(KAC).getGroup(op.param1)
                   Z.displayName = True
                   random.choice(KAC).updateGroup(Z)
                   Z.preventJoinByTicket = False
                   random.choice(KAC).updateGroup(Z)
                   Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                   satpam.acceptGroupInvitationByTicket(op.param1,Ticket)
                   satpam.kickoutFromGroup(op.param1,[op.param2])
                   Z.preventJoinByTicket = True
                   random.choice(KAC).updateGroup(Z)
                   satpam.updateGroup(Z)
                   satpam.leaveGroup(op.param1)
                   wait["blacklist"][op.param2] = True
                   print "kicked TAG"
               else:
                   pass
#-----------------------------------------------------------------------------
#---------------------------- PROTECT GUEST ----------------------------------				   
        if op.type == 13:
           if wait["Protectguest"] == True:
               if op.param2 not in Bots and admin:
                  random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  wait["blacklist"][op.param2] = True
                  print "kicked invite member"
               else:
                  pass
#---------------------------------------------------------------------------------
#---------------------------- BL INVITE KICK -------------------------------------			  
        if op.type == 13:
            if op.param3 not in Bots and admin:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
#--------------------------------------------------------------------------------
#---------------------------- MEMBER MASUK SAPA ----------------------------------				  
        if op.type == 17:
            if wait["MemberJoin"] == True:
                if op.param2 in Bots:
                    return
                ginfo = cl.getGroup(op.param1)
                ki.sendText(op.param1, "☆⇨Selamat Datang Di Grup ⇦☆ \n" + str(ginfo.name))
                ki.sendText(op.param1, " ⇨OwnerGrup⇦ " + str(ginfo.name) + " :\n" + ginfo.creator.displayName)
                kk.sendText(op.param1, "semoga betah kaka")
                print "MemberJoin"
#--------------------------------------------------------------------------------
#---------------------------- MEMBER LEFT SAPA ----------------------------------								
        if op.type == 15:
            if wait["MemberLeft"] == True:
                if op.param2 in Bots:
                    return
                ki.sendText(op.param1,"  bye ka")
                print "MemberLeft"
#--------------------------------------------------------------------------------
#---------------------------- CANCEL INVITE KICK --------------------------------						  
        if op.type == 32:
          if wait["Protectcancel"] == True:
            if op.param2 not in Bots and admin:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              cl.inviteIntoGroup(op.param1,[op.param3])
              wait["blacklist"][op.param2] = True
              print "kicked cancel invitation"
            else:
              pass
#--------------------------------------------------------------------------------
#---------------------------- BL MASUK KICK -------------------------------------			  
        if op.type == 17:
            if op.param2 not in Bots and admin:
                joinblacklist = op.param2.replace("��",',')
                joinblacklistX = joinblacklist.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, joinblacklistX)
                if matched_list == []:
                    pass
                else:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2]) 
#--------------------------------------------------------------------------------
#---------------------------- AUTO JOIN CANCEL-----------------------------------
        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
						
            if Amid in op.param3:
                G = ki.getGroup(op.param1)
                if wait["autoJoin2"] == True:
                    if wait["autoCancel2"]["on"] == True:
                        if len(G.members) <= wait["autoCancel2"]["members"]:
                            ki.rejectGroupInvitation(op.param1)
                        else:
                            ki.acceptGroupInvitation(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                elif wait["autoCancel2"]["on"] == True:
                    if len(G.members) <= wait["autoCancel2"]["members"]:
                        ki.rejectGroupInvitation(op.param1)

            if Bmid in op.param3:
                G = kk.getGroup(op.param1)
                if wait["autoJoin3"] == True:
                    if wait["autoCancel3"]["on"] == True:
                        if len(G.members) <= wait["autoCancel3"]["members"]:
                            kk.rejectGroupInvitation(op.param1)
                        else:
                            kk.acceptGroupInvitation(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                elif wait["autoCancel3"]["on"] == True:
                    if len(G.members) <= wait["autoCancel3"]["members"]:
                        kk.rejectGroupInvitation(op.param1)

            if Cmid in op.param3:
                G = kc.getGroup(op.param1)
                if wait["autoJoin4"] == True:
                    if wait["autoCancel4"]["on"] == True:
                        if len(G.members) <= wait["autoCancel4"]["members"]:
                            kc.rejectGroupInvitation(op.param1)
                        else:
                            kc.acceptGroupInvitation(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                elif wait["autoCancel4"]["on"] == True:
                    if len(G.members) <= wait["autoCancel4"]["members"]:
                        kc.rejectGroupInvitation(op.param1)

            if Dmid in op.param3:
                G = ks.getGroup(op.param1)
                if wait["autoJoin5"] == True:
                    if wait["autoCancel5"]["on"] == True:
                        if len(G.members) <= wait["autoCancel5"]["members"]:
                            ks.rejectGroupInvitation(op.param1)
                        else:
                            ks.acceptGroupInvitation(op.param1)
                    else:
                        ks.acceptGroupInvitation(op.param1)
                elif wait["autoCancel5"]["on"] == True:
                    if len(G.members) <= wait["autoCancel5"]["members"]:
                        ks.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
#--------------------------------------------------------------------------------
#---------------------------- MEMBER MASUK KICK ---------------------------------					
        if op.type == 17: #awal 17 ubah 13
           if wait["Protectjoin"] == True:
               if op.param2 not in admin and Bots: # Awalnya admin doang
                   random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
				
        if op.type == 19: #Member Ke Kick dan di invite bot
            if wait["Protectmember"] == True:
                if op.param2 in Bots:
                  pass
                if op.param2 in admin:
                  pass
                else:
                  try:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    cl.inviteIntoGroup(op.param1,[op.param3])	
                    wait["blacklist"][op.param2] = True	
                    print "kicked kick member"	
                  except:	
                    pass
#--------------------------------------------------------------------------------
#---------------------------- MEMBER KICK ADMIN KICK ----------------------------
        if op.type == 19:
          if wait["Protectadmin"] == True:  		
            if op.param3 in admin: #Kalo Admin ke Kick
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  cl.inviteIntoGroup(op.param1,creator)
                  wait["blacklist"][op.param2] = True
                  print "kicked kick admin"	
            else:	
                  pass                  
#--------------------------------------------------------------------------------
#---------------------------- MEMBER KICK CREATOR KICK --------------------------			
        if op.type == 19:
          if wait["Protectcreator"] == True:  		
            if op.param3 in creator: #Kalo creator ke Kick
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  cl.inviteIntoGroup(op.param1,creator)
                  wait["blacklist"][op.param2] = True
                  print "kicked kick owner"	
            else:	
                  pass
#--------------------------------------------------------------------------------
#---------------------------- MEMBER KICK BOT KICK ------------------------------
        if op.type == 19: #Member Ke Kick
          if wait["Protectbmo"] == True:  
            if op.param2 in Bots:
              pass
            if op.param2 in admin:
              pass
            else:
              try:
                G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                random.choice(KAC).updateGroup(G)
                Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                G.preventJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                wait["blacklist"][op.param2] = True
                print "kicked bot t1"
              except:
                pass
			  
        if op.type == 19: #bot ke kick di invite via link
          if wait["Protectbmo2"] == True:  
            if op.param2 in Bots:
              pass
            if op.param2 in admin:
              pass
            else:
              try:
                X = random.choice(KAC).getGroup(op.param1)
                X.preventJoinByTicket = False
                random.choice(KAC).updateGroup(X)
                Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                satpam.acceptGroupInvitationByTicket(op.param1,Ticket)
                satpam.kickoutFromGroup(op.param1,[op.param2])
                X = satpam.getGroup(op.param1)
                X.preventJoinByTicket = False
                satpam.updateGroup(X)
                satpam.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                X.preventJoinByTicket = True
                random.choice(KAC).updateGroup(X)
                satpam.updateGroup(X)
                satpam.leaveGroup(op.param1)
                wait["blacklist"][op.param2] = True
                print "kicked bot t2"
              except:
                pass

#--------------------------------------------------------------------------------
#---------------------------- AUTO JOIN CANCEL-----------------------------------

        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)

            if Amid in op.param3:
                G = ki.getGroup(op.param1)
                if wait["autoJoin2"] == True:
                    if wait["autoCancel2"]["on"] == True:
                        if len(G.members) <= wait["autoCancel2"]["members"]:
                            ki.rejectGroupInvitation(op.param1)
                        else:
                            ki.acceptGroupInvitation(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                elif wait["autoCancel2"]["on"] == True:
                    if len(G.members) <= wait["autoCancel2"]["members"]:
                        ki.rejectGroupInvitation(op.param1)

            if Bmid in op.param3:
                G = kk.getGroup(op.param1)
                if wait["autoJoin3"] == True:
                    if wait["autoCancel3"]["on"] == True:
                        if len(G.members) <= wait["autoCancel3"]["members"]:
                            kk.rejectGroupInvitation(op.param1)
                        else:
                            kk.acceptGroupInvitation(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                elif wait["autoCancel3"]["on"] == True:
                    if len(G.members) <= wait["autoCancel3"]["members"]:
                        kk.rejectGroupInvitation(op.param1)

            if Cmid in op.param3:
                G = kc.getGroup(op.param1)
                if wait["autoJoin4"] == True:
                    if wait["autoCancel4"]["on"] == True:
                        if len(G.members) <= wait["autoCancel4"]["members"]:
                            kc.rejectGroupInvitation(op.param1)
                        else:
                            kc.acceptGroupInvitation(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                elif wait["autoCancel4"]["on"] == True:
                    if len(G.members) <= wait["autoCancel4"]["members"]:
                        kc.rejectGroupInvitation(op.param1)

            if Dmid in op.param3:
                G = ks.getGroup(op.param1)
                if wait["autoJoin5"] == True:
                    if wait["autoCancel5"]["on"] == True:
                        if len(G.members) <= wait["autoCancel5"]["members"]:
                            ks.rejectGroupInvitation(op.param1)
                        else:
                            ks.acceptGroupInvitation(op.param1)
                    else:
                        ks.acceptGroupInvitation(op.param1)
                elif wait["autoCancel5"]["on"] == True:
                    if len(G.members) <= wait["autoCancel5"]["members"]:
                        ks.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
#--------------------------------------------------------------------------------
#---------------------------- LEAVE ROOM ----------------------------------------
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message

        if op.type == 22:
            if wait["leaveRoom2"] == True:
                ki.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom2"] == True:
                ki.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join2:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            ki.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = ki.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            ki.updateGroup(X)
                        except:
                            ki.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom2"] == True:
                    ki.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                ki.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
			
        if op.type == 22:
            if wait["leaveRoom3"] == True:
                kk.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom3"] == True:
                kk.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join3:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            kk.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = kk.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            kk.updateGroup(X)
                        except:
                            kk.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom3"] == True:
                    kk.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                kk.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
			
        if op.type == 22:
            if wait["leaveRoom4"] == True:
                kc.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom4"] == True:
                kc.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join4:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            kc.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = kc.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            kc.updateGroup(X)
                        except:
                            kc.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom4"] == True:
                    kc.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                kc.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message

        if op.type == 22:
            if wait["leaveRoom5"] == True:
                ks.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom5"] == True:
                ks.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join5:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            ks.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = ks.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            ks.updateGroup(X)
                        except:
                            ks.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom5"] == True:
                    ks.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                ks.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
#--------------------------------------------------------------------------------
#---------------------------- BL WL ---------------------------------------------
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to," dihapus dari daftar blacklist")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to," tidak ada dalam daftar blacklist")
						
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to," sudah ada di daftar blacklist")

                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to," ditambahkan ke daftar blacklist")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to," dihapus dari daftar blacklist")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to," tidak ada dalam daftar blacklist")
#-----------------------------------------------------------------------------
#---------------------------- CONTACT ----------------------------------------						
               elif wait["contact"] == True:
                 if msg.from_ in admin:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
#--------------------------------------------------------------------------------
#---------------------------- INVITE SEND CONTACT -------------------------------
            if msg.contentType == 13:
            	if wait["winvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"⇨" + _name + " sudah ada di dalam grup")
                                 break
                             elif invite in wait["blacklist"]:
                                 ki.sendText(msg.to,"sorry, " + _name + "\n di dalam daftar blacklist")
                                 kk.sendText(msg.to,"untuk mengundang ke grup ikuti perintah seteleah tanda (➡) \n\n➡➡➡➡➡➡➡➡➡➡➡➡➡➡➡➡ \n\nUnban ➡ send contact")
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"success invite : \n➡" + _name)
                                     wait2["winvite"] = False
                                     break
                                 except:
                                     try:
                                         ki.findAndAddContactsByMid(invite)
                                         ki.inviteIntoGroup(op.param1,[invite])
                                         wait2["winvite"] = False
                                     except:
                                         cl.sendText(msg.to,"Negative, Error detected")
                                         wait2["winvite"] = False
                                         break
#------------------------------------------------------------------------------
#---------------------------- TIMELIN3 ----------------------------------------
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL�0�9�6�9��\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
#--------------------------------------------------------------------------------
#---------------------------- HELP KEY ------------------------------------------
            elif msg.text in ["Key","help","Help"]:
			    if msg.from_ in admin:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,helpMessage)
					else:
						cl.sendText(msg.to,helpt)
            elif msg.text in ["command member"]:
			    if msg.from_ in admin:
					if wait["lang"] == "JP":
						ki.sendText(msg.to,commandmember)
					else:
						ki.sendText(msg.to,membert)
            elif msg.text in ["command creator"]:
			    if msg.from_ in admin:
					if wait["lang"] == "JP":
						kk.sendText(msg.to,commandcreator)
					else:
						kk.sendText(msg.to,creatort)
            elif msg.text in ["command admin"]:
			    if msg.from_ in admin:
					if wait["lang"] == "JP":
						kc.sendText(msg.to,commandadmin)
					else:
						kc.sendText(msg.to,admint)
            elif msg.text in ["command mimic"]:
			    if msg.from_ in admin:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,commandmimic)
					else:
						cl.sendText(msg.to,mimict)
            elif msg.text in ["command protect"]:
			    if msg.from_ in admin:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,commandprotect)
					else:
						cl.sendText(msg.to,protectt)
            elif msg.text in ["command kicker"]:
			    if msg.from_ in admin:
					if wait["lang"] == "JP":
						ki.sendText(msg.to,commandkicker)
					else:
						ki.sendText(msg.to,kickert)
            elif msg.text in ["command chat"]:
			    if msg.from_ in admin:
					if wait["lang"] == "JP":
						kk.sendText(msg.to,commandchat)
					else:
						kk.sendText(msg.to,chatt)
            elif msg.text in ["command sticker"]:
			    if msg.from_ in admin:
					if wait["lang"] == "JP":
						kc.sendText(msg.to,commandsticker)
					else:
						kc.sendText(msg.to,stickert)
#--------------------------------------------------------------------------------
#---------------------------- INVITE VIA CONTACT --------------------------------						
            elif msg.text in ["Invite:on"]:
                if msg.from_ in admin:
                    wait["winvite"] = True
                    cl.sendText(msg.to,"kirim kontak")		

            elif msg.text in ["Invite:off"]:
                if msg.from_ in admin:
                    wait["winvite"] = False
                    cl.sendText(msg.to,"invite off")				 
#--------------------------------------------------------------------------------
#---------------------------- UBAH NAMA BOT -------------------------------------
            elif ("Gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Gn ","")
						cl.updateGroup(X)
					else:
						cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("aramel1 gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("aramel1 gn ","")
						ki.updateGroup(X)
					else:
						ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("aramel2 gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("aramel2 gn ","")
						kk.updateGroup(X)
					else:
						kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("aramel3 gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("aramel3 gn ","")
						kc.updateGroup(X)
					else:
						kc.sendText(msg.to,"It can't be used besides the group.")
            elif ("aramel4 gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("aramel4 gn ","")
						ks.updateGroup(X)
					else:
						ks.sendText(msg.to,"It can't be used besides the group.")						
#--------------------------------------------------------------------------------
#---------------------------- KICK VIA MID --------------------------------------
            elif "Kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Kick ","")
					cl.kickoutFromGroup(msg.to,[midd])
            elif "aramel1 kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("aramel1 kick ","")
					ki.kickoutFromGroup(msg.to,[midd])
            elif "aramel2 kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("aramel2 kick ","")
					kk.kickoutFromGroup(msg.to,[midd])
            elif "aramel3 kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("aramel3 kick ","")
					kc.kickoutFromGroup(msg.to,[midd])
            elif "aramel4 kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("aramel4 kick ","")
					ks.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Invite ","")
					cl.findAndAddContactsByMid(midd)
					cl.inviteIntoGroup(msg.to,[midd])
            elif "aramel1 invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("aramel1 invite ","")
					ki.findAndAddContactsByMid(midd)
					ki.inviteIntoGroup(msg.to,[midd])
            elif "aramel2 invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("aramel2 invite ","")
					kk.findAndAddContactsByMid(midd)
					kk.inviteIntoGroup(msg.to,[midd])
            elif "aramel3 invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("aramel3 invite ","")
					kc.findAndAddContactsByMid(midd)
					kc.inviteIntoGroup(msg.to,[midd])
            elif "aramel4 invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("aramel4 invite ","")
					ks.findAndAddContactsByMid(midd)
					ks.inviteIntoGroup(msg.to,[midd])
#-----------------------------------------------------------------------------
#---------------------------- MID BOT ----------------------------------------					
            elif msg.text in ["Me"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': mid}
					cl.sendMessage(msg)
            elif msg.text in ["aramel1"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Amid}
					ki.sendMessage(msg)
            elif msg.text in ["aramel2"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Bmid}
					kk.sendMessage(msg)
            elif msg.text in ["aramel3"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Cmid}
					kc.sendMessage(msg)

            elif msg.text in ["aramel4"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Dmid}
					ks.sendMessage(msg)
#--------------------------------------------------------------------------------
#---------------------------- KIRIM GIFT ----------------------------------------
            elif msg.text in ["æ„�1�7�ã®ãƒ�1�7�ãƒ¬ã�1�7�¼ãƒ³ãƒ˄1�7","Gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '5'}
					msg.text = None
					cl.sendMessage(msg)
            elif msg.text in ["æ„�1�7�ã®ãƒ�1�7�ãƒ¬ã�1�7�¼ãƒ³ãƒ˄1�7","aramel1 gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '6'}
					msg.text = None
					ki.sendMessage(msg)
            elif msg.text in ["æ„�1�7�ã®ãƒ�1�7�ãƒ¬ã�1�7�¼ãƒ³ãƒ˄1�7","aramel2 gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '8'}
					msg.text = None
					kk.sendMessage(msg)
            elif msg.text in ["æ„�1�7�ã®ãƒ�1�7�ãƒ¬ã�1�7�¼ãƒ³ãƒ˄1�7","aramel3 gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '10'}
					msg.text = None
					kc.sendMessage(msg)
            elif msg.text in ["æ„�1�7�ã®ãƒ�1�7�ãƒ¬ã�1�7�¼ãƒ³ãƒ˄1�7","aramel4 gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '10'}
					msg.text = None
					ks.sendMessage(msg)
            elif msg.text in ["æ„�1�7�ã®ãƒ�1�7�ãƒ¬ã�1�7�¼ãƒ³ãƒ˄1�7","All gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '12'}
					msg.text = None
					ki.sendMessage(msg)
					kk.sendMessage(msg)
					kc.sendMessage(msg)
					cl.sendMessage(msg)
					ks.sendMessage(msg)
#--------------------------------------------------------------------------------
#---------------------------- CANCEL INVITAN ------------------------------------
            elif msg.text in ["cancel","Cancel"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						if X.invitee is not None:
							gInviMids = [contact.mid for contact in X.invitee]
							cl.cancelGroupInvitation(msg.to, gInviMids)
						else:
							if wait["lang"] == "JP":
								cl.sendText(msg.to,"tidak ada")
							else:
								cl.sendText(msg.to,"Sorry, nobody absent")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["aramel cancel","Bot cancel"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						G = kc.getGroup(msg.to)
						if G.invitee is not None:
							gInviMids = [contact.mid for contact in G.invitee]
							kc.cancelGroupInvitation(msg.to, gInviMids)
						else:
							if wait["lang"] == "JP":
								kc.sendText(msg.to,"No invites👈")
							else:
								kc.sendText(msg.to,"Invite people inside not👈")
					else:
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"tidak ada undangan")
						else:
							kc.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
#-----------------------------------------------------------------------------
#---------------------------- BUKA QR ----------------------------------------
            elif msg.text in ["Ourl","Link on","Urlon"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = False
						cl.updateGroup(X)
						if wait["lang"] == "JP":
							cl.sendText(msg.to)
						else:
							cl.sendText(msg.to)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["aramel1 ourl","aramel1 link on"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = False
						ki.updateGroup(X)
						if wait["lang"] == "JP":
							ki.sendText(msg.to)
						else:
							ki.sendText(msg.to)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["aramel2 ourl","aramel2 link on"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kk.getGroup(msg.to)
						X.preventJoinByTicket = False
						kk.updateGroup(X)
						if wait["lang"] == "JP":
							kk.sendText(msg.to)
						else:
							kk.sendText(msg.to)
					else:
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Can not be used outside the group")
						else:
							kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["aramel3 ourl","aramel3 link on"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kc.getGroup(msg.to)
						X.preventJoinByTicket = False
						kc.updateGroup(X)
						if wait["lang"] == "JP":
							kc.sendText(msg.to)
						else:
							kc.sendText(msg.to)
					else:
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Can not be used outside the group")
						else:
							kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["aramel4 ourl","aramel4 link on"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = ks.getGroup(msg.to)
						X.preventJoinByTicket = False
						ks.updateGroup(X)
						if wait["lang"] == "JP":
							ks.sendText(msg.to)
						else:
							ks.sendText(msg.to)
					else:
						if wait["lang"] == "JP":
							ks.sendText(msg.to,"Can not be used outside the group")
						else:
							ks.sendText(msg.to,"Not for use less than group")
#--------------------------------------------------------------------------------
#---------------------------- CLOSE LINK ----------------------------------------
            elif msg.text in ["Curl","Link off","Urloff"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = True
						cl.updateGroup(X)
						if wait["lang"] == "JP":
							cl.sendText(msg.to)
						else:
							cl.sendText(msg.to)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["aramel1 curl","aramel1 link off"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = ki.getGroup(msg.to)
						X.preventJoinByTicket = True
						ki.updateGroup(X)
						if wait["lang"] == "JP":
							ki.sendText(msg.to)
						else:
							ki.sendText(msg.to)
					else:
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"Can not be used outside the group")
						else:
							ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["aramel2 curl","aramel2 link off"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kk.getGroup(msg.to)
						X.preventJoinByTicket = True
						kk.updateGroup(X)
						if wait["lang"] == "JP":
							kk.sendText(msg.to,)
						else:
							kk.sendText(msg.to)
					else:
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Can not be used outside the group")
						else:
							kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["aramel3 curl","aramel3 link off"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kc.getGroup(msg.to)
						X.preventJoinByTicket = True
						kc.updateGroup(X)
						if wait["lang"] == "JP":
							kc.sendText(msg.to)
						else:
							kc.sendText(msg.to)
					else:
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Can not be used outside the group")
						else:
							kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["aramel4 curl","aramel4 link off"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = ks.getGroup(msg.to)
						X.preventJoinByTicket = True
						ks.updateGroup(X)
						if wait["lang"] == "JP":
							ks.sendText(msg.to)
						else:
							ks.sendText(msg.to)
					else:
						if wait["lang"] == "JP":
							ks.sendText(msg.to,"Can not be used outside the group")
						else:
							ks.sendText(msg.to,"Not for use less than group")
#--------------------------------------------------------------------------------
#---------------------------- JOIN LEWAT LINK -----------------------------------
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
#--------------------------------------------------------------------------------
#---------------------------- GROUP INFO ----------------------------------------
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#------------------------------------------------------------------------------
#---------------------------- ID GROUP ----------------------------------------
            elif "Id" == msg.text:
				if msg.from_ in admin:
					cl.sendText(msg.to,msg.to)
#-----------------------------------------------------------------------------
#---------------------------- MID BOT ----------------------------------------
            elif "All mid" == msg.text:
				if msg.from_ in admin:
					cl.sendText(msg.to,mid)
					ki.sendText(msg.to,Amid)
					kk.sendText(msg.to,Bmid)
					kc.sendText(msg.to,Cmid)
					ks.sendText(msg.to,Dmid)

            elif "Mid" == msg.text:
				if msg.from_ in admin:
					cl.sendText(msg.to,mid)
            elif "aramel1 mid" == msg.text:
				if msg.from_ in admin:
					ki.sendText(msg.to,Amid)
            elif "aramel2 mid" == msg.text:
				if msg.from_ in admin:
					kk.sendText(msg.to,Bmid)
            elif "aramel3 mid" == msg.text:
				if msg.from_ in admin:
					kc.sendText(msg.to,Dmid)
            elif "aramel4 mid" == msg.text:
				if msg.from_ in admin:
					ks.sendText(msg.to,Dmid)
#--------------------------------------------------------------------------------
#---------------------------- BOT JAWAB STIKER ----------------------------------
            elif msg.text in ["Wkwk"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "100",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Hehehe"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "10",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Galon"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "9",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["You"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "7",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "6",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Please"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "4",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "3",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "110",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Hmmm"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "101",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
            elif msg.text in ["Wc"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "247",
										"STKPKGID": "3",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
#------------------------------------------------------------------------
#---------------------------- TL ----------------------------------------
            elif msg.text in ["Cury PP"]:
				if msg.from_ in admin:
					tl_text = msg.text.replace("TL","")
					cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
#-------------------------------------------------------------------------
#---------------------------- C N ----------------------------------------
            elif msg.text in ["Cn: "]:
				if msg.from_ in admin:
					string = msg.text.replace("Cn: ","")
					if len(string.decode('utf-8')) <= 20:
						profile = cl.getProfile()
						profile.displayName = string
						cl.updateProfile(profile)
						cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["aramel1 rename: "]:
				if msg.from_ in admin:
					string = msg.text.replace("aramel1 rename: ","")
					if len(string.decode('utf-8')) <= 20:
						profile_B = ki.getProfile()
						profile_B.displayName = string
						ki.updateProfile(profile_B)
						ki.sendText(msg.to,"name : " + string + " done")
            elif msg.text in ["aramel2 rename: "]:
				if msg.from_ in admin:
					string = msg.text.replace("aramel2 rename: ","")
					if len(string.decode('utf-8')) <= 20:
						profile_B = kk.getProfile()
						profile_B.displayName = string
						kk.updateProfile(profile_B)
						kk.sendText(msg.to,"name : " + string + " done")
#-------------------------------------------------------------------------
#---------------------------- M C ----------------------------------------
            elif msg.text in ["Mc "]:
				if msg.from_ in admin:
					mmid = msg.text.replace("Mc ","")
					msg.contentType = 13
					msg.contentMetadata = {"mid":mmid}
					cl.sendMessage(msg)
#--------------------------------------------------------------------------------
#---------------------------- FUNGSI ON OF --------------------------------------
            elif msg.text in ["Guest On","guest on"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Block On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Block On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Guest Off","guest off"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Block Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Block Off")
                    else:
                        cl.sendText(msg.to,"done")
						
            elif msg.text in ["Qr on","qr on"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr off","qr off"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
						
            elif msg.text in ["Gname on"]:
              if msg.from_ in admin:
                if wait["Protectgroupname"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Gname On")
                    else:
                        cl.sendText(msg.to,"Protect Gname On")
                else:
                    wait["Protectgroupname"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Gname On")
                    else:
                        cl.sendText(msg.to,"Protect Gname On")
				
            elif msg.text in ["Gname off"]:
              if msg.from_ in admin:			
                if wait["Protectgroupname"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Gname Off")
                    else:
                        cl.sendText(msg.to,"Protect Gname OFF")
                else:
                    wait["Protectgroupname"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Gname Off")
                    else:
                        cl.sendText(msg.to,"Protect Gname Off")
						
            elif msg.text in ["Image on"]:
              if msg.from_ in admin:
                if wait["Protectpicture"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Image On")
                    else:
                        cl.sendText(msg.to,"Protect Image On")
                else:
                    wait["Protectpicture"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Image On")
                    else:
                        cl.sendText(msg.to,"Protect Image On")
						
            elif msg.text in ["Image off"]:
              if msg.from_ in admin:			
                if wait["Protectpicture"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Image Off")
                    else:
                        cl.sendText(msg.to,"Protect Image OFF")
                else:
                    wait["Protectpicture"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Image Off")
                    else:
                        cl.sendText(msg.to,"Protect Image Off")
						
            elif msg.text in ["Member on"]:
              if msg.from_ in admin:
                if wait["Protectmember"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect member On")
                    else:
                        cl.sendText(msg.to,"Protect member On")
                else:
                    wait["Protectmember"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect member On")
                    else:
                        cl.sendText(msg.to,"Protect member On")
						
            elif msg.text in ["Member off"]:
              if msg.from_ in admin:			
                if wait["Protectmember"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect member Off")
                    else:
                        cl.sendText(msg.to,"Protect member OFF")
                else:
                    wait["Protectmember"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect member Off")
                    else:
                        cl.sendText(msg.to,"Protect member Off")
						
            elif msg.text in ["Admin on"]:
              if msg.from_ in admin:
                if wait["Protectadmin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect admin On")
                    else:
                        cl.sendText(msg.to,"Protect admin On")
                else:
                    wait["Protectadmin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect admin On")
                    else:
                        cl.sendText(msg.to,"Protect admin On")
						
            elif msg.text in ["Admin off"]:
              if msg.from_ in admin:			
                if wait["Protectadmin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect admin Off")
                    else:
                        cl.sendText(msg.to,"Protect admin OFF")
                else:
                    wait["Protectadmin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect admin Off")
                    else:
                        cl.sendText(msg.to,"Protect admin Off")
						
            elif msg.text in ["Owner on"]:
              if msg.from_ in admin:
                if wait["Protectcreator"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect owner On")
                    else:
                        cl.sendText(msg.to,"Protect owner On")
                else:
                    wait["Protectcreator"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect owner On")
                    else:
                        cl.sendText(msg.to,"Protect owner On")
						
            elif msg.text in ["Owner off"]:
              if msg.from_ in admin:			
                if wait["Protectcreator"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect owner Off")
                    else:
                        cl.sendText(msg.to,"Protect owner OFF")
                else:
                    wait["Protectcreator"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect owner Off")
                    else:
                        cl.sendText(msg.to,"Protect owner Off")
						
            elif msg.text in ["Protect On","Mode On"]:
              if msg.from_ in admin:
                if wait["ProtectGroup"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                    else:
                        cl.sendText(msg.to,"Protect Group On")
                else:
                    wait["ProtectGroup"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                    else:
                        cl.sendText(msg.to,"Protect Group On")
						
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Kick Joined Group On")
                    else:
                        ki.sendText(msg.to,"Kick Joined Group On")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Kick Joined Group On")
                    else:
                        ki.sendText(msg.to,"Kick Joined Group On")

                if wait["Protectcancel"] == True:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Protect Cancel On")
                    else:
                        kk.sendText(msg.to,"Protect Cancel On")
                else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Protect Cancel On")

                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Auto Block On")
                    else:
                        kc.sendText(msg.to,"Block On")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Auto Block On")
                    else:
                        kc.sendText(msg.to,"Block On")
						
                if wait["ProtectQR"] == True:
                    if wait["lang"] == "JP":
                        ks.sendText(msg.to,"Protect QR On")
                    else:
                        ks.sendText(msg.to,"Protect QR On")
                else:
                    wait["ProtectQR"] = True
                    if wait["lang"] == "JP":
                        ks.sendText(msg.to,"Protect QR On")
                    else:
                        ks.sendText(msg.to,"Protect QR On")

                if wait["Protectgroupname"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Gname On")
                    else:
                        cl.sendText(msg.to,"Protect Gname On")
                else:
                    wait["Protectgroupname"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Gname On")
                    else:
                        cl.sendText(msg.to,"Protect Gname On")

                if wait["Protectpicture"] == True:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Protect Image On")
                    else:
                        ki.sendText(msg.to,"Protect Image On")
                else:
                    wait["Protectpicture"] = True
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Protect Image On")
                    else:
                        ki.sendText(msg.to,"Protect Image On")
						
                if wait["Protectmember"] == True:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Protect member On")
                    else:
                        kk.sendText(msg.to,"Protect member On")
                else:
                    wait["Protectmember"] = True
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Protect member On")
                    else:
                        kk.sendText(msg.to,"Protect member On")

                if wait["Protectadmin"] == True:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Protect admin On")
                    else:
                        kc.sendText(msg.to,"Protect admin On")
                else:
                    wait["Protectadmin"] = True
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Protect admin On")
                    else:
                        kc.sendText(msg.to,"Protect admin On")

                if wait["Protectcreator"] == True:
                    if wait["lang"] == "JP":
                        ks.sendText(msg.to,"Protect owner On")
                    else:
                        ks.sendText(msg.to,"Protect owner On")
                else:
                    wait["Protectcreator"] = True
                    if wait["lang"] == "JP":
                        ks.sendText(msg.to,"Protect owner On")
                    else:
                        ks.sendText(msg.to,"Protect owner On")						

						
            elif msg.text in ["Protect Off","Mode Off"]:
              if msg.from_ in admin:
                if wait["ProtectGroup"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group Off")
                    else:
                        cl.sendText(msg.to,"Group OFF")
                else:
                    wait["ProtectGroup"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group Off")
                    else:
                        cl.sendText(msg.to,"Protect Group Off")
						
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"kick Joined Group Off")
                    else:
                        ki.sendText(msg.to,"kick Joined Group Off")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"kick Joined Group Off")
                    else:
                        ki.sendText(msg.to,"kick Joined Group Off")
						
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Protect Cancel Off")
                    else:
                        kk.sendText(msg.to,"Protect Cancel Off")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Protect Cancel Off")
                    else:
                        kk.sendText(msg.to,"Protect Cancel Off")
						
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Block Invite Off")
                    else:
                        kc.sendText(msg.to,"Block Invite Off")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Block Invite Off")
                    else:
                        kc.sendText(msg.to,"Block Invite Off")

                if wait["ProtectQR"] == False:
                    if wait["lang"] == "JP":
                        ks.sendText(msg.to,"Protect QR Off")
                    else:
                        ks.sendText(msg.to,"Protect QR Off")
                else:
                    wait["ProtectQR"] = False
                    if wait["lang"] == "JP":
                        ks.sendText(msg.to,"Protect QR Off")
                    else:
                        ks.sendText(msg.to,"Protect QR Off")

                if wait["Protectgroupname"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Gname Off")
                    else:
                        cl.sendText(msg.to,"Protect Gname OFF")
                else:
                    wait["Protectgroupname"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Gname Off")
                    else:
                        cl.sendText(msg.to,"Protect Gname Off")	

                if wait["Protectpicture"] == False:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Protect Image Off")
                    else:
                        ki.sendText(msg.to,"Protect Image OFF")
                else:
                    wait["Protectpicture"] = False
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Protect Image Off")
                    else:
                        ki.sendText(msg.to,"Protect Image Off")

                if wait["Protectmember"] == False:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Protect member Off")
                    else:
                        kk.sendText(msg.to,"Protect member Off")
                else:
                    wait["Protectmember"] = False
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Protect member Off")
                    else:
                        kk.sendText(msg.to,"Protect member Off")

                if wait["Protectadmin"] == False:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Protect admin Off")
                    else:
                        kc.sendText(msg.to,"Protect admin Off")
                else:
                    wait["Protectadmin"] = False
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Protect admin Off")
                    else:
                        kc.sendText(msg.to,"Protect admin Off")

                if wait["Protectcreator"] == False:
                    if wait["lang"] == "JP":
                        ks.sendText(msg.to,"Protect owner Off")
                    else:
                        ks.sendText(msg.to,"Protect owner Off")
                else:
                    wait["Protectcreator"] = False
                    if wait["lang"] == "JP":
                        ks.sendText(msg.to,"Protect owner Off")
                    else:
                        ks.sendText(msg.to,"Protect owner Off")							
#----------------------------------------------------------------------------
#---------------------------- INFO @ ----------------------------------------	
            elif "Info @" in msg.text:
                nama = msg.text.replace("Info @","")
                target = nama.rstrip(' ')
                tob = cl.getGroup(msg.to)
                for g in tob.members:
                    if target == g.displayName:
                        mid = cl.getContact(g.mid)
                        try:
                            cover = cl.channel.getCover(g.mid)
                        except:
                            cover = ""
                        cl.sendText(msg.to,"[Display Name]:\n" + mid.displayName + "\n[Mid]:\n" + tob.mid + "\n[BIO]:\n" + mid.statusMessage + "\n[Ava]:\nhttp://dl.profile.line-cdn.net/" + mid.pictureStatus + "\n[Cover]:\n" + str(cover))
                    else:
                        pass
#--------------------------------------------------------------------------------
#---------------------------- FUNGSI ON OFF -------------------------------------						
            elif msg.text in ["é€£çµ¡å�1�7�˄1�7:ã‚ªãƒ1�7","K on","Contact on","é¡¯ç¤ºï¼šé–�1�7�1�7"]:
				if msg.from_ in admin:
					if wait["contact"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["contact"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å�1�7�˄1�7:ã‚ªãƒ�1�7�1�7","K off","Contact off","é¡¯ç¤ºï¼šé—ń1�7"]:
				if msg.from_ in admin:
					if wait["contact"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done ")
					else:
						wait["contact"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["Join on","Auto join:on"]:
				if msg.from_ in admin:
					if wait["autoJoin"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"selesai")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"selesai")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["Join off","Auto join:off"]:
				if msg.from_ in admin:
					if wait["autoJoin"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"dimatikan")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"dimatikan")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["Join2 on","Auto join2:on"]:
				if msg.from_ in admin:
					if wait["autoJoin2"] == True:
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"selesai")
						else:
							ki.sendText(msg.to,"done")
					else:
						wait["autoJoin2"] = True
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"selesai")
						else:
							ki.sendText(msg.to,"done")
            elif msg.text in ["Join2 off","Auto join2:off"]:
				if msg.from_ in admin:
					if wait["autoJoin2"] == False:
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"dimatikan")
						else:
							ki.sendText(msg.to,"done")
					else:
						wait["autoJoin2"] = False
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"dimatikan")
						else:
							ki.sendText(msg.to,"done")
            elif msg.text in ["Join3 on","Auto join3:on"]:
				if msg.from_ in admin:
					if wait["autoJoin3"] == True:
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"selesai")
						else:
							kk.sendText(msg.to,"done")
					else:
						wait["autoJoin3"] = True
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"selesai")
						else:
							kk.sendText(msg.to,"done")
            elif msg.text in ["Join3 off","Auto join3:off"]:
				if msg.from_ in admin:
					if wait["autoJoin3"] == False:
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"dimatikan")
						else:
							kk.sendText(msg.to,"done")
					else:
						wait["autoJoin3"] = False
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"dimatikan")
						else:
							kk.sendText(msg.to,"done")
            elif msg.text in ["Join4 on","Auto join4:on"]:
				if msg.from_ in admin:
					if wait["autoJoin4"] == True:
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"selesai")
						else:
							kc.sendText(msg.to,"done")
					else:
						wait["autoJoin4"] = True
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"selesai")
						else:
							kc.sendText(msg.to,"done")
            elif msg.text in ["Join4 off","Auto join4:off"]:
				if msg.from_ in admin:
					if wait["autoJoin4"] == False:
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"dimatikan")
						else:
							kc.sendText(msg.to,"done")
					else:
						wait["autoJoin4"] = False
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"dimatikan")
						else:
							kc.sendText(msg.to,"done")
            elif msg.text in ["Join5 on","Auto join5:on"]:
				if msg.from_ in admin:
					if wait["autoJoin5"] == True:
						if wait["lang"] == "JP":
							ks.sendText(msg.to,"selesai")
						else:
							ks.sendText(msg.to,"done")
					else:
						wait["autoJoin5"] = True
						if wait["lang"] == "JP":
							ks.sendText(msg.to,"selesai")
						else:
							ks.sendText(msg.to,"done")
            elif msg.text in ["Join5 off","Auto join5:off"]:
				if msg.from_ in admin:
					if wait["autoJoin5"] == False:
						if wait["lang"] == "JP":
							ks.sendText(msg.to,"dimatikan")
						else:
							ks.sendText(msg.to,"done")
					else:
						wait["autoJoin5"] = False
						if wait["lang"] == "JP":
							ks.sendText(msg.to,"dimatikan")
						else:
							ks.sendText(msg.to,"done")
#---------------------------------------------------------------------------
#---------------------------- G CANCEL -------------------------------------
            elif msg.text in ["Gcancel:"]:
				if msg.from_ in admin:
					try:
						strnum = msg.text.replace("Gcancel:","")
						if strnum == "off":
							wait["autoCancel"]["on"] = False
							if wait["lang"] == "JP":
								cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
							else:
								cl.sendText(msg.to,"å…³äº�1�7�é�1�7�€è¯·æ‹�1�7�ç»ã€‚è¦æ�1�7�¶å¼€è¯·æŒ‡å®šäººæ�1�7�°å�1�7�é€")
						else:
							num =  int(strnum)
							wait["autoCancel"]["on"] = True
							if wait["lang"] == "JP":
								cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
							else:
								cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš�1�7�å°ç»�1�7�ç�1�7�¨è�1�7�ªåŠ¨é�1�7�€è¯·æ‹�1�7�ç»1�7")
					except:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Value is wrong")
						else:
							cl.sendText(msg.to,"Bizarre ratings")
#-----------------------------------------------------------------------------
#---------------------------- LEAVE ROOM -------------------------------------
            elif msg.text in ["å¼·åˆ¶è‡ªå�1�7��1�7�é€€å�1�7�1�7:ã‚ªãƒ1�7","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå�1�7��1�7�é€€å�1�7�ºï¼šé�1�7��1�7�1�7"]:
				if msg.from_ in admin:
					if wait["leaveRoom"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["leaveRoom"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å¼€ã€�1�7�1�7")
            elif msg.text in ["å¼·åˆ¶è‡ªå�1�7��1�7�é€€å�1�7�1�7:ã‚ªãƒ�1�7�1�7","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå�1�7��1�7�é€€å�1�7�ºï¼šé�1�7�ń1�7"]:
				if msg.from_ in admin:
					if wait["leaveRoom"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["leaveRoom"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"already")
							
            elif msg.text in ["Leave2 on"]:
				if msg.from_ in admin:
					if wait["leaveRoom2"] == True:
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"already on")
						else:
							ki.sendText(msg.to,"done")
					else:
						wait["leaveRoom2"] = True
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"done")
						else:
							ki.sendText(msg.to,"è¦äº†å¼€ã€�1�7�1�7")
            elif msg.text in ["Leave2 off"]:
				if msg.from_ in admin:
					if wait["leaveRoom2"] == False:
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"already off")
						else:
							ki.sendText(msg.to,"done")
					else:
						wait["leaveRoom2"] = False
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"done")
						else:
							ki.sendText(msg.to,"already")
							
            elif msg.text in ["Leave3 on"]:
				if msg.from_ in admin:
					if wait["leaveRoom3"] == True:
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"already on")
						else:
							kk.sendText(msg.to,"done")
					else:
						wait["leaveRoom3"] = True
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"done")
						else:
							kk.sendText(msg.to,"è¦äº†å¼€ã€�1�7�1�7")
            elif msg.text in ["Leave3 off"]:
				if msg.from_ in admin:
					if wait["leaveRoom3"] == False:
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"already off")
						else:
							kk.sendText(msg.to,"done")
					else:
						wait["leaveRoom3"] = False
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"done")
						else:
							kk.sendText(msg.to,"already")
							
            elif msg.text in ["Leave4 on"]:
				if msg.from_ in admin:
					if wait["leaveRoom4"] == True:
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"already on")
						else:
							kc.sendText(msg.to,"done")
					else:
						wait["leaveRoom4"] = True
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"done")
						else:
							kc.sendText(msg.to,"è¦äº†å¼€ã€�1�7�1�7")
            elif msg.text in ["Leave4 off"]:
				if msg.from_ in admin:
					if wait["leaveRoom4"] == False:
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"already off")
						else:
							kc.sendText(msg.to,"done")
					else:
						wait["leaveRoom4"] = False
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"done")
						else:
							kc.sendText(msg.to,"already")
							
            elif msg.text in ["Leave5 on"]:
				if msg.from_ in admin:
					if wait["leaveRoom5"] == True:
						if wait["lang"] == "JP":
							ks.sendText(msg.to,"already on")
						else:
							ks.sendText(msg.to,"done")
					else:
						wait["leaveRoom5"] = True
						if wait["lang"] == "JP":
							ks.sendText(msg.to,"done")
						else:
							ks.sendText(msg.to,"è¦äº†å¼€ã€�1�7�1�7")
            elif msg.text in ["Leave5 off"]:
				if msg.from_ in admin:
					if wait["leaveRoom5"] == False:
						if wait["lang"] == "JP":
							ks.sendText(msg.to,"already off")
						else:
							ks.sendText(msg.to,"done")
					else:
						wait["leaveRoom5"] = False
						if wait["lang"] == "JP":
							ks.sendText(msg.to,"done")
						else:
							ks.sendText(msg.to,"already")
#--------------------------------------------------------------------------------
#---------------------------- FUNGSI ON OFF -------------------------------------							
            elif msg.text in ["Share on","share on"]:
				if msg.from_ in admin:
					if wait["timeline"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["timeline"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å¼€ã€�1�7�1�7")
            elif msg.text in ["Share off","Share off"]:
				if msg.from_ in admin:
					if wait["timeline"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["timeline"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å�1�7�³æ�1�7�­ã€ 1�7")
#--------------------------------------------------------------------------------
#---------------------------- SETTINGS GROUP ------------------------------------
            elif msg.text in ["Set","Status","status"]:
				if msg.from_ in admin:
					md = "⭐S E T T I N G S⭐\n*============*\n"
					if wait["contact"] == True: md+="☞ Contact → ✔\n"
					else: md+="☞ Contact → ❌\n"
					if wait["autoJoin"] == True: md+="☞ Auto join → ✔\n"
					else: md +="☞ Auto join → ❌\n"
					if wait["autoJoin2"] == True: md+="☞ Auto join → ✔\n"
					else: md +="☞ Auto join → ❌\n"
					if wait["autoJoin3"] == True: md+="☞ Auto join → ✔\n"
					else: md +="☞ Auto join → ❌\n"
					if wait["autoJoin4"] == True: md+="☞ Auto join → ✔\n"
					else: md +="☞ Auto join → ❌\n"
					if wait["autoJoin5"] == True: md+="☞ Auto join → ✔\n"
					else: md +="☞ Auto join → ❌\n"
					if wait["autoCancel"]["on"] == True:md+="☞ Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
					else: md+= "☞ Group cancel → ❌\n"
					if wait["autoCancel2"]["on"] == True:md+="☞ Group cancel :" + str(wait["autoCancel2"]["members"]) + "\n"
					else: md+="☞ Group cancel → ❌\n"
					if wait["autoCancel3"]["on"] == True:md+="☞ Group cancel :" + str(wait["autoCancel3"]["members"]) + "\n"
					else: md+="☞ Group cancel → ❌\n"
					if wait["autoCancel4"]["on"] == True:md+="☞ Group cancel :" + str(wait["autoCancel4"]["members"]) + "\n"
					else: md+="☞ Group cancel → ❌\n"
					if wait["autoCancel5"]["on"] == True:md+="☞ Group cancel :" + str(wait["autoCancel5"]["members"]) + "\n"
					else: md+="☞ Group cancel → ❌\n"
					if wait["leaveRoom"] == True: md+="☞ Auto leave → ✔\n"
					else: md+="☞ Auto leave → ❌\n"
					if wait["leaveRoom2"] == True: md+="☞ Auto leave → ✔\n"
					else: md+="☞ Auto leave → ❌\n"
					if wait["leaveRoom3"] == True: md+="☞ Auto leave → ✔\n"
					else: md+="☞ Auto leave → ❌\n"
					if wait["leaveRoom4"] == True: md+="☞ Auto leave → ✔\n"
					else: md+="☞ Auto leave → ❌\n"
					if wait["leaveRoom5"] == True: md+="☞ Auto leave → ✔\n"
					else: md+="☞ Auto leave → ❌\n"
					if wait["timeline"] == True: md+="☞ Share → ✔\n"
					else:md+="☞ Share → ❌\n"
					if wait["likeOn"] == True: md+="☞ Auto like → ✔\n"
					else:md+="☞ Auto like → ❌\n"
					if wait["autoAdd"] == True: md+="☞ autoAdd → ✔\n"
					else:md+="☞ autoAdd → ❌\n"
					if wait["commentOn"] == True: md+="☞ Comment → ✔\n"
					else:md+="☞ Comment → ❌\n"
					if wait["MemberJoin"] == True: md+="☞ Member join → ✔\n"
					else:md+="☞ Member join → ❌\n"
					if wait["MemberLeft"] == True: md+="☞ Member left → ✔\n"
					else:md+="☞ Member left → ❌\n"
					if wait["ProtectGroup"] == True: md+="☞ Group → ✔\n*============*\n⭐Aogiri Cyber Line⭐\n*============*"
					else:md+="☞ Protect Group → ❌\n*============*\n⭐Aogiri Cyber Line⭐\n*============*"
					cl.sendText(msg.to,md)
					
            elif msg.text in ["Set proteksi","Set2","Status2","status2"]:
				if msg.from_ in admin:
					md = "⭐Status Proteksi⭐\n*============*\n"
					if wait["Protectpicture"] == True: md+="☞ Image → ✔\n"
					else: md+="☞ Image → ❌\n"                    
					if wait["Protectgroupname"] == True: md+="☞ Gname → ✔\n"
					else: md+="☞ Gname → ❌\n"
					if wait["Protectmember"] == True: md+="☞ Member → ✔\n"
					else: md +="☞ Member → ❌\n"
					if wait["Protectadmin"] == True: md+="☞ Admin → ✔\n"
					else: md +="☞ Admin → ❌\n"
					if wait["Protectcreator"] == True: md+="☞ Owner → ✔\n"
					else: md +="☞ Owner → ❌\n"
					#if wait["winvite"] == True: md+="☞ Invite → ✔\n"
					#else: md+="☞ Invite → ❌\n"
					if wait["Protectdisplayname"] == True: md+="☞ Tag → ✔\n"
					else: md+="☞ Tag → ❌\n"
					if wait["Protectbmo"] == True: md+="☞ Bmo in → ✔\n"
					else: md+="☞ Bmo in → ❌\n"
					if wait["Protectbmo2"] == True: md+="☞ Bmo out → ✔\n"
					else: md+="☞ Bmo out → ❌\n"
					if wait["ProtectQR"] == True: md+="☞ Link → ✔\n"
					else:md+="☞ Link → ❌\n"
					if wait["Protectcancel"] == True: md+="☞ Cancel → ✔\n"
					else:md+="☞ Cancel → ❌\n"
					if wait["atjointicket"] == True: md+="☞ Ajgbyt → ✔\n"
					else:md+="☞ Ajgbyt → ❌\n"
					if wait["Protectjoin"] == True: md+="☞Protectjoin → ✔\n"
					else:md+="☞ Protectjoin → ❌\n"
					if wait["Protectguest"] == True: md+="☞Guest → ✔\n"
					else:md+="☞ Guest → ❌\n"
					if wait["ProtectGroup"] == True: md+="☞ Group → ✔\n*============*\n⭐Aogiri Cyber Line⭐\n*============*"
					else:md+="☞ Group → ❌\n*============*\n⭐Aogiri Cyber Line⭐\n*============*"
					cl.sendText(msg.to,md)
#------------------------------------------------------------------------
#---------------------------- ALBUM -------------------------------------					
            elif "album merit " in msg.text:
				if msg.from_ in admin:
					gid = msg.text.replace("album merit ","")
					album = cl.getAlbum(gid)
					if album["result"]["items"] == []:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"There is no album")
						else:
							cl.sendText(msg.to,"ç›¸å�1�7�Œæ²¡åœ¨ã€ 1�7")
					else:
						if wait["lang"] == "JP":
							mg = "The following is the target album"
						else:
							mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš�1�7�ç�1�7�¸å�1�7�ń1�7"
						for y in album["result"]["items"]:
							if "photoCount" in y:
								mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
							else:
								mg += str(y["title"]) + ":0sheet\n"
						cl.sendText(msg.to,mg)
            elif "Set album:" in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Set album:","")
                    album = cl.getAlbum(gid)
                    if album["result"]["items"] == []:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Tidak ada album👈")
                        else:
                            cl.sendText(msg.to,"Dalam album tidak👈")
                    else:
                        if wait["lang"] == "JP":
                            mg = "Berikut ini adalah album dari target"
                        else:
                            mg = "Berikut ini adalah subjek dari album"
                        for y in album["result"]["items"]:
                            if "photoCount" in y:
                                mg += str(y["title"]) + ":" + str(y["photoCount"]) + "æžš\n"
                            else:
                                mg += str(y["title"]) + ":0 Pieces\n"
                        cl.sendText(msg.to,mg)

            elif "Hapus album " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Hapus album ","")
                    albums = cl.getAlbum(gid)["result"]["items"]
                    i = 0
                    if albums != []:
                        for album in albums:
                            cl.deleteAlbum(gid,album["gid"])
                            i += 1
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,str(i) + "Soal album telah dihapus")
                    else:
                        cl.sendText(msg.to,str(i) + "Hapus kesulitan album🛡")
                elif msg.text.lower() == 'group id':
                    gid = cl.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                    cl.sendText(msg.to,h)

            elif "Album deleted:" in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Album deleted:","")
                    albums = cl.getAlbum(gid)["result"]["items"]
                    i = 0
                    if albums != []:
                        for album in albums:
                            cl.deleteAlbum(gid,album["id"])
                            i += 1
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,str(i) + "Soal album telah dihapus👈")
                    else:                    
					    cl.sendText(msg.to,str(i) + "Hapus kesulitan album👈")
#---------------------------------------------------------------------------
#---------------------------- GROUP ID -------------------------------------
            elif msg.text in ["Group id"]:
				if msg.from_ in admin:
					gid = cl.getGroupIdsJoined()
					h = ""
					for i in gid:
						h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
					cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
				if msg.from_ in admin:
					gid = cl.getGroupIdsInvited()
					for i in gid:
						cl.rejectGroupInvitation(i)
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"All invitations have been refused")
					else:
						cl.sendText(msg.to,"æ‹�1�7�ç»äº�1�7�å�1�7�¨éƒ¨çš�1�7�é�1�7�€è¯·ã€�1�7�1�7")
#--------------------------------------------------------------------------------
#---------------------------- FUNGSI ON OFF -------------------------------------					
            elif msg.text in ["Like:on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["いいね:オフ","Like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")    

            elif msg.text in ["è‡ªå�1�7��1�7�è¿½åń1�7 :ã‚ªãƒ1�7","Add on","Auto add:on","è‡ªå�1�7��1�7�è¿½åń1�7 ï¼šé–�1�7�1�7"]:
				if msg.from_ in admin:
					if wait["autoAdd"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoAdd"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å¼€ã€�1�7�1�7")
            elif msg.text in ["è‡ªå�1�7��1�7�è¿½åń1�7 :ã‚ªãƒ�1�7�1�7","Add off","Auto add:off","è‡ªå�1�7��1�7�è¿½åń1�7 ï¼šé—ń1�7"]:
				if msg.from_ in admin:
					if wait["autoAdd"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoAdd"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å�1�7�³æ�1�7�­ã€ 1�7")
            elif "Message change: " in msg.text:
				if msg.from_ in admin:
					wait["message"] = msg.text.replace("Message change: ","")
					cl.sendText(msg.to,"we changed the message👈")
            elif "Message add: " in msg.text:
				if msg.from_ in admin:
					wait["message"] = msg.text.replace("Message add: ","")
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"kami mengubah pesan👈")
					else:
						cl.sendText(msg.to,"change information")
            elif msg.text in ["Message","Mesagge add cek","Message Confirmation"]:
				if msg.from_ in admin:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"Additional information is automatically set to the following  \n\n" + wait["message"])
					else:
						cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut  \n\n" + wait["message"])
            elif msg.text in ["Change","change"]:
                if msg.from_ in admin:
                    if wait["lang"] =="JP":
                        wait["lang"] = "TW"
                        cl.sendText(msg.to,"I changed the language to engglis👈")
                    else:
                        wait["lang"] = "JP"
                        cl.sendText(msg.to,"I changed the language to indonesia👈")
            elif "Message set" in msg.text:
				if msg.from_ in admin:
					c = msg.text.replace("Message set","")
					if c in [""," ","\n",None]:
						cl.sendText(msg.to,"Is a string that can not be changed👈")
					else:
						wait["comment"] = c
						cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
				if msg.from_ in admin:
					c = msg.text.replace("Add comment:","")
					if c in [""," ","\n",None]:
						cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
					else:
						wait["comment"] = c
						cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒ˄1�7:ã‚ªãƒ1�7","Comment on","Comment:on","è‡ªå�1�7��1�7�é¦�1�7�Ä1�7 ç•™è¨€ï¼šé�1�7��1�7�1�7"]:
				if msg.from_ in admin:
					if wait["commentOn"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"already on")
					else:
						wait["commentOn"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å¼€ã€�1�7�1�7")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒ˄1�7:ã‚ªãƒ�1�7�1�7","Comment on","Comment off","è‡ªå�1�7��1�7�é¦�1�7�Ä1�7 ç•™è¨€ï¼šé�1�7�ń1�7"]:
				if msg.from_ in admin:
					if wait["commentOn"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"It is already turned off")
					else:
						wait["commentOn"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Off👈")
						else:
							cl.sendText(msg.to,"To turn off")
            elif msg.text in ["Comment"]:
				if msg.from_ in admin:
					cl.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:👈\n\n" + str(wait["comment"]))
#----------------------------------------------------------------------------
#---------------------------- GROUP URL -------------------------------------
            elif msg.text in ["Gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							cl.updateGroup(x)
						gurl = cl.reissueGroupTicket(msg.to)
						cl.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["aramel1 gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							ki.updateGroup(x)
						gurl = ki.reissueGroupTicket(msg.to)
						ki.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["aramel2 gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							kk.updateGroup(x)
						gurl = kk.reissueGroupTicket(msg.to)
						kk.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["aramel3 gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							kc.updateGroup(x)
						gurl = kc.reissueGroupTicket(msg.to)
						kc.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
#------------------------------------------------------------------------
#---------------------------- BL WL -------------------------------------
            elif msg.text in ["Comment bl "]:
				if msg.from_ in admin:
					wait["wblack"] = True
					cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
				if msg.from_ in admin:
					wait["dblack"] = True
					cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
				if msg.from_ in admin:
					if wait["commentBlack"] == {}:
						cl.sendText(msg.to,"confirmed")
					else:
						cl.sendText(msg.to,"Blacklist")
						mc = ""
						for mi_d in wait["commentBlack"]:
							mc += "" +cl.getContact(mi_d).displayName + "\n"
						cl.sendText(msg.to,mc)
#----------------------------------------------------------------						
#--------------------FUNGSI JAM START----------------------------						
            elif msg.text in ["Jam on"]:
				if msg.from_ in admin:
					if wait["clock"] == True:
						cl.sendText(msg.to,"jam di hidupkan")
					else:
						wait["clock"] = True
						now2 = datetime.now()
						nowT = datetime.strftime(now2,"(%H:%M)")
						profile = cl.getProfile()
						profile.displayName = wait["cName"] + nowT
						cl.updateProfile(profile)
						cl.sendText(msg.to,"done")
            elif msg.text in ["Jam off"]:
				if msg.from_ in admin:
					if wait["clock"] == False:
						cl.sendText(msg.to,"jam dimatikan")
					else:
						wait["clock"] = False
						cl.sendText(msg.to,"selesai")
            elif msg.text in ["Change clock "]:
				if msg.from_ in admin:
					n = msg.text.replace("Change clock ","")
					if len(n.decode("utf-8")) > 13:
						cl.sendText(msg.to,"changed")
					else:
						wait["cName"] = n
						cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["Up"]:
				if msg.from_ in admin:
					if wait["clock"] == True:
						now2 = datetime.now()
						nowT = datetime.strftime(now2,"(%H:%M)")
						profile = cl.getProfile()
						profile.displayName = wait["cName"] + nowT
						cl.updateProfile(profile)
						cl.sendText(msg.to,"Updated")
					else:
						cl.sendText(msg.to,"Please turn on the name clock")
#------------------------------------------------------------------------
#---------------------------- SIDER -------------------------------------

            elif msg.text == "Check":
              if msg.from_ in admin:
                cl.sendText(msg.to, "Cek sider")
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
                  pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                wait2['ROM'][msg.to] = {}
                #print wait2
				
            elif msg.text == "Nyimak":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "•Sider In Group•%s\n\n====duduL bot====\n\nsider yang telah membaca\n%sikut chat masuk surga *\n\nstatus terbaca dan di simak pada:\n[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Ketik ♪ Check ♪ terlebih dahulu  untuk mengaktifkan")
				
            elif msg.text == "Lurking":
                if msg.toType == 2:
                    ki.sendText(msg.to, "Set reading point:" + datetime.now().strftime('\n%Y/%m/%d %H:%M:%S'))
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print wait2
                        
            elif msg.text == "Result":
                if msg.toType == 2:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        ki.sendText(msg.to, "==============================\nActive readers:%s\n\n\n\nPassive readers:\n%s\n\n==============================\nIn the last seen point:\n[%s]\n==============================\n [☸]➦Powered By: AcL々•┅─────" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        print "ReadPoint Set..."
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print wait
                        ki.sendText(msg.to, "Auto set reading point in:" + datetime.now().strftime('\n%Y-%m-%d %H:%M:%S'))
                    else:
                        ki.sendText(msg.to, "Reading point has not been set.")
#--------------------------------------------------------------------------------
#---------------------------- TAG ALL MEMBER ------------------------------------						
            elif "Mention" in msg.text:
              if msg.from_ in admin:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg) 
						
            elif msg.text in ["Tagall","aramel @","duduL @"]:
              if msg.from_ in admin:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(5)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(6)
                    akh = akh + 1
                    cb2 += "@nrik\n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    ki.sendMessage(msg)
                except Exception as error:
                    print error
#----------------------------------------------------------------------------
#---------------------------- BOT MASUK -------------------------------------
            elif msg.text in ["Masuk","Jarvis","aramel in","mlebu"]:
				if msg.from_ in admin:
							G = cl.getGroup(msg.to)
							ginfo = cl.getGroup(msg.to)
							G.preventJoinByTicket = False
							cl.updateGroup(G)
							invsend = 0
							Ticket = cl.reissueGroupTicket(msg.to)
							ki.acceptGroupInvitationByTicket(msg.to,Ticket)
							kk.acceptGroupInvitationByTicket(msg.to,Ticket)
							kc.acceptGroupInvitationByTicket(msg.to,Ticket)
							ks.acceptGroupInvitationByTicket(msg.to,Ticket)
							G = cl.getGroup(msg.to)
							G.preventJoinByTicket = True
							ki.updateGroup(G)
							print "kicker ok" 
							G.preventJoinByTicket(G)
							ki.updateGroup(G)
							
            elif msg.text in ["aramel2 in"]:
				if msg.from_ in admin:
							G = ki.getGroup(msg.to)
							ginfo = ki.getGroup(msg.to)
							G.preventJoinByTicket = False
							ki.updateGroup(G)
							invsend = 0
							Ticket = ki.reissueGroupTicket(msg.to)
							kk.acceptGroupInvitationByTicket(msg.to,Ticket)
							kc.acceptGroupInvitationByTicket(msg.to,Ticket)
							ks.acceptGroupInvitationByTicket(msg.to,Ticket)
							cl.acceptGroupInvitationByTicket(msg.to,Ticket)
							G = ki.getGroup(msg.to)
							G.preventJoinByTicket = True
							kk.updateGroup(G)
							print "kicker ok" 
							G.preventJoinByTicket(G)
							kk.updateGroup(G)
							
            elif msg.text in ["aramel3 in"]:
				if msg.from_ in admin:
							G = kk.getGroup(msg.to)
							ginfo = kk.getGroup(msg.to)
							G.preventJoinByTicket = False
							kk.updateGroup(G)
							invsend = 0
							Ticket = kk.reissueGroupTicket(msg.to)
							kc.acceptGroupInvitationByTicket(msg.to,Ticket)
							ks.acceptGroupInvitationByTicket(msg.to,Ticket)
							cl.acceptGroupInvitationByTicket(msg.to,Ticket)
							ki.acceptGroupInvitationByTicket(msg.to,Ticket)
							G = kk.getGroup(msg.to)
							G.preventJoinByTicket = True
							kc.updateGroup(G)
							print "kicker ok" 
							G.preventJoinByTicket(G)
							kc.updateGroup(G)
							
            elif msg.text in ["aramel4 in"]:
				if msg.from_ in admin:
							G = kc.getGroup(msg.to)
							ginfo = kc.getGroup(msg.to)
							G.preventJoinByTicket = False
							kc.updateGroup(G)
							invsend = 0
							ks.acceptGroupInvitationByTicket(msg.to,Ticket)
							Ticket = kc.reissueGroupTicket(msg.to)
							cl.acceptGroupInvitationByTicket(msg.to,Ticket)
							ki.acceptGroupInvitationByTicket(msg.to,Ticket)
							kk.acceptGroupInvitationByTicket(msg.to,Ticket)
							G = kc.getGroup(msg.to)
							G.preventJoinByTicket = True
							ks.updateGroup(G)
							print "kicker ok" 
							G.preventJoinByTicket(G)
							ks.updateGroup(G)
							
            elif msg.text in ["aramel5 in"]:
				if msg.from_ in admin:
							G = ks.getGroup(msg.to)
							ginfo = ks.getGroup(msg.to)
							G.preventJoinByTicket = False
							ks.updateGroup(G)
							invsend = 0
							cl.acceptGroupInvitationByTicket(msg.to,Ticket)
							Ticket = kc.reissueGroupTicket(msg.to)
							ki.acceptGroupInvitationByTicket(msg.to,Ticket)
							kk.acceptGroupInvitationByTicket(msg.to,Ticket)
							kc.acceptGroupInvitationByTicket(msg.to,Ticket)
							G = ks.getGroup(msg.to)
							G.preventJoinByTicket = True
							cl.updateGroup(G)
							print "kicker ok" 
							G.preventJoinByTicket(G)
							cl.updateGroup(G)

            elif msg.text in ["aramel join"]:
                if msg.form_ in admin:
                  X = ki.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  ki.updateGroup(X)
                  invsend = 0
                  Ti = ki.reissueGroupTicket(msg.to)
                  cl.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["aramel1 join"]:
                if msg.from_ in admin:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)

            elif msg.text in ["aramel2 join"]:
                if msg.from_ in admin:
                  x =cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["aramel3 join"]:
                if msg.from_ in admin:
                  x =cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
				  
            elif msg.text in ["aramel4 join"]:
                if msg.from_ in admin:
                  x =cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ks.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
#-----------------------------------------------------------------------------
#---------------------------- BOT KELUAR -------------------------------------
            elif msg.text in ["Out","out","muleh","aramel left","left"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							ki.sendText(msg.to,"papay  ⇨ "  +  str(ginfo.name)  + "")
							kk.sendText(msg.to,"papay  ⇨ "  +  str(ginfo.name)  + "")
							kc.sendText(msg.to,"papay  ⇨ "  +  str(ginfo.name)  + "")
							ks.sendText(msg.to,"papay  ⇨ "  +  str(ginfo.name)  + "")
							ki.leaveGroup(msg.to)
							kk.leaveGroup(msg.to)
							kc.leaveGroup(msg.to)
							ks.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["left all"]: # Semua Ninggalin Group Termasuk Selfbotnya :D
                if msg.from_ in admin:
                    if msg.toType == 2:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            ki.sendText(msg.to,"papay  ⇨ "  +  str(ginfo.name)  + "")
                            kk.sendText(msg.to,"papay  ⇨ "  +  str(ginfo.name)  + "")
                            kc.sendText(msg.to,"papay  ⇨ "  +  str(ginfo.name)  + "")
                            ks.sendText(msg.to,"papay  ⇨ "  +  str(ginfo.name)  + "")
                            cl.sendText(msg.to,"papay  ⇨ "  +  str(ginfo.name)  + "")
                            ki.leaveGroup(msg.to)
                            kk.leaveGroup(msg.to)
                            kc.leaveGroup(msg.to)
                            ks.leaveGroup(msg.to)
                            cl.leaveGroup(msg.to)
                        except:
                            pass
            elif msg.text in ["Bye aramel"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							cl.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["Bye aramel1"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							ki.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["Bye aramel2"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							kk.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["Bye aramel3"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							kc.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["Bye aramel4"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							ks.leaveGroup(msg.to)
						except:
							pass							
#---------------------------------------------------------------------------
#---------------------------- BOT LIKE -------------------------------------
            elif msg.text in ["Bot Like", "Bot like"]: #Semua Bot Ngelike Status Akun Utama
                if msg.from_ in admin:
                    print "[Command]Like executed"
                    cl.sendText(msg.to,"Like Status Admin")
                    try:
                        likePost()
                    except:
                        pass
                
            elif msg.text in ["Like temen", "Bot like temen"]: #Semua Bot Ngelike Status Teman
                if msg.from_ in admin:
                    print "[Command]Like executed"
                    cl.sendText(msg.to,"Like Status Teman")
                    try:
                        autolike()
                    except:
                        pass
#--------------------------------------------------------------------------
#---------------------------- KICK BL -------------------------------------
            elif msg.text in ["Kill"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = ki.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						if matched_list == []:
							kk.sendText(msg.to,"Sayonara")
							kc.sendText(msg.to,"Sayonara")
							return
						for jj in matched_list:
							try:
								klist=[ki,kk,kc]
								kicker=random.choice(klist)
								kicker.kickoutFromGroup(msg.to,[jj])
								print (msg.to,[jj])
							except:
								print
#-----------------------------------------------------------------------------
#---------------------------- LIST GROUP -------------------------------------
            elif msg.text in ["Glist"]:
                if msg.from_ in creator:
                        gid = cl.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            h += "[•]%s Member\n" % (cl.getGroup(i).name   +"👉"+str(len(cl.getGroup(i).members)))
                        cl.sendText(msg.to, "=======[List Group]======\n"+ h +"Total Group : " +"[ "+str(len(gid))+" ]")
			
            elif msg.text in ["GL Id"]: #Melihat ID Group Yang Di Join untuk Invite Owner ke Group yang di join BOT(Untuk Selfbot ini ga kepake)
              if msg.from_ in creator:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
#--------------------------------------------------------------------------------
#---------------------------- BOT LEFT ALL ROM ----------------------------------
            elif msg.text in ["Bot out","Op bye"]: # Keluar Dari Semua Group Yang Di dalem nya  ada bot(Kalo Bot Kalian Nyangkut di Group lain :D)
                if msg.from_ in creator:
                    gid = cl.getGroupIdsJoined()
                    gid = ki.getGroupIdsJoined()
                    gid = kk.getGroupIdsJoined()
                    gid = kc.getGroupIdsJoined()
                    gid = ks.getGroupIdsJoined()
                    for i in gid:
                        kc.leaveGroup(i)
                        ki.leaveGroup(i)
                        kk.leaveGroup(i)
                        ks.leaveGroup(i)
                        cl.leaveGroup(i)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"papay  ⇨ "  +  str(ginfo.name)  + "")
                        ki.sendText(msg.to,"papay  ⇨ "  +  str(ginfo.name)  + "")
                        kk.sendText(msg.to,"papay  ⇨ "  +  str(ginfo.name)  + "")
                        kc.sendText(msg.to,"papay  ⇨ "  +  str(ginfo.name)  + "")
                        ks.sendText(msg.to,"papay  ⇨ "  +  str(ginfo.name)  + "")

                    else:
                        cl.sendText(msg.to,"He declined all invitations")
#------------------------------------------------------------------------------
#---------------------------- RATAIN ROOM -------------------------------------
            elif "Cleanse" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "ok"
						_name = msg.text.replace("Cleanse","")
						gs = cl.getGroup(msg.to)
						gs = ki.getGroup(msg.to)
						gs = kk.getGroup(msg.to)
						gs = kc.getGroup(msg.to)
						gs = ks.getGroup(msg.to)
						cl.sendText(msg.to,"Perintah DiLaksanakan ô")
						ki.sendText(msg.to,"Group DiBersihkan.")
						targets = []
						for g in gs.members:
							if _name in g.displayName:
								targets.append(g.mid)
						if targets == []:
							cl.sendText(msg.to,"Not found.")
							ki.sendText(msg.to,"Not found.")
						else:
							for target in targets:
								try:
									klist=[cl,ki,kk,kc,ks]
									kicker=random.choice(klist)
									kicker.kickoutFromGroup(msg.to,[target])
									print (msg.to,[g.mid])
								except:
									ki.sendText(msg.to,"Group cleanse")
									kk.sendText(msg.to,"Group cleanse")
#-------------------------------------------------------------------------------
#---------------------------- KICK VIA TAG -------------------------------------									
            elif "aramel Nk " in msg.text:
				if msg.from_ in admin:
						nk0 = msg.text.replace("Nk ","")
						nk1 = nk0.lstrip()
						nk2 = nk1.replace("@","")
						nk3 = nk2.rstrip()
						_name = nk3
						gs = cl.getGroup(msg.to)
						targets = []
						for s in gs.members:
							if _name in s.displayName:
								targets.append(s.mid)
						if targets == []:
							sendMessage(msg.to,"user does not exist")
							pass
						else:
							for target in targets:
									try:
										klist=[cl,ki,kk,kc,ks]
										kicker=random.choice(klist)
										kicker.kickoutFromGroup(msg.to,[target])
										print (msg.to,[g.mid])
									except:
										ki.sendText(msg.to,"Bye...")
										kk.sendText(msg.to,"Sayonara")
									
            elif "Nk " in msg.text:
              if msg.from_ in admin:
                nk0 = msg.text.replace("Nk ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("@","")
                nk3 = nk2.rstrip()
                _name = nk3
                gs = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                gs.preventJoinByTicket = False
                cl.updateGroup(gs)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                satpam.acceptGroupInvitationByTicket(msg.to,Ticket)
                targets = []
                for s in gs.members:
                    if _name in s.displayName:
                       targets.append(s.mid)
                if targets == []:
                   sendMessage(msg.to,"user does not exist")
                   pass
                else:
                   for target in targets:
                      try:
                        satpam.kickoutFromGroup(msg.to,[target])
                        print (msg.to,[g.mid])
                      except:
                        satpam.leaveGroup(msg.to)
                        gs = cl.getGroup(msg.to)
                        gs.preventJoinByTicket = True
                        cl.updateGroup(gs)
                        gs.preventJoinByTicket(gs)
                        cl.updateGroup(gs)
#--------------------------------------------------------------------------------
#---------------------------- BL ALL IN ROOM ------------------------------------									
            elif "Banned:" in msg.text:                  
                       nk0 = msg.text.replace("Banned:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Locked")
                                except:
                                    kk.sendText(msg.to,"Error")
#--------------------------------------------------------------------------------
#---------------------------- WL ALL IN ROOM ------------------------------------
            elif "Unbanned:" in msg.text:                  
                       nk0 = msg.text.replace("Unbanned:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Unlocked")
                                except:
                                    kk.sendText(msg.to,"Error")
#----------------------------------------------------------------------------
#---------------------------- BL MEMBER -------------------------------------										
            elif "Blacklist @ " in msg.text:
				if msg.from_ in admin:
					_name = msg.text.replace("Blacklist @ ","")
					_kicktarget = _name.rstrip(' ')
					gs = random.choice(KAC).getGroup(msg.to)
					targets = []
					for g in gs.members:
						if _kicktarget == g.displayName:
							targets.append(g.mid)
							if targets == []:
								cl.sendText(msg.to,"Not found")
							else:
								for target in targets:
									try:
										wait["blacklist"][target] = True
										f=codecs.open('st2__b.json','w','utf-8')
										json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
										random.choice(KAC).sendText(msg.to,"Succes")
									except:
										ki.sendText(msg.to,"error")
#-----------------------------------------------------------------------------
#---------------------------- BL VIA TAG -------------------------------------
            elif "Ban @" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "[Ban]ok"
						_name = msg.text.replace("Ban @","")
						_nametarget = _name.rstrip('  ')
						gs = cl.getGroup(msg.to)
						gs = ki.getGroup(msg.to)
						gs = kk.getGroup(msg.to)
						gs = kc.getGroup(msg.to)
						gs = ks.getGroup(msg.to)
						targets = []
						for g in gs.members:
							if _nametarget == g.displayName:
								targets.append(g.mid)
						if targets == []:
						    cl.sendText(msg.to,"Dilarang Banned Bot")
						else:
							for target in targets:
								try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									random.choice(KAC).sendText(msg.to,"Akun telah sukses di banned")
								except:
									random.choice(KAC).sendText(msg.to,"error")
#-----------------------------------------------------------------------------
#---------------------------- WL VIA TAG -------------------------------------
            elif "Unban @" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "[Unban]ok"
						_name = msg.text.replace("Unban @","")
						_nametarget = _name.rstrip('  ')
						gs = cl.getGroup(msg.to)
						gs = ki.getGroup(msg.to)
						gs = kk.getGroup(msg.to)
						gs = kc.getGroup(msg.to)
						gs = kc.getGroup(msg.to)
						targets = []
						for g in gs.members:
							if _nametarget == g.displayName:
								targets.append(g.mid)
						if targets == []:
							cl.sendText(msg.to,"Tidak DiTemukan")
							ki.sendText(msg.to,"Tidak DiTemukan")
							kk.sendText(msg.to,"Tidak DiTemukan")
							kc.sendText(msg.to,"Tidak DiTemukan")
							ks.sendText(msg.to,"Tidak DiTemukan")
						else:
							for target in targets:
								try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"succes unlocked target")
								except:
									ki.sendText(msg.to,"error")
#--------------------------------------------------------------------------------
#---------------------------- CLONE CONTACT -------------------------------------						
            elif "Clone " in msg.text:
                if msg.from_ in admin:
                 targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        contact = cl.getContact(target)
                        X = contact.displayName
                        profile = cl.getProfile()
                        profile.displayName = X
                        cl.updateProfile(profile)
                        cl.sendText(msg.to, "success clone target")
                        #---------------------------------------
                        Y = contact.statusMessage
                        lol = cl.getProfile()
                        lol.statusMessage = Y
                        cl.updateProfile(lol)
                        #---------------------------------------
                        P = contact.pictureStatus
                        cl.updateDisplayPicture(P)
                    except Exception as e:
                        cl.sendText(msg.to, "failed")
                        print e
						
            elif "aramel2 clone " in msg.text:
                if msg.from_ in admin:
                 targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        contact = ki.getContact(target)
                        X = contact.displayName
                        profile = ki.getProfile()
                        profile.displayName = X
                        ki.updateProfile(profile)
                        ki.sendText(msg.to, "Success clone target")
                        #---------------------------------------
                        Y = contact.statusMessage
                        lol = ki.getProfile()
                        lol.statusMessage = Y
                        ki.updateProfile(lol)
                        #---------------------------------------
                        P = contact.pictureStatus
                        ki.updateDisplayPicture(P)
                    except Exception as e:
                        ki.sendText(msg.to, "failed")
                        print e
						
            elif "aramel3 clone " in msg.text:
                if msg.from_ in admin:
                 targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        contact = kk.getContact(target)
                        X = contact.displayName
                        profile = kk.getProfile()
                        profile.displayName = X
                        kk.updateProfile(profile)
                        kk.sendText(msg.to, "Success clone target")
                        #---------------------------------------
                        Y = contact.statusMessage
                        lol = kk.getProfile()
                        lol.statusMessage = Y
                        kk.updateProfile(lol)
                        #---------------------------------------
                        P = contact.pictureStatus
                        kk.updateDisplayPicture(P)
                    except Exception as e:
                        kk.sendText(msg.to, "failed")
                        print e
						
            elif "aramel4 clone " in msg.text:
                if msg.from_ in admin:
                 targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        contact = kc.getContact(target)
                        X = contact.displayName
                        profile = kc.getProfile()
                        profile.displayName = X
                        kc.updateProfile(profile)
                        kc.sendText(msg.to, "Success clone target")
                        #---------------------------------------
                        Y = contact.statusMessage
                        lol = kc.getProfile()
                        lol.statusMessage = Y
                        kc.updateProfile(lol)
                        #---------------------------------------
                        P = contact.pictureStatus
                        kc.updateDisplayPicture(P)
                    except Exception as e:
                        kc.sendText(msg.to, "failed")
                        print e
						
            elif "aramel5 clone " in msg.text:
                if msg.from_ in admin:
                 targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        contact = ks.getContact(target)
                        X = contact.displayName
                        profile = ks.getProfile()
                        profile.displayName = X
                        ks.updateProfile(profile)
                        ks.sendText(msg.to, "Success clone target")
                        #---------------------------------------
                        Y = contact.statusMessage
                        lol = ks.getProfile()
                        lol.statusMessage = Y
                        ks.updateProfile(lol)
                        #---------------------------------------
                        P = contact.pictureStatus
                        ks.updateDisplayPicture(P)
                    except Exception as e:
                        ks.sendText(msg.to, "failed")
                        print e
#--------------------------------------------------------------------------------
#---------------------------- CEK MID VIA TAG -----------------------------------							
            elif ("Cek " in msg.text):
                if msg.from_ in admin:
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)
#--------------------------------------------------------------------------------
#---------------------------- KICK SATU LEBIH -----------------------------------
            elif "Vk " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif "aramel2 Vk " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      ki.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif "aramel3 Vk " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      kk.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif "aramel4 Vk " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      kc.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif "aramel5 Vk " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      ks.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
#-----------------------------------------------------------------------------
#---------------------------- JAWAB CHAT -------------------------------------
            elif msg.text in ["Test"]:
				if msg.from_ in admin:
					cl.sendText(msg.to,"ada duL ")
#--------------------------------------------------------------------------------
#---------------------------- MENGIKUTI KATA ADMIN ------------------------------
            elif "duduL say " in msg.text:
                if msg.from_ in admin:
					bctxt = msg.text.replace("duduL say ","")
					ki.sendText(msg.to,(bctxt))
#--------------------------------------------------------------------------------
#---------------------------- KIRIM CONTACT CREATOR -----------------------------
            elif msg.text in ["Creator"]:
					msg.contentType = 13
					msg.contentMetadata = {'mid': "u31b521fe93c9530357936576ba4a8f3d"}
					cl.sendMessage(msg)
#-----------------------------------------------------------------------
#---------------------------- FUNGSI SPAM ------------------------------
            elif "Spam: " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam: "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                # ☆⇨ Aogiri Cyber Line ⇦☆
                if txt[1] == "on":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Kelebihan batas:v")
                elif txt[1] == "off":
                    if jmlh <= 100000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Kelebihan batas:v")

            elif "hai @" in msg.text:
                _name = msg.text.replace("Hay @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       kk.sendText(g.mid,"Your Account Has Been Spammed !")  
                       kc.sendText(g.mid,"Your Account Has Been Spammed !")  
                       ks.sendText(g.mid,"Your Account Has Been Spammed !")
                       cl.sendText(msg.to, "Done")
                       print " Spammed !"

            elif "hallo " in msg.text:
                midd = msg.text.replace("Hallo ","")
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       ki.sendText(g.mid,[miid] + "Your Account Has Been Spammed !")
                       kk.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")  
                       kc.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")  
                       ks.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")
                       cl.sendText(msg.to, "Done")
                       print " Spammed !"
#----------------------------------------------------------------------------
#--------------------------------- DUGEM ------------------------------------
            elif "kedapkedip " in msg.text.lower():
              if msg.from_ in admin:
                txt = msg.text.replace("kedapkedip ", "")
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"
#--------------------------------------------------------------------------------
#---------------------------- REMOVE CHAT LINE BOT ------------------------------				   
            elif "Remove Chat" in msg.text:
                if msg.from_ in admin:
                   try:
                      cl.removeAllMessages(op.param2)
                      ki.removeAllMessages(op.param2)
                      kk.removeAllMessages(op.param2)
                      kc.removeAllMessages(op.param2)
                      ks.removeAllMessages(op.param2)
                      cl.sendText(msg.to,"Chat Telah Dibersihkan.")
                      print "Succes Remove Chat"
                   except:
                     pass
#--------------------------------------------------------------------------------
#---------------------------- UPDATE PROFIL STATUS ------------------------------
            elif "Cstatus:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                else:
                    cl.sendText(msg.to,"Done")
            elif "Cstatus2:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus2:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                else:
                    ki.sendText(msg.to,"Done")
            elif "Cstatus3:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus3:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
                else:
                    kk.sendText(msg.to,"Done")
            elif "Cstatus4:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus4:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = kc.getProfile()
                    profile.statusMessage = string
                    kc.updateProfile(profile)
                else:
                    kc.sendText(msg.to,"Done")
            elif "Cstatus5:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus5:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ks.getProfile()
                    profile.statusMessage = string
                    ks.updateProfile(profile)
                else:
                    ks.sendText(msg.to,"Done")
            elif "Cstatus6:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus6:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = satpam.getProfile()
                    profile.statusMessage = string
                    satpam.updateProfile(profile)
                    print "done update status"
#-------------------------------------------------------------------------
#---------------------------- UBAH NAMA BOT ------------------------------
            elif "Cname:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cname:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
            elif "Cname2:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cname2:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
            elif "Cname3:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cname3:","")
                if len(string.decode('utf-8')) <= 500:
                    profile =kk.getProfile()
                    profile.displayName = string
                    kk.updateProfile(profile)
            elif "Cname4:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cname4:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = kc.getProfile()
                    profile.displayName = string
                    kc.updateProfile(profile)
            elif "Cname5:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cname5:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ks.getProfile()
                    profile.displayName = string
                    ks.updateProfile(profile)
            #elif "Cname6:" in msg.text:
              #if msg.from_ in admin:
                #string = msg.text.replace("Cname6:","")
                #if len(string.decode('utf-8')) <= 500:
                    #profile = satpam.getProfile()
                    #profile.displayName = string
                    #satpam.updateProfile(profile)
#----------------------------------------------------------------------
#---------------------------- MENANYAKAN ------------------------------
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
            elif "Rate" in msg.text:
                tanya = msg.text.replace("Rate","")
                jawab = ("10%","20%","30%","40%","50%","60%","70%","80%","90%","100%")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
#----------------------------------------------------------------------------			
#---------------------------------- SONG ------------------------------------
            elif ".lirik " in msg.text.lower():
                songname = msg.text.replace("/lirik ","")
                params = {"songname":songname}
                r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                data = r.text
                data = json.loads(data)
                for song in data:
                    cl.sendText(msg.to,song[5])
                    print "[Command] Lirik"

            elif ".music " in msg.text.lower():
                songname = msg.text.replace("/lagu ","")
                params = {"songname":songname}
                r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                data = r.text
                data = json.loads(data)
                for song in data:
                    cl.sendText(msg.to,"Judul : " + song[0] + "\nDurasi : " + song[1])
                    cl.sendAudioWithURL(msg.to,song[3])
                    print "[Command] Lagu"
#--------------------------------------------------------------------------------
#---------------------------- INVITE CREATOR GROUP ------------------------------
            elif msg.text in ["Gcreator:inv"]:
	           if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       cl.findAndAddContactsByMid(gCreator)
                       cl.inviteIntoGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass
#-----------------------------------------------------------------
#---------------------------- STALK ------------------------------
            elif "Stalk " in msg.text:
                 print "[Command]Stalk executing"
                 stalkID = msg.text.replace("Stalk ","")
                 subprocess.call(["instaLooter",stalkID,"tmp/","-n","1"])   
                 files = glob.glob("tmp/*.jpg")
                 for file in files:
                     os.rename(file,"tmp/tmp.jpg")
                 fileTmp = glob.glob("tmp/tmp.jpg")
                 if not fileTmp:
                     cl.sendText(msg.to, "Image not found, maybe the account haven't post a single picture or the account is private")
                     print "[Command]Stalk,executed - no image found"
                 else:
                     image = upload_tempimage(client)
                     cl.sendText(msg.to, format(image['link']))
                     subprocess.call(["sudo","rm","-rf","tmp/tmp.jpg"])
                     print "[Command]Stalk executed - succes"
#--------------------------------------------------------------------------------
#---------------------------- KEMBALI KE PROFIL SBLM CLONE ----------------------          
            elif msg.text in ["backup"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "backup done")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
                    
            elif msg.text in ["backup2"]:
                try:
                    ki.updateDisplayPicture(backup.pictureStatus)
                    ki.updateProfile(backup)
                    ki.sendText(msg.to, "backup done")
                except Exception as e:
                    ki.sendText(msg.to, str (e))
					
            elif msg.text in ["backup3"]:
                try:
                    kk.updateDisplayPicture(backup3.pictureStatus)
                    kk.updateProfile(backup3)
                    kk.sendText(msg.to, "backup done")
                except Exception as e:
                    kk.sendText(msg.to, str (e))
                    
            elif msg.text in ["backup4"]:
                try:
                    kc.updateDisplayPicture(backup4.pictureStatus)
                    kc.updateProfile(backup4)
                    kc.sendText(msg.to, "backup done")
                except Exception as e:
                    kc.sendText(msg.to, str (e))
					
            elif msg.text in ["backup5"]:
                try:
                    ks.updateDisplayPicture(backup5.pictureStatus)
                    ks.updateProfile(backup5)
                    ks.sendText(msg.to, "backup done")
                except Exception as e:
                    ks.sendText(msg.to, str (e))
#--------------------------------------------------------------------------------
#---------------------------- INVITE CREATOR ------------------------------------
            elif "InviteMeTo: " in msg.text:
                if msg.from_ in creator:
                    gid = msg.text.replace("InviteMeTo: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            cl.findAndAddContactsByMid(msg.from_)
                            cl.inviteIntoGroup(gid,[msg.from_])
                        except:
                            cl.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#--------------------------------------------------------------------------------
#---------------------- MENAMPILKAN KONTAK CREATOR GROUP ------------------------
            elif msg.text in ["Gcreator"]:
              if msg.toType == 2:
                    msg.contentType = 13
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gCreator}
                        gCreator1 = ginfo.creator.displayName
                        
                    except:
                        gCreator = "Error"
                    cl.sendText(msg.to, "Group Creator : " + gCreator1)
                    cl.sendMessage(msg)
#--------------------------------------------------------------------------------
#---------------------------- ADD REM LIST ADMIN --------------------------------
            elif "Admin add @" in msg.text:
                if msg.from_ in creator:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Admin add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    gs = satpam.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"Admin Ditambahkan")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command DiTolak")
                    cl.sendText(msg.to,"Admin Tidak Bisa Menggunakan")

            elif "Admin remove @" in msg.text:
                if msg.from_ in creator:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Admin remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = satpam.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        #ki.sendText(msg.to,"Contact not found")
						random.choice(KAC).sendText(msg.to,"Kontak tidak ditemukan")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Admin Dihapus")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command DiTolak")
                    cl.sendText(msg.to,"Admin Tidak Bisa Menggunakan")

            elif msg.text in ["Adminlist","adminlist"]:
              if msg.from_ in creator:
                if admin == []:
                    cl.sendText(msg.to,"The adminlist is empty")
                else:
                    cl.sendText(msg.to,"Tunggu...")
                    mc = "||Admin duduL Bot||\n=====================\n"
                    for mi_d in admin:
                        mc += "••>" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
#--------------------------------------------------------------------------
#---------------------------- BOT ADD FRIEND ------------------------------
            elif "Bot Add @" in msg.text:
				if msg.toType == 2:
					if msg.from_ in creator:
						print "[Command]Add executing"
						_name = msg.text.replace("Bot Add @","")
						_nametarget = _name.rstrip('  ')
						gs = cl.getGroup(msg.to)
						gs = ki.getGroup(msg.to)
						gs = kk.getGroup(msg.to)
						gs = kc.getGroup(msg.to)
						gs = ks.getGroup(msg.to)
						targets = []
						for g in gs.members:
							if _nametarget == g.displayName:
								targets.append(g.mid)
						if targets == []:
							random.choice(KAC).sendText(msg.to,"Contact not found")
						else:
							for target in targets:
								try:
									cl.findAndAddContactsByMid(target)
									ki.findAndAddContactsByMid(target)
									kk.findAndAddContactsByMid(target)
									kc.findAndAddContactsByMid(target)
									ks.findAndAddContactsByMid(target)
								except:
									cl.sendText(msg.to,"Error")
					else:
						cl.sendText(msg.to,"Perintah Ditolak")
						cl.sendText(msg.to,"Perintah ini Hanya Untuk creator")
#-------------------------------------------------------------------------
#---------------------------- FUNGSI ON OFF ------------------------------	
            elif msg.text in ["Joinn on","joinn on","protectjoin on"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Joinn off","joinn off","protectjoin off"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
						
            elif msg.text in ["Mad On","mad on"]:
              if msg.from_ in admin:
                 if wait["Protectcancel"] == True:
                    if wait["lang"] == "JP":
                         cl.sendText(msg.to,"please dont cancel anyone")
                    else:
                         cl.sendText(msg.to,"done")
                 else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Mad Off","mad off"]:
              if msg.from_ in admin:
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                    else:
                        cl.sendText(msg.to,"done")

            elif msg.text in ["Member join on"]:
              if msg.from_ in admin:
                 if wait["MemberJoin"] == True:
                    if wait["lang"] == "JP":
                         cl.sendText(msg.to,"sapaan untuk member join aktif")
                    else:
                         cl.sendText(msg.to,"done")
                 else:
                    wait["MemberJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"sapaan untuk member join aktif")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Member join off"]:
              if msg.from_ in admin:
                if wait["MemberJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"sapaan untuk member join off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["MemberJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"sapaan untuk member join off")
                    else:
                        cl.sendText(msg.to,"done")
						
            elif msg.text in ["Member left on"]:
              if msg.from_ in admin:
                 if wait["MemberLeft"] == True:
                    if wait["lang"] == "JP":
                         cl.sendText(msg.to,"sapaan untuk member left aktif")
                    else:
                         cl.sendText(msg.to,"done")
                 else:
                    wait["MemberLeft"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"sapaan untuk member left aktif")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Member left off"]:
              if msg.from_ in admin:
                if wait["MemberLeft"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"sapaan untuk member left off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["MemberLeft"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"sapaan untuk member left off")
                    else:
                        cl.sendText(msg.to,"done")
						
            elif msg.text in ["Tag on"]:
              if msg.from_ in admin:
                 if wait["Protectdisplayname"] == True:
                    if wait["lang"] == "JP":
                         cl.sendText(msg.to,"kick user tag")
                    else:
                         cl.sendText(msg.to,"done")
                 else:
                    wait["Protectdisplayname"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick user tag")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Tag off"]:
              if msg.from_ in admin:
                if wait["Protectdisplayname"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick user tag off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectdisplayname"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick user tag off")
                    else:
                        cl.sendText(msg.to,"done")
						
            elif msg.text in ["Bmo on"]:
              if msg.from_ in admin:
                 if wait["Protectbmo"] == True:
                    if wait["lang"] == "JP":
                         cl.sendText(msg.to,"done")
                    else:
                         cl.sendText(msg.to,"done")
                 else:
                    wait["Protectbmo"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Bmo off"]:
              if msg.from_ in admin:
                if wait["Protectbmo"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectbmo"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"done")
						
            elif msg.text in ["Bmo out on"]:
              if msg.from_ in admin:
                 if wait["Protectbmo2"] == True:
                    if wait["lang"] == "JP":
                         cl.sendText(msg.to,"done")
                    else:
                         cl.sendText(msg.to,"done")
                 else:
                    wait["Protectbmo2"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Bmo out off"]:
              if msg.from_ in admin:
                if wait["Protectbmo2"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectbmo2"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"done")						
#----------------------------------------------------------------------
#---------------------------- BL VIA TAG ------------------------------
            elif ("Ban " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Banned")
                   except:
                      pass
#--------------------------------------------------------------------
#---------------------------- STEAL DP ------------------------------					  
            elif "Steal dp @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Steal dp @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#----------------------------------------------------------------------
#---------------------------- STEAL HOME ------------------------------					
            elif "Steal home @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Steal home @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:                                                                   ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#-------------------------------------------------------------------------
#---------------------------- STEAL VIA MID ------------------------------
            elif "Steal " in msg.text:
                if msg.from_ in admin:
                    salsa = msg.text.replace("Steal ","")
                    Manis = cl.getContact(salsa)
                    Imoet = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    try:
                        cover = cl.channel.getCover(Manis)
                    except:
                        cover = ""
                    cl.sendText(msg.to,"Gambar Foto Profilenya")
                    cl.sendImageWithURL(msg.to,Imoet)
                    if cover == "":
                        cl.sendText(msg.to,"User tidak memiliki cover atau sejenisnya")
                    else:
                        cl.sendText(msg.to,"Gambar Covernya")
                        cl.sendImageWithURL(msg.to,cover)
#--------------------------------------------------------------------------------
#---------------------------- MENGIKUTI KATA (MIMIC) ----------------------------
            elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
            	text = msg.text
            	if text is not None:
            		cl.sendText(msg.to,text)
            	else:
            		if msg.contentType == 7:
            			msg.contentType = 7
            			msg.text = None
            			msg.contentMetadata = {
            							 	 "STKID": "6",
            							 	 "STKPKGID": "1",
            							 	 "STKVER": "100" }
            			cl.sendMessage(msg)
            		elif msg.contentType == 13:
            			msg.contentType = 13
            			msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
            			cl.sendMessage(msg)					
						
            elif "Mimic:" in msg.text:
            	if msg.from_ in admin:
            		cmd = msg.text.replace("Mimic:","")
            		if cmd == "on":
            			if mimic["status"] == False:
            				mimic["status"] = True
            				cl.sendText(msg.to,"Mimic on")
            			else:
            				cl.sendText(msg.to,"Mimic already on")
            		elif cmd == "off":
            			if mimic["status"] == True:
            				mimic["status"] = False
            				cl.sendText(msg.to,"Mimic off")
            			else:
            				cl.sendText(msg.to,"Mimic already off")
            		elif "add:" in cmd:
            			target0 = msg.text.replace("Mimic:add:","")
            			target1 = target0.lstrip()
            			target2 = target1.replace("@","")
            			target3 = target2.rstrip()
            			_name = target3
            			gInfo = cl.getGroup(msg.to)
            			targets = []
            			for a in gInfo.members:
            				if _name == a.displayName:
            					targets.append(a.mid)
            			if targets == []:
            				cl.sendText(msg.to,"No targets")
            			else:
            				for target in targets:
            					try:
            						mimic["target"][target] = True
            						cl.sendText(msg.to,"Success added target")
            						#cl.sendMessageWithMention(msg.to,target)
            						break
            					except:
            						cl.sendText(msg.to,"Failed")
            						break
            		elif "del:" in cmd:
            			target0 = msg.text.replace("Mimic:del:","")
            			target1 = target0.lstrip()
            			target2 = target1.replace("@","")
            			target3 = target2.rstrip()
            			_name = target3
            			gInfo = cl.getGroup(msg.to)
            			targets = []
            			for a in gInfo.members:
            				if _name == a.displayName:
            					targets.append(a.mid)
            			if targets == []:
            				cl.sendText(msg.to,"No targets")
            			else:
            				for target in targets:
            					try:
            						del mimic["target"][target]
            						cl.sendText(msg.to,"Success deleted target")
            						#cl.sendMessageWithMention(msg.to,target)
            						break
            					except:
            						cl.sendText(msg.to,"Failed!")
            						break
            		elif cmd == "ListTarget":
            			if mimic["target"] == {}:
            				cl.sendText(msg.to,"No target")
                    	else:
                    		lst = "<<ListTarget>>"
                    		total = len(mimic["target"])
                    		for a in mimic["target"]:
                				if mimic["target"][a] == True:
                					stat = "On"
                				else:
                					stat = "Off"
                				lst += "\n->" + cl.getContact(mi_d).displayName + " | " + stat
                                cl.sendText(msg.to,lst + "\nTotal:" + total)
#-------------------------------------------------------------------
#---------------------------- YOUTUBE ------------------------------
            elif ".Youtube " in msg.text:
                 query = msg.text.replace(".Youtube ","")
                 with requests.session() as s:
                     s.headers['user-agent'] = 'Mozilla/5.0'
                     url    = 'http://www.youtube.com/results'
                     params = {'search_query': query}
                     r    = s.get(url, params=params)
                     soup = BeautifulSoup(r.content, 'html5lib')
                     for a in soup.select('.yt-lockup-title > a[title]'):
                         if '&List' not in a['href']:
                               cl.sendText(msg.to,'http://www.youtube.com' + a['href'] + a['title'])
#----------------------------------------------------------------------------
#--------------------------------- HI / HAI ---------------------------------
            elif msg.text.lower() in ["hi","hai","apa"]:
                if msg.from_ in admin:
                    beb = "Hi sayang " + cl.getContact(msg.from_).displayName #+ " 􀸂􀆇starry heart􏿿"
                    kk.sendText(msg.to,beb)
                else:
                    hi = "Hi " + cl.getContact(msg.from_).displayName
                    cl.sendText(msg.to,hi)
#----------------------------------------------------------------------------
#--------------------------------- TRANSLATE --------------------------------
            elif "translate-en " in msg.text:
                txt = msg.text.replace("translate-en ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'en')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate EN'
                except:
                    cl.sendText(msg.to,'Error.')

            elif "translate-id " in msg.text:
                txt = msg.text.replace("translate-id ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'id')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate ID'
                except:
                    cl.sendText(msg.to,'Error.')
					
            elif msg.text == "Trans":
                text = "Translator\n'tr: ' -> To Indo\n'tr-en: ' -> Indonesia-English"
            elif "tr: " in msg.text:
                isi = msg.text.replace("tr: ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-en: " in msg.text:
                isi = msg.text.replace("tr: ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-fr: " in msg.text:
                isi = msg.text.replace("tr: ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='fr')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-ar: " in msg.text:
                isi = msg.text.replace("tr: ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ar')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-cn: " in msg.text:
                isi = msg.text.replace("tr: ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='zh-CN')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-de: " in msg.text:
                isi = msg.text.replace("tr: ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='de')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-hi: " in msg.text:
                isi = msg.text.replace("tr: ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='hi')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-jp: " in msg.text:
                isi = msg.text.replace("tr: ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ja')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-jw: " in msg.text:
                isi = msg.text.replace("tr: ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='jw')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-ko: " in msg.text:
                isi = msg.text.replace("tr: ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ko')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-th: " in msg.text:
                isi = msg.text.replace("tr: ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='th')
                A = hasil.text
                A = A.encode('utf-8')
#-----------------------------------------------------------------------
#---------------------------- FUNGSI CHAT ------------------------------
            elif msg.text in ["hmm"]:
				if msg.from_ in admin:
					ki.sendText(msg.to,"Tenggorokam sakit ka??")
            elif msg.text in ["wkwkwk"]:
				if msg.from_ in admin:
					ki.sendText(msg.to,"dih si duduL ngakak")
            elif msg.text in ["bunda"]:
				if msg.from_ in admin:
					cl.sendText(msg.to,"araey sayang amel")
					ki.sendText(msg.to,"araey sayang amel")
					kk.sendText(msg.to,"araey sayang amel􏿿")
					kc.sendText(msg.to,"araey sayang amel")
            elif msg.text in ["welcome"]:
				if msg.from_ in admin:
					ki.sendText(msg.to,"Selamat datang di Grup")
					kk.sendText(msg.to,"Jangan nakal ok!")
            elif msg.text in ["amel","mila","bunda aramel"]:
				if msg.from_ in admin:			    
				    ki.sendText(msg.to,"cari aja")
				    kk.sendText(msg.to,"Di Smule")
				    kc.sendText(msg.to,"......")
            elif msg.text in ["Respon","respon","Respon Dong","respon dong"]:
				if msg.from_ in admin:
					cl.sendText(msg.to,"Respon Lambat duL")
					ki.sendText(msg.to,"Yg penting gk lemot")
					kk.sendText(msg.to,"Nggak lemot gundulmu....")
					kc.sendText(msg.to,".............")
#----------------------------------------------------------------------------
#------------------------------ BROADCAST PC --------------------------------
            elif "bc " in msg.text:
                if msg.from_ in admin:
                    broadcasttxt = msg.text.replace("bc ", "")
                    orang = cl.getAllContactIds()
                    for manusia in orang:
                        cl.sendText(manusia,(broadcasttxt))
                        print "[Command] BC Contact"
#----------------------------------------------------------------------------
#----------------------------- BROADCAST Group ------------------------------
            elif "bcgc " in msg.text:
                if msg.from_ in admin:
                    broadcasttxt = msg.text.replace("bcgc ", "")
                    orang = cl.getGroupIdsJoined()
                    for manusia in orang:
                        cl.sendText(manusia,(broadcasttxt))
                        print "[Command] BC Grup"
#-----------------------------------------------------------------------
#---------------------------- MID VIA TAG ------------------------------
            elif "Mid @" in msg.text:
            	if msg.from_ in admin:
                  _name = msg.text.replace("Mid @","")
                  _nametarget = _name.rstrip(' ')
                  gs = cl.getGroup(msg.to)
                  for g in gs.members:
                      if _nametarget == g.displayName:
                          random.choice(KAC).sendText(msg.to, g.mid)
                      else:
                          pass
#---------------------------------------------------------------------
#---------------------------- SPEED BOT ------------------------------
            elif msg.text in ["Sp","Speed","speed"]:
				if msg.from_ in admin:
					start = time.time()
					cl.sendText(msg.to, "Waiting...")
					elapsed_time = time.time() - start
					cl.sendText(msg.to, "%sdetik" % (elapsed_time))
					elapsed_time = time.time() - start
					ki.sendText(msg.to, "%sdetik" % (elapsed_time))
					elapsed_time = time.time() - start
					kk.sendText(msg.to, "%sdetik" % (elapsed_time))
					elapsed_time = time.time() - start
					kc.sendText(msg.to, "%sdetik" % (elapsed_time))
					elapsed_time = time.time() - start
					ks.sendText(msg.to, "%sdetik" % (elapsed_time))
#--------------------------------------------------------------------------
#---------------------------- RESPONNAME BOT ------------------------------					
            elif msg.text.lower() == 'responsname':
              if msg.from_ in admin:
                profile = cl.getProfile()
                text = profile.displayName
                cl.sendText(msg.to, text)
                profile = ki.getProfile()
                text = profile.displayName
                ki.sendText(msg.to, text)
                profile = kk.getProfile()
                text = profile.displayName
                kk.sendText(msg.to, text)
                profile = kc.getProfile()
                text = profile.displayName
                kc.sendText(msg.to, text)
                profile = ks.getProfile()
                text = profile.displayName
                ks.sendText(msg.to, text)
#-----------------------------------------------------------------------
#---------------------------- CLEAR ALL BL -----------------------------  
            elif msg.text in ["Clear ban"]:
              if msg.from_ in admin:
                wait["blacklist"] = {}
                cl.sendText(msg.to,"clear")
#--------------------------------------------------------------------------
#---------------------------- BL VIA CONTACT ------------------------------
            elif msg.text in ["Ban"]:
				if msg.from_ in admin:
					wait["wblacklist"] = True
					cl.sendText(msg.to,"kirim kontak")
#--------------------------------------------------------------------------
#---------------------------- WL VIA CONTACT ------------------------------					
            elif msg.text in ["Unban"]:
				if msg.from_ in admin:
					wait["dblacklist"] = True
					cl.sendText(msg.to,"kirim kontak")
#------------------------------------------------------------------
#---------------------------- CEK BL ------------------------------
            elif msg.text.lower() == 'cek ban':
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    ki.sendText(msg.to,"􀜁􀇔􏿿 Nothing in the blacklist")
                else:
                    ki.sendText(msg.to,"􀜁􀇔􏿿 following is a blacklist")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "➡" +ki.getContact(mi_d).displayName + "\n"
                    ki.sendText(msg.to,mc)
#-------------------------------------------------------------------------
#---------------------------- BLOCK VIA TAG ------------------------------
            elif "Block @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[block] OK"
                    _name = msg.text.replace("Block @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                           targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to, "Not Found...")
                    else:
                        for target in targets:
                            try:
                               cl.blockContact(target)
                               cl.sendText(msg.to, "Success block contact~")
                            except Exception as e:
                               print e					
#----------------------------------------------------------------------
#---------------------------- LIST BLOCK ------------------------------
            elif msg.text in ["blocklist"]:
              if msg.from_ in admin:
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Please wait...")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)
#------------------------------------------------------------------
#---------------------------- CEK BL ------------------------------
            elif msg.text.lower() == 'banlist':
                if msg.from_ in admin:
                  if msg.toType == 2:
                      group = cl.getGroup(msg.to)
                      gMembMids = [contact.mid for contact in group.members]
                      matched_list = []
                      for tag in wait["blacklist"]:
                          matched_list+=filter(lambda str: str == tag, gMembMids)
                      cocoa = ""
                      for mm in matched_list:
                          cocoa += "➡" +cl.getContact(mm).displayName + "\n"
                      cl.sendText(msg.to,cocoa + "====Daftar Blacklist====")
					  
            elif msg.text in ["cek bl"]:
				if msg.from_ in admin:
					if wait["blacklist"] == {}:
						cl.sendText(msg.to,"􀜁􀇔􏿿 Nothing in the blacklist")
					else:
						cl.sendText(msg.to,"blacklist user")
						mc = ""
						for mi_d in wait["blacklist"]:
							mc += "⇨" +cl.getContact(mi_d).displayName + "\n"
						cl.sendText(msg.to,mc)
#-------------------------------------------------------------------
#---------------------------- KICK WL ------------------------------
            elif msg.text in ["Kill ban"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						if matched_list == []:
							random.choice(KAC).sendText(msg.to,"tidak ada daftar blacklist")
							return
						for jj in matched_list:
							random.choice(KAC).kickoutFromGroup(msg.to,[jj])
							cl.sendText(msg.to,"Bye...")
#-------------------------------------------------------------------------
#---------------------------- CLEAR INVITAN ------------------------------
            elif msg.text in ["Clear"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.invitee]
						for _mid in gMembMids:
							cl.cancelGroupInvitation(msg.to,[_mid])
						cl.sendText(msg.to,"I pretended to cancel and canceled.")
#------------------------------------------------------------------
#---------------------------- RANDOM ------------------------------
            elif "random:" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						strnum = msg.text.replace("random:","")
						source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
						try:
							num = int(strnum)
							group = cl.getGroup(msg.to)
							for var in range(0,num):
								name = "".join([random.choice(source_str) for x in xrange(10)])
								group.name = name
								cl.updateGroup(group)
						except:
							cl.sendText(msg.to,"Error")
#-----------------------------------------------------------------
#---------------------------- ALBUM ------------------------------
            elif "album" in msg.text:
				if msg.from_ in admin:
					try:
						albumtags = msg.text.replace("album","")
						gid = albumtags[:6]
						name = albumtags.replace(albumtags[:34],"")
						cl.createAlbum(gid,name)
						cl.sendText(msg.to,name + "created an album")
					except:
						cl.sendText(msg.to,"Error")
#-------------------------------------------------------------------
#---------------------------- FAKECAT ------------------------------
            elif "fakecat" in msg.text:
				if msg.from_ in admin:
					try:
						source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
						name = "".join([random.choice(source_str) for x in xrange(10)])
						anu = msg.text.replace("fakecat","")
						cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
					except Exception as e:
						try:
							cl.sendText(msg.to,str(e))
						except:
							pass
#----------------------------------------------------------------
#---------------------------- CCTV ------------------------------
        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = cl.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n[•]" + Name
                wait2['ROM'][op.param1][op.param2] = "[•]" + Name
                wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            else:
              cl.sendText
          except:
             pass
#------------------------------------------------------------------
#---------------------------- FINISH ------------------------------
#------------------------------------------------------------------
#---------------------------- FINISH ------------------------------
#------------------------------------------------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def autolike():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kk.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kc.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ks.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   satpam.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   print "Like"
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          kk.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          kc.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ks.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          satpam.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

#def autolike():
#			for zx in range(0,20):
#				hasil = cl.activity(limit=20)
#				if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
#					try:    
#						cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						#cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By Aogiri Cyber Line\n\n line://ti/p/~4r4m3l")
#						ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						#ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By Aogiri Cyber Line\n\n line://ti/p/~adinda_pratiwie ")
#						kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						#kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By Aogiri Cyber Line\n\n line://ti/p/~4r4m3l")
#						kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						#kc.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By Aogiri Cyber Line\n\n line://ti/p/~adinda_pratiwie ")
#						ks.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						#ks.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By Aogiri Cyber Line\n\n line://ti/p/~4r4m3l")
#						satpam.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						#satpam.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By Aogiri Cyber Line\n\n line://ti/p/~adinda_pratiwie ")
#						print "DiLike"
#					except:
#							pass
#				else:
#						print "Sudah DiLike"
#			time.sleep(500)
#thread2 = threading.Thread(target=autolike)
#thread2.daemon = True
#thread2.start()

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
				
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
				
                profile2 = ki.getProfile()
                profile2.displayName = wait["cName2"] + nowT
                ki.updateProfile(profile2)

                profile3 = kk.getProfile()
                profile3.displayName = wait["cName3"] + nowT
                kk.updateProfile(profile3)
                
                profile4 = kc.getProfile()
                profile4.displayName = wait["cName4"] + nowT
                kc.updateProfile(profile4)
				
                profile5 = ks.getProfile()
                profile5.displayName = wait["cName5"] + nowT
                ks.updateProfile(profile5)

                #profile6 = satpam.getProfile()
                #profile6.displayName = wait["cName6"] + nowT
                #satpam.updateProfile(profile6)
				
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
