# xml2json

### xml
```xml
<Scr>
<Id>1</Id>
<File Active="true">
<FileType>Photo</FileType>
<Src>https://photo_jpg.jpg</Src>
<Rank>1</Rank>
</File>
<File Active="true">
<FileType>Photo</FileType>
<Src>photo_jpg.jpg</Src>
<Rank>2</Rank>
</File>
<Id>2</Id>
<File Active="true">
<FileType>Photo</FileType>
<Src>https://photo_jpg.jpg</Src>
<Rank>1</Rank>
</File>
<File Active="true">
<FileType>Photo</FileType>
<Src>photo_jpg.jpg</Src>
<Rank>2</Rank>
</File>
</Scr>
```

### to json
```json
[
    {
        "Id": {"text": "1"},
        "File": [
            {
                "Active": "true",
                "FileType": {"text": "Photo"},
                "Src": {"text": "https://photo_jpg.jpg"},
                "Rank": {"text": "1"}
            },
            {
                "Active": "true",
                "FileType": {"text": "Photo"},
                "Src": {"text": "photo_jpg.jpg"},
                "Rank": {"text": "2"}
            }
        ]
    },
    {
        "Id": {"text": "2"},
        "File": [
            {
                "Active": "true",
                "FileType": {"text": "Photo"},
                "Src": {"text": "https://photo_jpg.jpg"},
                "Rank": {"text": "1"}
            },
            {
                "Active": "true",
                "FileType": {"text": "Photo"},
                "Src": {"text": "photo_jpg.jpg"},
                "Rank": {"text": "2"}
            }
        ]
    }
]
```
