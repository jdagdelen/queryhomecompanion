Each material contains multiple computations for different purposes. Each computation is referred to as a "task". This field contains a dictionary of all the tasks performed on this material and their associated task_ids. An example would be:

{'GGA Uniform v2': 'mp-882394', 
'GGA band structure v2': 'mp-885182', 
'GGA+U Uniform v2': 'mp-797269', 
'GGA+U band structure v2': 'mp-797820', 
'GGA+U optimize structure (2x)': 'mp-19017'}











## Example response in JSON

```json
{
    "GGA band structure v2": "mp-940654", 
    "GGA Uniform v2": "mp-940234", 
    "GGA static v2": "mp-925833", 
    "GGA optimize structure (2x)": "mp-1234"
}
```

