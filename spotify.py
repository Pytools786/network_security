import os

os.chdir(r"C:\Windows\System32\drivers\etc")

cwd = os.getcwd()


my_file = open("hosts", "a")

text_list = ["127.0.0.1 media-match.com\n"
"127.0.0.1 adclick.g.doublecklick.net\n"
"127.0.0.1 www.googleadservices.com\n"
"127.0.0.1 pagead2.googlesyndication.com\n"
"127.0.0.1 googleads.g.doubleclick.net\n"
"127.0.0.1 pubads.g.doubleclick.net\n"
"127.0.0.1 securepubads.g.doubleclick.net\n"
"127.0.0.1 www.omaze.com\n"
"127.0.0.1 omaze.com\n"
"127.0.0.1 bounceexchange.com\n",
"127.0.0.1 core.insightexpressai.com\n",
"127.0.0.1 content.bitsontherun.com\n",
"127.0.0.1 s0.2mdn.net\n",
"127.0.0.1 v.jwpcdn.com\n",
"127.0.0.1 d2gi7ultltnc2u.cloudfront.net\n",
"127.0.0.1 cs283.wpc.teliasoneracdn.net\n",
"127.0.0.1 cs126.wpc.teliasoneracdn.net\n",
"127.0.0.1 u.scdn.co\n",
"127.0.0.1 cs126.wpc.edgecastcdn.net\n",
"127.0.0.1 pagead46.l.doubleclick.net\n",
"127.0.0.1 pagead.l.doubleclick.net\n",
"127.0.0.1 video-ad-stats.googlesyndication.com\n",
"127.0.0.1 pagead-googlehosted.l.google.com\n",
"127.0.0.1 partnerad.l.doubleclick.net\n",
"127.0.0.1 prod.spotify.map.fastlylb.net\n",
"127.0.0.1 adserver.adtechus.com\n",
"127.0.0.1 na.gmtdmp.com\n",
"127.0.0.1 anycast.pixel.adsafeprotected.com\n",
"127.0.0.1 ads.pubmatic.com\n",
"127.0.0.1 idsync-ext.rlcdn.com\n",
"127.0.0.1 www.googletagservices.com\n",
"127.0.0.1 googlehosted.l.googleusercontent.com\n",
"127.0.0.1 d361oi6ppvq2ym.cloudfront.net\n",
"127.0.0.1 gads.pubmatic.com\n",
"127.0.0.1 ads-west-colo.adsymptotic.com\n",
"127.0.0.1 geo3.ggpht.com\n",
"127.0.0.1 showads33000.pubmatic.com\n",
"127.0.0.1 crashdump.spotify.com\n",
"127.0.0.1 adeventtracker.spotify.com\n",
"127.0.0.1 log.spotify.com\n",
"127.0.0.1 analytics.spotify.com\n",
"127.0.0.1 ads-fa.spotify.com\n",
"127.0.0.1 audio-ec.spotify.com\n",
"127.0.0.1 sto3.spotify.com\n",
"127.0.0.1 audio2.spotify.com\n",
"127.0.0.1 http://audio2.spotify.com\n",
"127.0.0.1 www.audio2.spotify.com\n",
"127.0.0.1 desktop.spotify.com\n",
"127.0.0.1 heads-ec.spotify.com\n",
"127.0.0.1 open.spotify.com\n",
"#127.0.0.1 spclient.wg.spotify.com\n",]

my_file.writelines(text_list)

my_file = open("hosts")

print("ALL DONE ... ")

print("YOU ARE READY TO GO")
my_file.close()
