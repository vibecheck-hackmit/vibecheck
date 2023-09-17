# Cool HackMIT Project

## Dev Notes
auth files live in a `.creds` folder
for docker in dev env, run this once
```
docker compose -f docker-compose-dev.yml build
```
and then to take launch
```
docker compose -f docker-compose-dev.yml up
```
and to take down
```
docker compose -f docker-compose-dev.yml down
```
you can also take down only one of the services if you want, for example
```
docker compose -f docker-compose-dev.yml down api
```
works similarly for bringing them back up.



