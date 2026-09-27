#!/usr/bin/env python3
import argparse,requests
p=argparse.ArgumentParser();p.add_argument("url");a=p.parse_args();u=a.url.rstrip("/")
for x in ("/","/robots.txt","/sitemap.xml","/wp-json/","/api","/swagger.json"):
 try:r=requests.get(u+x,verify=False,timeout=8);print(r.status_code,len(r.content),x,r.url)
 except Exception as e:print("ERR",x,e)
