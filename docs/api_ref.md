# API Reference

## Endpoints

Coffee Break exposes some endpoints to either display or register scorecards.

All endpoints accept both GET and POST requests and behave the same on both.

All the parameters are the same for all endpoints and are described in the
[Parameters](#parameters) section.

### Generate picture

Routes: `/api/generate`, `/api/card.jpg`

Note: The .jpg route can be more convenient with some browsers, as it is more
likely to trigger caching systems.

Accepts params: YES

The returned content is the scorecard and has a mimetype of `image/jpeg`.

### Generate HTML

Route: `/api/card.html`

Accept params: YES

The returned content is the HTML of the scorecard, the one used to generate the
image. This is useful to inspect the different classes and styling elements.

### Register scorecard

Route: `/api/register`

Accept params: YES

Saves the request to the database and returns a JSON object with the ID and the
link of the saved request, in the form:
```js
{
	"id": <ID here>,
	"url": <URL here>
}
```

The URL can be used to [retrieve a registered scorecard](#retrieve-scorecard).

### Retrieve scorecard

Route: `/api/cards/<ID>.jpg`

Accept params: NO

Generates the picture of a previously registered scorecard. The behaviour is the
same as the [Generate picture](#generate-picture) route, except that instead of
taking parameters, the one sent when registering the card are used instead.

### Example scorecards

Example requests are available for reference in the `/examples/requests` folder
at the root of the repository. They can be used to generate pictures or HTML
using the `/api/examples/<example_name>` and `/api/examples/<example_name>.html`
routes respectively.

Accept params: NO

## Parameters

All the accepted parameters are defined and described in the `/coffeebreak/params.py`
file. Please refer to the file for an up-to-date documentation.

All parameters are **optional** and can be omitted freely without breaking the
scorecard generation.

### All parameters

Name            | Type             | Description
----------------|------------------|------------
username        | any              | The player name
player_code     | any              | Some games provide each player with a code to add friends or rivals
rank            | any              | Dan rank, skill level, ...
avatar          | string, URL      | The player avatar
playstyle       | any              | Controller, Keyboard, Tablet, Mobile, ...
profile_extras  | any              | Additional infos displayed under rank and playstyle
game            | any              | The game name
title           | any              | Song title
subtitle        | any              | Used by some games to add additional information or translation
artist          | any              | Song artist
subartist       | any              | Used by some games to add additional information or translation
genre           | any              | Song genre
bpm             | any              | The song BPM, is a string because some games have varying BPM or text as BPM, such as `"170-173"` or `"???"`
jacket          | string, URL      | Song jacket picture
mode            | any              | Useful for games with Single Play and Double Play modes
level           | float or number  | Chart level, such as: `3`, `18` or `9.3`
difficulty      | any              | Chart difficulty name, such as "HYPER", "EX" or "Insane"
notes_count     | number           | The amount of notes in the chart
max_chart_combo | number           | The maximum reachable combo, displayed when the player's max combo is also provided
creator         | any              | The name of the creator of the chart
mods            | JSON array       | A list of difficulty modifiers used while playing, ie: `["EZ", "FL"]`
clear_type      | any              | Sometimes called "medal", usually `"CLEARED"`, `"HARD CLEAR"`, `"FULLCOMBO"`, `"FAILED"`, etc
score           | any              | The actual score
grade           | any              | Sometimes called rank, usually `"AA"`, `"AAA+"`, `"S"`, etc
accuracy        | any              | The hit accuracy
hp              | number [0-100]   | The remaining HP at the end of the song, used to display a bar on the scorecard
max_combo       | any              | The highest combo reached by the player
breaks          | any              | The amount of times the player lose their combo
pp              | any              | The amount of performance points awarded for this score, different from actual score and used in rankings in games such as osu! and Beat Saber score servers
judges          | JSON object      | Mapping of judge names -> amount, ie: `{"PGREAT": 100, "GREAT": 12, "GOOD": 0, "POOR": 2, "BAD": 0}`
date            | any              | The time when the score was realised
copyright       | any              | A custom copyright notice at the bottom of the card
class           | JSON object      | See [the styling section](#styling)
settings        | JSON object      | See [the settings section](#settings)

### Styling

The `class` parameter is a special JSON object passed in the request that can be
used to apply custom styles to the scorecard. It can apply predefined classes to
other elements.

For example, to turn the difficulty name into the color red, the value
`{"difficulty": "red"}` can be used.

#### Classes

Here is a list of the available classes.

Name | Description
-----|------------
gold, red, orange, light-orange, yellow, lime, green, blreen, blue, ocean, purple, mangenta, pink | Apply a color
bg-gold, bg-red, bg-orange, bg-light-orange, ... | Apply a background color
rainbow | Apply a rainbow effect to the text
bg-rainbow | Apply a rainbow effect to the background
borders | Add borders
big-borders | Add bolder borders
rounded-borders | Makes the borders rounded
round | Tries to make the borders round enough to be a circle (looks weird on non-squares)
contain | Always fits picture inside their container, while maintaining ratio

#### Stylable elements

Here is a list of the elements that can be styled

Name | Description
-----|------------
background_color | Special element, takes a color instead of a class
background_image | Special element, takes an URL instead of a class
pp_name | Special element, renames the pp label
level_suffix | Special element, adds to the level
avatar |
rank |
difficulty |
level |
clear_type |
clear_types | JSON object of mapping of clear type names to classes, ie: `{"class": "clear_types": {"FULLCOMBO": "rainbow" }}`
hp |
grade |
grades | JSON object of mapping of grade names to classes, ie: `{"class": "grades": {"SSS": "gold" }}`
score |
judges | JSON object of mapping of judge names to classes, ie: `{"class": "judges": {"PGREAT": "rainbow"}}`


### Settings

Special settings can be enabled using the `settings` parameter. They provided
minor logic to calculate some stuffs before generating the card. Most of the
settings will try to modify the default values when applied, meaning that the
actual parameters always take priority.

For example, to automatically fill the `date` parameter with the current time,
the value `{"auto_date": true}` can be used.

#### List of settings

This is the list of the settings that can be used

Name | Type | Description
-----|------|------------
preset | string | Apply default values to match the style of certain games. Supported values: `"osu!"`, `"IIDX"`. See `/coffeebreak/presets.json` for the actual values. Submit a PR to add more.
auto_combo | any | Calculates `max_chart_combo` by summing all `judges` values.
auto_date | any | Fills `date` with the current date
auto_fc | any or JSON object | Sets `clear_type` to `"FULLCOMBO"` if `breaks` = 0 or `judges.MISS` = 0, otherwise, sets `clear_type` to `CLEARED`. See below for how those values can be customized by using a JSON object.
auto_fc.miss | string | Overrides the judge name for misses to look for when checking for 0 miss
auto_fc.fc | string | The value to use in `clear_type` if there are 0 miss
auto_fc.not_fc | string | The value to use in `clear_type` if there is 1 or more miss
