from pytest import fixture

from xml2json import Xml2Json


@fixture
def xml_string():
    return """<Scr>
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
    </Scr>"""


def test_xml2json(xml_string):
    json = Xml2Json("Id").parse(xml_string)
    assert json == [
        {
            "Id": {"text": "1"},
            "File": [
                {
                    "Active": "true",
                    "FileType": {"text": "Photo"},
                    "Src": {"text": "https://photo_jpg.jpg"},
                    "Rank": {"text": "1"},
                },
                {
                    "Active": "true",
                    "FileType": {"text": "Photo"},
                    "Src": {"text": "photo_jpg.jpg"},
                    "Rank": {"text": "2"},
                },
            ],
        },
        {
            "Id": {"text": "2"},
            "File": [
                {
                    "Active": "true",
                    "FileType": {"text": "Photo"},
                    "Src": {"text": "https://photo_jpg.jpg"},
                    "Rank": {"text": "1"},
                },
                {
                    "Active": "true",
                    "FileType": {"text": "Photo"},
                    "Src": {"text": "photo_jpg.jpg"},
                    "Rank": {"text": "2"},
                },
            ],
        },
    ]
