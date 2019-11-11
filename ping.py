from urllib.request import urlopen


allurls = [,]

gping = "https://www.google.com/ping?sitemap="
bping = "http://www.bing.com/webmaster/ping.aspx?siteMap="

print("Pinging Google & Bing...........")

for url in allurls:
    gpingurl = gping + url
    bpingurl = bping + url

    try:
        with urlopen(gpingurl) as conn:
            print (gpingurl)
            if conn:
                print("Pinged")
            else:
                print("Error in pinging RSS: " + gpingurl +" to Google")

        with urlopen(bpingurl) as conn1:
            print (bpingurl)
            if conn1:
                print("Pinged")
            else:
                print("Error in pinging RSS: " + bpingurl +" to Bing")
    except:
        print("Error")


print("Pinging Done...........")
