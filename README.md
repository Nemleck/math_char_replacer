# Programm Presentation

This programm can replace what you write (ex: sqrt) with the actual character (for this example, √)

# Keys Configuration

You can use the presets, but also make your events.

`keys.json`
```json
{
    "input": "sqrt",
    "output": "√",
    "params": ["accept_lower_and_upper_case"]
}
```

In this example, every times you will write "sqrt", it will be replaced with √.

The parameter "accept_lower_and_upper_case" makes the programm accept lower AND upper cases. This means you can write "sqrt" but also "SqRt", or "SQRT", and so on.

`keys.json`
```json
{
    "input": "This is ",
    "output": "autocompletion",
    "params": ["keep_text"]
}
```

In this example, we add the parameter "keep_text", that makes the programm no longer remove what you write (here "This is ").
This allows you to make autocompletion, for example.

## Adding key combination

`keys.json`
```json
{
    "input": "hey",
    "output": ["ctrl", "a"],
    "params": ["keep_text"]
},
```

Here, writing "hey" makes you able to select all the text. All you need to know to do that is that it only works in lists.

`keys.json`
```json
{
    "input": ["ctrl", "²"],
    "output": ["ctrl", "a"]
},
``` 

Conversely, we can make ctrl inputs, that makes either ctrl output or normal text. **Be just aware of not doing dangerous stuff with this. It may bug, and delete many things if the suppr key is mentionned above.**

# Special Events

`keys.json`
```json
"special_keys": {
    "end": "²end",
    "reload": "²r",
    "on": "²on",
    "off": "²off"
}
```

These are the special events :

- The "end" makes the programm end.
- The "reload" makes the programm reload the json.
- The "off" makes you able the temporary disable the programm, without stopping it.
- The "on" makes you able the able again then programm to replace what you type.

*Note that adding events make you able to use it, but it won't do anything. If you want to add keys, please do that in the "keys" property.*