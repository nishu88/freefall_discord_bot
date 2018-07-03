import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os
import re

from PIL import ImageGrab
from bs4 import BeautifulSoup
from PIL import ImageEnhance

Client = discord.Client()
client = commands.Bot(command_prefix = "?")

chat_filter = ["PINEAPPLE", "APPLE", "CHROME"]
bypass_list = []
print("HI there")
@client.event
async def on_ready():
    print("Bot is online and connected to Discord")
    await client.change_presence(game=discord.Game(name="Busy Being AWESOME"))


@client.event
async def on_message(message):
    if message.content == "cookie":
        await client.send_message(message.channel, ":cookie:") #responds with Cookie emoji when someone says "cookie"

    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content.upper().startswith('!SAY'):
        args = message.content.split(" ")
        #args[0] = !SAY
        #args[1] = Hey
        #args[2] = There
        #args[1:] = Hey There
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))

    contents = message.content.split(" ") #contents is a list type
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "**Hey!** You're not allowed to use that word here!")
                except discord.errors.NotFound:
                    return
    if message.content.lower().startswith('?guess '):
        var=message.content
        var=var[6:]
        s=var.split("\n")
        
        length=len(s)      
        
        
        o3=s[length-1]
        o2=s[length-2]
        o1=s[length-3]        
        q=" "
        for i in range(0,length-3):
            if q[-1] !=" ":
                q=q+" "
            q+=s[i]
            
        q=q.replace(" ","+")
            
        await client.send_message(message.channel, q)
        await client.send_message(message.channel, o1)
        await client.send_message(message.channel, o2)
        await client.send_message(message.channel, o3)

        tab="https://www.bing.com/search?q="
        tabb="https://search.aol.com/aol/search?s_chn=prt_bon&q=" 
        tab1="https://search.aol.com/aol/search?s_chn=prt_bon&q=" #num=30&ei=py29WruLGoiSvQSbsIjYAg&
        tab2="https://www.google.co.in/search?q="        
        
        response=requests.get(tab+q+"&count=30")        
        soup=BeautifulSoup(response.text,"html.parser")        
        response1=requests.get(tabb+q)        
        soup1=BeautifulSoup(response1.text,"html.parser")
        #print(soup1)
        
        links = soup1.findAll("a")
        #print (links)
        ctrrrr=0
        for link in  soup1.find_all("a"):
            ctrrrr+=1
            firstlink=re.split(":(?=http)",link["href"].replace("/url?q=",""))
            #print(firstlink)
            if(ctrrrr==19):              
                break
                
            
           # print (firstlink)
        
        
            
        firstlink[0]=firstlink[0][0:]
        #print(firstlink[0])
        
        response2=requests.get(firstlink[0])        
        soup2=BeautifulSoup(response2.text,"html.parser")
            
            #break
##        for anchor in soup.findAll('a', href=True):
##            print anchor['href']
                
        ss1=soup.get_text().lower()
        #print (ss1)
        ss2=soup1.get_text().lower()
        #print (ss2)
        ss3=soup2.get_text().lower()
##        ss15=ss1.split(" resultsdate language region",1)[0]
##        ss1=ss1.split(" resultsdate language region",1)[1]
        #print(ss1)
        ss1=ss1.replace(" ","")
        ss2=ss2.replace(" ","")
        ss3=ss3.replace(" ","")
        #print (ss3)
        ca=ss3.count(o1.lower().replace(" ",""))       
        cb=ss3.count(o2.lower().replace(" ",""))
        cc=ss3.count(o3.lower().replace(" ",""))        
        c1= ss1.count(o1.lower().replace(" ","")) + ss2.count(o1.lower().replace(" ","")) + ca 
        c2=  ss1.count(o2.lower().replace(" ","")) + ss2.count(o2.lower().replace(" ","")) + cb
        c3=   ss1.count(o3.lower().replace(" ","")) + ss2.count(o3.lower().replace(" ","")) + cc
        
        
        m=max(c1,c2,c3)
        await client.send_message(message.channel, o1+"       "+str(c1)+"           "+str(ca))
        await client.send_message(message.channel, o2+"       "+str(c2)+"           "+str(cb))
        await client.send_message(message.channel, o3+"       "+str(c3)+"           "+str(cc))
        
        if m==c1:
            await client.send_message(message.channel, "\n"+"111   "+o1+" "+o1+" "+o1+" "+o1)
        elif m==c2:
            await client.send_message(message.channel, "\n"+"111   "+o2+" "+o2+" "+o2+" "+o2)
        elif m==c3:
            await client.send_message(message.channel, "\n"+"111   "+o3+" "+o3+" "+o3+" "+o3)        
                    
        

client.run(os.getenv('TOKEN'))
