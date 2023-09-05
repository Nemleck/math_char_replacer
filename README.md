# program Presentation

This program can replace what you write (ex: sqrt) with the actual character (for this example, √), or something else.

# Keys Configuration

You can use the presets, but also make your events.

`part of keys.json`
```json
{
    "input": "sqrt",
    "output": "√",
    "params": ["accept_lower_and_upper_case"]
}
```

In this example, every times you write "sqrt", it will be replaced with √.

The parameter "accept_lower_and_upper_case" makes the program accept lower AND upper cases for the input. This means you can write "sqrt" but also "SqRt", or "SQRT", and so on.

`part of keys.json`
```json
{
    "input": "This is ",
    "output": "autocompletion",
    "params": ["keep_text"]
}
```

In this example, we add the parameter "keep_text", that makes the program no longer remove what you write (here "This is ").
This allows you to make autocompletion, for example.

## Adding key combination

`part of keys.json`
```json
{
    "input": "hey",
    "output": ["ctrl", "a"],
    "params": ["keep_text"]
},
```

With this, writting "hey" makes you able now to select all the text (with ctrl + a), and keeps the hey you you wrote with the "keep_text" parameter.

`part of keys.json`
```json
{
    "input": ["ctrl", "²"],
    "output": ["ctrl", "a"]
},
``` 

Conversely, we can make ctrl inputs, that makes either ctrl output or normal text. **Be just aware of not doing dangerous stuff with this, like putting the suppr key. It may bug, and delete many things.**

# Special Events

`part of keys.json`
```json
"special_keys": {
    "end": "²end",
    "reload": "²r",
    "on": "²on",
    "off": "²off"
}
```

These are the special events :

- The "end" ends the program.
- The "reload" reloads the json.
- The "off" temporary disables the program, without stopping it.
- The "on" enables the program.

*Note that adding events make you able to use it, but it won't do anything. If you want to add keys, please do that in the "keys" property.*

# Add external key files

When you add new keys, you may want to organise your keys. That's why you can add external files with new keys.

`math.json`
```json
[
    {
        "input": "sqrt",
        "output": "√"
    },
    {
        "input": "===",
        "output": "⇔"
    },
    {
        "input": "inter",
        "output": "⋂"
    },
    {
        "input": "union",
        "output": "⋃"
    }
]
```

In this new file, you just have to list your keys, same as before, but in the root of the file.

To register it as an external file in the `keys.json`, just add the name of your file (and the extension) in the following list :

`part of keys.json`
```json
"external_keys": [
    "math.json",
    "blahblahblah.json"
],
```