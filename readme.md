
## Setup
Create a file named `config.yaml` at the root of the project with the following information.  
```
spotify:
  client-id: <client-id>
  client-secret: <client-secret>
genius:
  access-token: <accesstoken>
```
How to get [access token from genius](https://docs.genius.com/#/authentication-h1)  
How to get [secret from spotify](https://developer.spotify.com/documentation/web-api/tutorials/getting-started)

## Usage
create a csv file named `input.csv` and put _title_ and _artist_ seprarated with semicolon.
then you can run the script with `python main.py -i input.csv`

## Language supported
script only support song in **french**,**english**,**spanish** and **dutch**.  
Other language are not supported and statistic might be unclear
