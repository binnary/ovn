#!/usr/bin/env python
configs="""secret
mktun
rmtun
dev
dev-type
user
group
show-pkcs11-ids
show-gateway"""
import os,sys
print(configs.split())
fileds = locals()
for i in configs.split():
  print(i)
