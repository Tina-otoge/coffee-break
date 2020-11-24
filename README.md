# ☕ coffee break
A score card generator for rhythm games

coffee break is a client-server application to generate a score card of any rhythm game inspired by [eAMUSEMENT](https://p.eagate.573.jp) score cards for arcade rhythm games.

coffee break wants to be suitable for any game, and exposes an easy to use API to be integrated in other services such as bots or games themselves.

It turns simple HTTP requests to the API into beautiful and very customizable
scorecards for you to use in your own score server, game, or social medias.

# Example
Request: `/api/generate`  
```js
{
	"game": "SOUND VOLTEX",
	"username": "N.TINA",
	"rank": "SL10",
	"avatar": "https://fairyjoke.tina.moe/api/sdvx/apecas/4521.png",
	
	"title": "Brain Power",
	"artist": "ノマ",
	"jacket": "https://remywiki.com/images/thumb/e/e7/Brain_Power.png/200px-Brain_Power.png",
	"BPM": "170-173",

	"difficulty": "EXHAUST",
	"level": 16,

	"score":  9796493,
	"grade": "AAA",
	"clear_type": "HARD CLEAR",
	"hp": 85,
	"judges": {
		"CRITICAL": 1545,
		"NEAR": 21,
		"ERROR": 13,
	},

	"copyright": "KONMAI",
	"settings": { "auto_combo": true, },
	"class": {
		"difficulty": "red",
		"clear_type": "red",
		"hp": "bg-orange",
		"grade": "gold",
		"judges": { "CRITICAL": "yellow", }
		"rank": "yellow",
		"avatar": "contain",
	}
}
```
Result:  
![scorecard](https://i.imgur.com/asQwqcu.jpeg)

Documentation
-------------

The documentation can be built by running `make html` in the `/docs` folder.

Live version temporarly hosted at https://tina.moe/private/coffee-docs/

- [API reference](api_ref.md)

# Development, issues and features request

Wether you have experience as a dev or not, you can help the project by reporting
issues and request features by
[opening a new issue](https://github.com/asso-msn/coffee-break/issues/new).
Please tag it correctly.

If you are willing to help developing the project, you can either try to fix an
existing issue by submitting a PR for review, or directly submit a PR with your
feature proposal.
