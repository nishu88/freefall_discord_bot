import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os
import requests
from re import split,sub

from bs4 import BeautifulSoup

overall_miss=0
miss=0
overall_questions=0

Client = discord.Client()
client = commands.Bot(command_prefix = "?")

chat_filter = ["DISCOdRD"]
bypass_list = []

@client.event
async def on_ready():
    print("Bot is online and connected to Discord")
##    await client.say("Bot is online and connected to Discord")
    await client.change_presence(game=discord.Game(name="Busy Being AWESOME"))


@client.event
async def on_message(message):
    global overall_miss,miss,overall_questions,id1,abcd1
        

    if message.content.lower().startswith('?miss'):
         overall_miss=overall_miss+1
         miss=miss+1
        
    if message.content.lower().startswith('?reset'):
         miss=0

         
    if message.content.lower().startswith('?thankyou'):
         
         await client.send_message(message.channel, "Thank you for your TRUST in the BLOT (not a typo)")
         await client.send_message(message.channel, "Developed by- <@277695189131460609>")
         await client.send_message(message.channel, "Subscription- FREE until i change my mind :P")
         await client.send_message(message.channel, "Today's stats =  "+ str(10-miss)+" / " +str(10))
         #await client.send_message(message.channel, "Overall stats =  "+ str(overall_questions-overall_miss)+" / " +str(overall_questions))
         #await client.send_message(message.channel, "Accuracy =  "+ str((overall_questions-overall_miss)/ overall_questions*100))
         #await client.send_message(message.channel, "BLOT going to Sleep   :sleeping:")
    
    if message.content.lower() == "cookie":
        await client.send_message(message.channel, ":cookie:") #responds with Cookie emoji when someone says "cookie"
        
    if message.content.lower() == "owner" or message.content.lower() == "?father" or message.content.lower() == "?owner" or message.content.lower() == "?maker":
        await client.send_message(message.channel, "<@277695189131460609> NISHANTH D ALUHONNU")

    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
        
    if message.content.lower() == "?here":    
        if str(message.author.id)=="277695189131460609" or str(message.author.id)=="366125961206300673":
            id1= str(message.channel.id )
            await client.send_message(message.channel, "Got it")
            
      
        
        
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
                    #await client.delete_message(message)
                    await asyncio.sleep(1)
                    await client.send_message(message.channel, "<Discord> is not a bad word !!! <@159985870458322944> you NUTS??   :sunglasses: ")#**Hey!** You're not allowed to use that word here!
                except discord.errors.NotFound:
                    return

                
    if message.content.lower().startswith('?guess '):
        
        overall_questions = overall_questions +1
        
        var=message.content
        var=var[6:]
        s=var.split("\n")
        
        length=len(s)      
        if(len(s[0])<6):
            s[0]=""
        
        o3=s[length-1]
        o2=s[length-2]
        o1=s[length-3]        
        q=" "
        for i in range(0,length-3):
            if q[-1] !=" ":
                q=q+" "
            q+=s[i]
            
        #await client.send_message(message.channel, q)   
        
        q=q.replace(" ","+")
            
        


##        tab="https://www.bing.com/search?q="
        tabb="https://search.aol.com/aol/search?s_chn=prt_bon&q=" 
        tab1="https://search.aol.com/aol/search?s_chn=prt_bon&q=" #num=30&ei=py29WruLGoiSvQSbsIjYAg&
        tab2="https://www.google.co.in/search?q="
        tab3="https://duckduckgo.com/html/?q="
        
        #await client.send_message(message.channel, tab2+q)
        #await client.send_message(discord.Object(id=id1),tab2+q)
        
##        response=requests.get(tab+q+"&count=30")        
##        soup=BeautifulSoup(response.text,"html.parser")        
        response1=requests.get(tabb+q)        
        soup1=BeautifulSoup(response1.text,"html.parser")
        #print(soup1)
        
        
        #print (links)
        for link in  soup1.find_all("a",{"class": " ac-algo fz-l ac-21th lh-24"}):                  
              firstlink=split(":(?=http)",link["href"].replace("/url?q=",""))
              break
                
            
           # print (firstlink)
        
        
            
        firstlink[0]=firstlink[0][0:]
        #print(firstlink[0])
        
        response2=requests.get(firstlink[0])        
        soup2=BeautifulSoup(response2.text,"html.parser")

        response3=requests.get(tab3+q)        
        soup3=BeautifulSoup(response3.text,"html.parser")

            
            #break
##        for anchor in soup.findAll('a', href=True):
##            print anchor['href']
##        ss1=soup.get_text().lower()       
        ss2=soup1.get_text().lower()
        #print (ss2)
        ss3=soup2.get_text().lower()
        ss4=soup3.get_text().lower()
        ##        ss15=ss1.split(" resultsdate language region",1)[0]
        ##        ss1=ss1.split(" resultsdate language region",1)[1]
        #print(ss1)
##        ss1=sub('\W+','', ss1)
        ss2=sub('\W+','', ss2)
        ss3=sub('\W+','', ss3)
        ss4=sub('\W+','', ss4)
        #re.sub('\W+','', string)

        ox=o1.lower().split(" ")
        oy=o2.lower().split(" ")
        oz=o3.lower().split(" ")
