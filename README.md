# sshare
secure share client

## Commands

* c:token - create new one-time token
* c:delete:[token/url] - delete file/token

## Default values

Put the following into ~/.sshare.yml:

```ymal
sshare:
  url: https://YOURDOMAIN
  upload-key: YOURKEY
  timeout: 3600
```
