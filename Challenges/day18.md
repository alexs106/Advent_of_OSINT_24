# Day 18

Day 18 is probably my favourite challenge because of the subtility of it all.

Okay so first of all they give us a back story of Callisto aka the suspected cyber threat actor.

The first step is to find the domain name that was registered to Callisto that lead to a steroids site knowing that this site and others are now offline.

They give us a little clue knowing we can use their Whois records.

So that's where I started. 

I looked up the who is history of the website we are given :
*live-login.info*

Thanks to this website*, I found the email address used to register the domain : *vladimirdj90@gmail.com*.

*https://osint.sh/whoishistory/

Based on that, I just had to do a reverse whois search* and look up domain names registered to this email.

*https://www.reversewhois.io/?

Thanks to this I found the domain name I needed : 
**mymuscle.org**

Okay so part 2, I needed to find the page for this website on a social network called VK. Knowing that most websites put their social media at the bottom of the page, I used *Wayback Machine* to access the website's last working version from 2017.

Thanks to this I found the link to their VK page :
http://vk.com/mymuscleorg. 

Then I came out of Wayback Machine, else the page doesn't work and found the administrator of the page in *Additional info*: *Valera Brezhnev*.

When going into her VK page I found her birthday : 
September 7th, 1979 or in the format needed **19790907**


**Ranking : 23/222**