##        print(ox)
##        print(oy)
##        print(oz)
        

        oa=sub('\W+','', o1)
        ob=sub('\W+','', o2)
        oc=sub('\W+','', o3)
        
        ca=ss3.count(oa.lower())       
        cb=ss3.count(ob.lower())
        cc=ss3.count(oc.lower())
        
        c1= ss2.count(oa.lower()) + ca +ss4.count(oa.lower())#+ss1.count(oa.lower())
        c2= ss2.count(ob.lower()) + cb+ss4.count(ob.lower())#+ ss1.count(ob.lower()) 
        c3=   ss2.count(oc.lower()) + cc+ss4.count(oc.lower())#+ ss1.count(oc.lower()) 

        print()
        m=max(c1,c2,c3)
        m1=min(c1,c2,c3)
        #await client.send_message(message.channel, o1+"       "+str(c1)+"           "+str(ca))
        #await client.send_message(message.channel, o2+"       "+str(c2)+"           "+str(cb))
        #await client.send_message(message.channel, o3+"       "+str(c3)+"           "+str(cc))

                
        if m==c1:
            
            await client.send_message(message.channel,"\n"+" "+"111   "+o1)            
            #await client.send_message(discord.Object(id='464836410373832704'), 'hello')
            if(m!=0):
##                await client.send_message(discord.Object(id=id1),"\n"+"Best Possibility=  "+"111   "+o1)                
                await client.send_message(discord.Object(id=id1),embed=discord.Embed(description="Best Possibility", colour=0x3DF270).set_author(name=o1,icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/NYCS-bull-trans-1.svg/1024px-NYCS-bull-trans-1.svg.png"))
                
        elif m==c2:
            await client.send_message(message.channel, "\n"+" "+"222   "+o2)
##            await client.send_message(discord.Object(id=id1), "\n"+"Best Possibility=  "+"222   "+o2)   
            await client.send_message(discord.Object(id=id1),embed=discord.Embed(description="Best Possibility", colour=0x3DF270).set_author(name=o2,icon_url="https://image.ibb.co/bTTHWy/number_2_two_icon_11920.png"))
            
        elif m==c3:
            await client.send_message(message.channel, "\n"+"  "+"333   "+o3)
            #await client.send_message(discord.Object(id=id1), "\n"+"Best Possibility=  "+"333   "+o3)
            await client.send_message(discord.Object(id=id1),embed=discord.Embed(description="Best Possibility", colour=0x3DF270).set_author(name=o3,icon_url="https://i0.wp.com/tantrwm.com/wp-content/uploads/2016/11/Tantrwm-Video-Production-Wales-Filming-Live-Streaming-Webcasts-Webcastings-Production-3-man-film-crew.png?fit=2000%2C2000"))
           
         
        if m1==c1:
            #await client.send_message(message.channel, "\n"+"Least=  "+"111   "+o1)  
            if(m!=0):
                await client.send_message(discord.Object(id=id1),"```\n"+"Least Possibility=  "+"111   "+o1+"```")
                
        elif m1==c2:
            #await client.send_message(message.channel, "\n"+"Least =  "+"222   "+o2)
            await client.send_message(discord.Object(id=id1),"```\n"+"Least Possibility=  "+"222   "+o2+"```")
        elif m1==c3:
            #await client.send_message(message.channel, "\n"+"Least =  "+"333   "+o3)
            await client.send_message(discord.Object(id=id1),"```\n"+"Least Possibility=  "+"333   "+o3+"```")

                
                    
        ##        print(c1)
        ##        print(o2)
        ##        print(c2)
        ##        print(o3)
        ##        print(c3)      

        cxx=0
        cyy=0
        czz=0
        abcd=" "
        
        if(len(ox)>=1):
            for w in ox:
                w=sub('\W+','', w)
                if(len(w)>2 and w !="the" and w !="that" and w !="this" and w !="and" ):
                    if(w not in oy and w not in oz):
                        cx=ss2.count(w.lower()) + ss3. count(w.lower())+ss4.count(w.lower())
                        cxx=cxx+cx                       
                        abcd=abcd+ str(w)+"  ("+str(cx)+")  "
        abcd1 =   abcd + "\n"   
        await client.send_message(message.channel, "       "+abcd+"        "+str(cxx) )
        abcd=""
##        await client.send_message(message.channel, "       "+ )
        if(len(oy)>=1):
            for w in oy:
                w=sub('\W+','', w)
                if(len(w)>2 and w !="the" and w !="that" and w !="this" and w !="and" ):
                    if(w not in ox and w not in oz):
                        cy=ss2.count(w.lower()) + ss3. count(w.lower())+ss4.count(w.lower())
                        cyy=cyy+cy
                        abcd=abcd+str(w)+"  ("+str(cy)+")  "
        abcd1=abcd1+abcd+"\n"               
        await client.send_message(message.channel, "       "+abcd+"        "+str(cyy)  )
        abcd=""
##        await client.send_message(message.channel, "       "+str(cyy)  )
        if(len(oz)>=1):
            for w in oz:
                w=sub('\W+','', w)
                if(len(w)>2 and w !="the" and w !="that" and w !="this"  and w !="and" ):
                    if(w not in oy and w not in ox):
                        cz=ss2.count(w.lower()) + ss3. count(w.lower())+ss4.count(w.lower())
                        czz=czz+cz
                        abcd=abcd+str(w)+"  ("+str(cz)+")  "
        abcd1=abcd1+abcd+"\n"                
        await client.send_message(message.channel, "       "+abcd +"        "+str(czz) )
        abcd=""
##        await client.send_message(message.channel, "       "+str(czz)  )
            
  
    if message.content.lower().startswith('?hits'):
        await client.send_message(message.channel,embed=discord.Embed(description=abcd1, colour=0x3DF270).set_author(name="Hits",icon_url="https://image.ibb.co/n250Jd/iconfinder_white.png").set_footer(text="Be a Fountain. Not a Drain. #GiveAndTake") )
            
            
  
                    
        

client.run(os.getenv('TOKEN'))
