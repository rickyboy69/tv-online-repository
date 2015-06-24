# -*- coding: utf-8 -*-

"""tv online
    2013 rickyboy"""

import xbmc,xbmcaddon,xbmcgui,xbmcplugin,urllib,urllib2,os,re,sys,datetime,time
from BeautifulSoup import BeautifulSoup

####################################################### CONSTANTES #####################################################

versao = '0.0.2'
addon_id = 'plugin.video.tv online'
art = '/resources/art/'
selfAddon = xbmcaddon.Addon(id=addon_id)

################################################### MENUS PLUGIN ######################################################

def listar_canais(url):
      dialog = xbmcgui.Dialog()
      dialog.ok("Fórum", "tv portugal.")
      for line in urllib2.urlopen(url).readlines():
            params = line.split(',')
            try:
                  nome = params[0]
                  print 'Nome: ' + nome
                  img = params[1].replace(' rtmp','rtmp').replace(' rtsp','rtsp').replace(' http','http')
                  print 'Img: ' + img
                  rtmp = params[2].replace(' rtmp','rtmp').replace(' rtsp','rtsp').replace(' http','http')
                  print 'Link: ' + rtmp
                  addLink(nome,rtmp,img)
            except:
                  pass
      xbmc.executebuiltin("Container.SetViewMode(500)")


################################################## PASTAS ################################################################

def addLink(name,url,iconimage):
      liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
      liz.setInfo( type="Video", infoLabels={ "Title": name } )
      liz.setProperty('fanart_image', "%s/fanart.jpg"%selfAddon.getAddonInfo("path"))
      return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)


######################################################## OUTRAS FUNCOES ###############################################

def get_params():
      param=[]
      paramstring=sys.argv[2]
      if len(paramstring)>=2:
            params=sys.argv[2]
            cleanedparams=params.replace('?','')
            if (params[len(params)-1]=='/'):
                  params=params[0:len(params)-2]
            pairsofparams=cleanedparams.split('&')
            param={}
            for i in range(len(pairsofparams)):
                  splitparams={}
                  splitparams=pairsofparams[i].split('=')
                  if (len(splitparams))==2:
                        param[splitparams[0]]=splitparams[1]                 
      return param

params=get_params()
url=None
name=None
mode=None
tamanhoparavariavel=None

try: url=urllib.unquote_plus(params["url"])
except: pass
try: tamanhoparavariavel=urllib.unquote_plus(params["tamanhof"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except: pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "Name: "+str(tamanhoparavariavel)

if mode==None or url==None or len(url)<1:
      listar_canais('http://www.brasiltvs.com/adminapp/chn/app_channels_v2.txt?1413230775230')
      #listar_canais('http://www.brasiltvs.com/adminapp/app_channels_v2.txt?1399053793680')
elif mode==1: listar_canais(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
