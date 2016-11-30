# demo.slackbot
Slack integration using Synapse for automated savings.

___
>**Disclaimer**
>SynapseBot is only a proof of concept. It is not secure and should never be used for real users, nodes, or transactions.
___

#### Slack Interface

See [samples.md](/samples.md).


#### Non-Docker Instructions

To run:
```
python3 app/app.py && python3 app/slack_event_loop.py
```

#### Docker Instructions

To build:
```
docker build --rm -t misc.slackbot .
```

To run:
```
docker run -d -p 89:80 -v $(pwd)/app:/app
```


#### App Structure

```
app/
├── app.py
├── bot.py
├── commands.py
├── config.py
├── core/
├── db.py
├── models.py
├── schema.sql
├── secrets.py
├── slack_event_loop.py
├── static/
└── templates/
```
