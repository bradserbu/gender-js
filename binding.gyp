{
  "include_dirs" : [
    "<!(node -e \"require('nan')\")"
  ],
  "targets": [
    {
       "target_name": "gender",
       "sources": [ "src/gender-js.cc", "src/gender.c"]
    }
  ]
}
