

## Example response in JSON

```json
{
    "lattice": {
        "a": 3.8774999999999995, 
        "volume": 58.298236734375, 
        "c": 3.8774999999999995, 
        "b": 3.8774999999999995, 
        "alpha": 90.0, 
        "beta": 90.0, 
        "gamma": 90.0
    }, 
    "space_group": {
        "hermann_mauguin": "P 1", 
        "centering": "P", 
        "crystal_system": "Triclinic", 
        "number": 1, 
        "point_group": "1", 
        "is_standard": true, 
        "schoenflies": "C1^1", 
        "laue": "-1", 
        "cctbx_name": "P 1", 
        "hall": " P 1"
    }, 
    "db": {}, 
    "sites": [
        {
            "abc": [
                0.0, 
                0.0, 
                0.0
            ], 
            "meta": {
                "type": "atom"
            }, 
            "name": "Al", 
            "occupancy": 1.0, 
            "label": "Al-0"
        }, 
        {
            "abc": [
                0.0, 
                0.5, 
                0.5
            ], 
            "meta": {
                "type": "atom"
            }, 
            "name": "Pt", 
            "occupancy": 1.0, 
            "label": "Pt-1"
        }, 
        {
            "abc": [
                0.5, 
                0.5, 
                0.0
            ], 
            "meta": {
                "type": "atom"
            }, 
            "name": "Pt", 
            "occupancy": 1.0, 
            "label": "Pt-1"
        }, 
        {
            "abc": [
                -0.5, 
                0.0, 
                0.5
            ], 
            "meta": {
                "type": "atom"
            }, 
            "name": "Pt", 
            "occupancy": 1.0, 
            "label": "Pt-1"
        }
    ], 
    "transforms": [
        {
            "initial_space_group": {
                "hermann_mauguin": "P m -3 m", 
                "centering": "P", 
                "crystal_system": "Cubic", 
                "number": 221, 
                "point_group": "m-3m", 
                "is_standard": true, 
                "schoenflies": "Oh^1", 
                "laue": "m-3m", 
                "cctbx_name": "P m -3 m", 
                "hall": "-P 4 2 3"
            }, 
            "name": "to_niggli"
        }, 
        {
            "initial_space_group": {
                "hermann_mauguin": "P m -3 m", 
                "centering": "P", 
                "crystal_system": "Cubic", 
                "number": 221, 
                "point_group": "m-3m", 
                "is_standard": true, 
                "schoenflies": "Oh^1", 
                "laue": "m-3m", 
                "cctbx_name": "P m -3 m", 
                "hall": "-P 4 2 3"
            }, 
            "name": "to_p1"
        }
    ]
}
```

