# ShareMyHealth

A consumer-directed health information exchange.

This application is built using Python 3.7 and Django 2.1.x.

The default port for this application is **8001**. This avoids 
conflicts when running the OIDC Server on the same machine.

It will also configure a postgreSQL docker instance on 
port **5432**.

## Deploy with Docker

Docker is supported. 
Run docker with:

     docker-compose -f .development/docker-compose.yml up
     
If you make changes to requirements.txt to add libraries re-run 
docker-compose with the --build option.

If you're working with a fresh db image the migrations have 
to be run.

## Associated Projects

[ShareMyHealth](https://github.com/TransparentHealth/sharemyhealth) is designed as a 
consumer-mediated health information exchange.  
ShareMyHealth acts as a relying party to 
[vmi](https://github.com/TransparentHealth/vmi).

[VerifyMyIdentity - VMI](https://github.com/TransparentHealth/vmi), 
a standards-focused OpenID Connect Identity Provider.

## Supporting Resources

vmi uses css resources from Bootstrap (v.3.3.x) and 
Font-Awesome (v4.4.x). 

